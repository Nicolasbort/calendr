import logging

from api.constants.city import StateChoices
from api.models import Address, City, Plan, Profession, Professional, Profile
from app.settings import ENV
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

    Profile.global_objects.all().delete()
    Address.objects.all().delete()
    City.objects.all().delete()
    Plan.global_objects.all().delete()
    Profession.global_objects.all().delete()
    Professional.global_objects.all().delete()


def create_profie() -> Profile:
    profile = Profile(
        email="user@example.com",
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
    return Plan.objects.create(name="Básico")


def create_profession() -> Profession:
    return Profession.objects.create(name="Psicólogo")


def create_professional(address, profession, plan, profile) -> Professional:
    return Professional.objects.create(
        picture="picture.png",
        bio="lorem ipsu^m",
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
    if ENV != "dev":
        logger.info("Can't run seed in non 'dev' environemt")
        return

    clear_data()

    if mode == MODE_CLEAR:
        return

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
