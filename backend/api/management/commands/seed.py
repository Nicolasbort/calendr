import datetime
import itertools
import logging
import os
import random

from api.constants.appointment import TypeChoices
from api.constants.city import StateChoices
from api.constants.profile import GenreChoices
from api.constants.session import WeekDayChoices
from api.models import (
    Address,
    Appointment,
    Calendar,
    City,
    Plan,
    Profession,
    Professional,
    Profile,
    Session,
)
from api.models.patient import Patient
from api.utils.datetime import add_minutes_to_time
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from faker import Faker

logger = logging.getLogger("django")

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = "refresh"

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        logger.info("Running seed...")
        run_seed(self, options["mode"])
        logger.info("Done.")


def clear_data():
    logger.info("Deleting all database data")

    Profile.all_objects.all().delete()
    Address.all_objects.all().delete()
    City.all_objects.all().delete()
    Plan.all_objects.all().delete()
    Profession.all_objects.all().delete()
    Appointment.all_objects.all().delete()
    Session.all_objects.all().delete()
    Patient.all_objects.all().delete()
    Calendar.all_objects.all().delete()
    Professional.all_objects.all().delete()


def create_default_plan() -> Plan:
    plan, _ = Plan.objects.get_or_create(name="Gratuito")
    return plan


def create_default_profession() -> Profession:
    profession, _ = Profession.objects.get_or_create(name="Psicólogo")
    return profession


def create_admin() -> Profile:
    profile = Profile(
        email="admin@example.com",
        username="admin",
        first_name="Admin",
        last_name="Auto",
        phone="11999999999",
        is_staff=True,
        is_superuser=True,
        email_verified=True,
    )
    profile.set_password("password")
    profile.save()

    return profile


def create_cities(faker: Faker, number) -> list[City]:
    cities = []

    for i in range(number):
        cities.append(
            City(name=faker.city(), state=random.choice(StateChoices.choices)[0])
        )

    return City.objects.bulk_create(cities)


def create_addresses(faker: Faker, cities) -> list[Address]:
    addresses = []

    for city in cities:
        addresses.append(
            Address(
                city=city,
                street=faker.street_name(),
                number=faker.building_number(),
                district=faker.word(),
                complement=faker.word(),
            )
        )

    return Address.objects.bulk_create(addresses)


def create_profiles(faker: Faker, number) -> list[Profile]:
    profiles = []

    for i in range(number):
        profiles.append(
            Profile(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                username=f"{faker.word()}_{faker.word()}",
                email=faker.email(),
                password=make_password("password"),
                email_verified=faker.boolean(chance_of_getting_true=40),
                phone=faker.msisdn(),
            )
        )

    return Profile.objects.bulk_create(profiles)


def create_professionals(
    faker: Faker,
    profiles: list[Profile],
    addresses: list[Address],
    plan: Plan,
    profession: Profession,
) -> list[Professional]:
    professionals = []

    for profile, address in itertools.zip_longest(profiles, addresses):
        professionals.append(
            Professional(
                profession=profession,
                plan=plan,
                address=address,
                profile=profile,
                picture=faker.file_name(category="image"),
                genre=random.choice(GenreChoices.choices)[0],
                birthday=faker.date_of_birth(minimum_age=18, maximum_age=80),
                bio=faker.sentence(),
            )
        )

    return Professional.objects.bulk_create(professionals)


def create_patients(
    faker: Faker,
    profiles: list[Profile],
    professionals: list[Professional],
) -> list[Patient]:
    patients = []

    for profile in profiles:
        patients.append(
            Patient(
                profile=profile,
                professional=random.choice(professionals),
                notify_appointment=faker.boolean(chance_of_getting_true=80),
                notify_pending_payment=faker.boolean(chance_of_getting_true=70),
            )
        )

    return Patient.objects.bulk_create(patients)


def create_calendars(
    faker: Faker,
    professionals: list[Professional],
) -> list[Calendar]:
    calendars = []

    duration_choices = [30, 45, 50, 60]
    interval_choices = [10, 15, 10, 0]
    index = random.randint(0, 3)

    for professional in professionals:
        calendars.append(
            Calendar(
                professional=professional,
                name=faker.color_name(),
                duration=duration_choices[index],
                interval=interval_choices[index],
                is_default=True,
                is_active=True,
            )
        )

    return Calendar.objects.bulk_create(calendars)


def create_sessions(
    faker: Faker,
    number: int,
    calendars: list[Calendar],
) -> list[Session]:
    sessions = []

    session_per_calendar = round(number / len(calendars))
    week_day_choices = WeekDayChoices.choices

    for calendar in calendars:
        last_time_end = datetime.time(8, 0, 0)

        for _ in range(session_per_calendar):
            time_start = last_time_end
            time_end = add_minutes_to_time(
                last_time_end, calendar.duration + calendar.interval
            )

            last_time_end = time_end

            sessions.append(
                Session(
                    calendar=calendar,
                    week_day=random.choice(week_day_choices)[0],
                    time_start=time_start,
                    time_end=time_end,
                )
            )

    return Session.objects.bulk_create(sessions)


def get_random_date_by_weekday(weekday: int) -> datetime.date:
    thirdy_days_ago = datetime.datetime.now().date() - datetime.timedelta(days=30)

    while thirdy_days_ago.weekday() != weekday:
        thirdy_days_ago += datetime.timedelta(days=1)

    return thirdy_days_ago


def create_appointments(
    faker: Faker,
    sessions: list[Session],
    professionals: list[Professional],
    patients: list[Patient],
) -> list[Appointment]:
    appointments = []

    for session in sessions:
        appointments.append(
            Appointment(
                professional=random.choice(professionals),
                patient=random.choice(patients),
                session=session,
                date=get_random_date_by_weekday(
                    WeekDayChoices.to_python(session.week_day)
                ),
                type=random.choice(TypeChoices.choices)[0],
                note=faker.sentence(),
                link=faker.url(),
                notify_appointment=faker.boolean(chance_of_getting_true=80),
            )
        )

    return Appointment.objects.bulk_create(appointments)


@atomic
def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    if os.environ.get("ENV", "prod") != "dev":
        create_default_plan()
        create_default_profession()

        logger.info("Default Plan and Profession created.")
        return

    clear_data()

    if mode == MODE_CLEAR:
        return

    logger.info("Seeding data")

    plan = create_default_plan()
    profession = create_default_profession()
    create_admin()

    TOTAL_PATIENTS = 15
    TOTAL_PROFESSIONALS = 5
    TOTAL_CITIES = round(TOTAL_PROFESSIONALS / 2)
    TOTAL_CALENDARS = round(TOTAL_PROFESSIONALS / 2)
    TOTAL_SESSIONS = TOTAL_CALENDARS * 10
    TOTAL_APPOINTMENTS = TOTAL_CALENDARS

    logger.info(
        f"""Amount of data being created:
        \tCities: {TOTAL_CITIES}
        \tAddresses: {TOTAL_CITIES}
        \tProfiles: {TOTAL_PATIENTS + TOTAL_PROFESSIONALS}
        \tProfessionals: {TOTAL_PROFESSIONALS}
        \tPacientes: {TOTAL_PATIENTS}
        \tCalendars: {TOTAL_CALENDARS}
        \tSessions: {TOTAL_SESSIONS}
        \tAppointments: {TOTAL_APPOINTMENTS}"""
    )

    logger.info("This process may take a while...")

    faker = Faker("pt_BR")

    cities = create_cities(faker, TOTAL_CITIES)
    addresses = create_addresses(faker, cities)
    profiles = create_profiles(faker, TOTAL_PATIENTS + TOTAL_PROFESSIONALS)
    professionals = create_professionals(
        faker,
        profiles[:TOTAL_PROFESSIONALS],
        addresses,
        plan,
        profession,
    )
    patients = create_patients(faker, profiles[TOTAL_PROFESSIONALS:], professionals)
    calendars = create_calendars(faker, professionals[:TOTAL_CALENDARS])
    sessions = create_sessions(faker, TOTAL_SESSIONS, calendars)
    appointments = create_appointments(
        faker, sessions[:TOTAL_APPOINTMENTS], professionals, patients
    )
