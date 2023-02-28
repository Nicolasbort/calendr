from api.constants.city import StateChoices
from api.models.city import City
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.profile import Profile
from django.core.management.base import BaseCommand

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
        self.stdout.write("Seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("Done.")


def clear_data():
    """Deletes all the table data"""
    Profile.objects.all().delete()
    City.objects.all().delete()
    Plan.objects.all().delete()
    Profession.objects.all().delete()


def create_admin(data):
    """Creates an admin profile"""
    profile = Profile(
        username="admin",
        email="admin@example.com",
        first_name="Admin",
        last_name="Auto",
        genre="M",
        is_staff=True,
        is_superuser=True,
        **data,
    )
    profile.set_password("password")
    profile.save()
    return profile


def create_city(city: dict):
    """Creates a city object"""
    city = City(**city)
    city.save()
    return city


def create_plan():
    """Creates a basic plan object"""
    plan = Plan(name="Básico")
    plan.save()
    return plan


def create_profession():
    """Creates a base profession"""
    profession = Profession(name="Psicólogo")
    profession.save()
    return profession


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
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
        create_city(city)

    plan = create_plan()
    profession = create_profession()
    create_admin({"plan": plan, "profession": profession})
