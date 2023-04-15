import json

import pytest
from api.constants.city import StateChoices
from api.models.address import Address
from api.models.city import City
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.profile import Profile
from django.urls import reverse


@pytest.mark.django_db
class TestSignupViewSet:
    @staticmethod
    def test_signup_professional(no_auth_api, plan, profession):
        url = reverse("api:sign-up-professional")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "professional@example.com",
            "birthday": "1995-01-01",
            "phone": "99999999",
            "registration_number": "32941-32",
            "password": "password",
            "address": {
                "zip_code": "99999999",
                "street": "Rua",
                "number": "999",
                "district": "Bairro",
                "complement": "Complemento",
                "city": {
                    "state": StateChoices.RS,
                    "name": "Pelotas",
                },
            },
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Professional.objects.count() == 1
        assert City.objects.count() == 1

        professional = Professional.objects.first()
        profile = professional.profile
        address = professional.address

        assert professional.plan.id == plan.id
        assert professional.profession.id == profession.id
        assert professional.registration_number == data["registration_number"]
        assert professional.birthday.strftime("%Y-%m-%d") == "1995-01-01"
        assert professional.picture is None
        assert professional.genre is None
        assert professional.bio is None

        assert profile.first_name == data["first_name"]
        assert profile.last_name == data["last_name"]
        assert profile.email == data["email"]
        assert (
            profile.username == data["first_name"].lower() + data["last_name"].lower()
        )
        assert profile.phone == data["phone"]
        assert profile.password is not None

        assert address.street == data["address"]["street"]
        assert address.number == data["address"]["number"]
        assert address.district == data["address"]["district"]
        assert address.complement == data["address"]["complement"]

    @staticmethod
    def test_signup_professional_city_already_exists(
        no_auth_api, city, plan, profession
    ):
        url = reverse("api:sign-up-professional")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "professional@example.com",
            "birthday": "1995-01-01",
            "phone": "99999999",
            "registration_number": "32941-32",
            "password": "password",
            "address": {
                "zip_code": "99999999",
                "street": "Rua",
                "number": "999",
                "district": "Bairro",
                "complement": "Complemento",
                "city": {
                    "state": city.state,
                    "name": city.name,
                },
            },
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Professional.objects.count() == 1
        assert City.objects.count() == 1

        professional = Professional.objects.first()
        profile = professional.profile
        address = professional.address

        assert professional.plan.id == plan.id
        assert professional.profession.id == profession.id
        assert professional.registration_number == data["registration_number"]
        assert professional.birthday.strftime("%Y-%m-%d") == "1995-01-01"
        assert professional.picture is None
        assert professional.genre is None
        assert professional.bio is None

        assert profile.first_name == data["first_name"]
        assert profile.last_name == data["last_name"]
        assert profile.email == data["email"]
        assert (
            profile.username == data["first_name"].lower() + data["last_name"].lower()
        )
        assert profile.phone == data["phone"]
        assert profile.password is not None

        assert address.street == data["address"]["street"]
        assert address.number == data["address"]["number"]
        assert address.district == data["address"]["district"]
        assert address.complement == data["address"]["complement"]

        assert address.city.state == city.state
        assert address.city.name == city.name

    @staticmethod
    def test_signup_professional_no_address(no_auth_api, plan, profession):
        url = reverse("api:sign-up-professional")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "professional@example.com",
            "birthday": "1995-01-01",
            "phone": "99999999",
            "registration_number": "32941-32",
            "password": "password",
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Professional.objects.count() == 1
        assert Address.objects.count() == 0
        assert City.objects.count() == 0

        professional = Professional.objects.first()
        profile = professional.profile

        assert professional.plan.id == plan.id
        assert professional.profession.id == profession.id
        assert professional.registration_number == data["registration_number"]
        assert professional.birthday.strftime("%Y-%m-%d") == "1995-01-01"
        assert professional.picture is None
        assert professional.genre is None
        assert professional.bio is None

        assert profile.first_name == data["first_name"]
        assert profile.last_name == data["last_name"]
        assert profile.email == data["email"]
        assert (
            profile.username == data["first_name"].lower() + data["last_name"].lower()
        )
        assert profile.phone == data["phone"]
        assert profile.password is not None

    @staticmethod
    def test_signup_professional_same_username(no_auth_api, profile, plan, profession):
        profile.username = "firstlast"
        profile.save(update_fields=["username"])

        url = reverse("api:sign-up-professional")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "professional@example.com",
            "birthday": "1995-01-01",
            "phone": "99999999",
            "registration_number": "32941-32",
            "password": "password",
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Professional.objects.count() == 1

        professional = Professional.objects.first()
        profile = professional.profile

        assert profile.username != "firstlast"
        assert "firstlast" in profile.username

    @staticmethod
    def test_signup_professional_atomiticy(no_auth_api, plan, profession):
        url = reverse("api:sign-up-professional")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "invalid email",
            "birthday": "date to throw error",
            "phone": "99999999",
            "registration_number": "32941-32",
            "password": "password",
            "address": {
                "zip_code": "99999999",
                "street": "Rua",
                "number": "999",
                "district": "Bairro",
                "complement": "Complemento",
                "city": {
                    "state": StateChoices.SC,
                    "name": "Floripa",
                },
            },
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        assert Professional.objects.count() == 0
        assert Address.objects.count() == 0
        assert City.objects.count() == 0
        assert Profile.objects.count() == 0

        response_data = response.json()

        assert "birthday" in response_data
        assert "email" in response_data

    @staticmethod
    def test_signup_patient(no_auth_api, professional):
        url = reverse("api:sign-up-patient")

        data = {
            "professional": str(professional.id),
            "notify_pending_payment": False,
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "patient@example.com",
            "phone": "99999999",
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Patient.objects.count() == 1

        patient = Patient.objects.first()
        profile = patient.profile

        assert patient.notify_pending_payment == False

        assert profile.first_name == data["first_name"]
        assert profile.last_name == data["last_name"]
        assert profile.email == data["email"]
        assert (
            profile.username == data["first_name"].lower() + data["last_name"].lower()
        )
        assert profile.phone == data["phone"]
        assert profile.password is not None

    @staticmethod
    def test_signup_patient_atomiticy(no_auth_api, professional):
        url = reverse("api:sign-up-patient")

        data = {
            "professional": str(professional.id),
            "notify_pending_payment": False,
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "email to throw error",
            "phone": "99999999",
        }

        response = no_auth_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        assert Patient.objects.count() == 0
        assert Profile.objects.count() == 1  # Only the professional profile
