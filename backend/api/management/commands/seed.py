import logging
import os

from api.constants.city import StateChoices
from api.models import Address, City, Plan, Profession, Professional, Profile
from django.core.management.base import BaseCommand

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
        logger.info("Seeding data...")
        run_seed(self, options["mode"])
        logger.info("Done.")


def clear_data():
    logger.info("Deleting all database data")

    Profile.all_objects.all().delete()
    Address.objects.all().delete()
    City.objects.all().delete()
    Plan.all_objects.all().delete()
    Profession.all_objects.all().delete()
    Professional.all_objects.all().delete()


def create_profie() -> Profile:
    profile = Profile(
        email="user@example.com",
        username="user",
        first_name="User",
        last_name="Auto",
        is_staff=False,
        is_superuser=False,
    )
    profile.set_password("password")
    profile.save()

    return profile


def create_admin() -> Profile:
    profile = Profile(
        email="admin@example.com",
        username="admin",
        first_name="Admin",
        last_name="Auto",
        is_staff=True,
        is_superuser=True,
    )
    profile.set_password("password")
    profile.save()

    return profile


def create_address(city: City) -> Address:
    return Address.objects.create(
        street="Rua Street",
        number="99",
        district="Bairro",
        complement="Complemento",
        city=city,
    )


def create_city(city: dict) -> City:
    return City.objects.create(**city)


def create_plan() -> Plan:
    plan, _ = Plan.objects.get_or_create(name="Gratuito")
    return plan


def create_profession() -> Profession:
    profession, _ = Profession.objects.get_or_create(name="Psicólogo")
    return profession


def create_professional(address, profession, plan, profile) -> Professional:
    return Professional.objects.create(
        picture="picture.png",
        bio="lorem ipsum",
        genre="M",
        birthday="1995-01-01",
        address=address,
        profession=profession,
        plan=plan,
        profile=profile,
    )


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    if os.environ.get("ENV", "prod") != "dev":
        create_plan()
        create_profession()

        logger.info("Default Plan and Profession created.")
        return

    clear_data()

    if mode == MODE_CLEAR:
        return

    logger.info("Creating models.")

    cities = [
        {"name": "São Paulo", "state": StateChoices.SP},
        {"name": "Rio de Janeiro", "state": StateChoices.RJ},
        {"name": "Curitiba", "state": StateChoices.PR},
        {"name": "Florianópolis", "state": StateChoices.SC},
    ]

    # Creating cities
    for city in cities:
        last_city = create_city(city)

    address = create_address(last_city)
    plan = create_plan()
    profession = create_profession()
    profile = create_profie()
    create_professional(address, profession, plan, profile)
    create_admin()
