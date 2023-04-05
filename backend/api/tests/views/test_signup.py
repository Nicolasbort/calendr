import json

import pytest
from api.models.address import Address
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.profile import Profile
from django.urls import reverse


@pytest.mark.django_db
class TestSignupViewSet:
    @staticmethod
    def test_signup_professional(admin_api, city, plan, profession):
        url = reverse("api:sign-up-professional")

        data = {
            "picture": "picture.png",
            "bio": "lorem ipsum",
            "genre": "M",
            "birthday": "1995-01-01",
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "professional@example.com",
            "username": "professional",
            "phone": "99999999",
            "address": {
                "street": "Rua",
                "number": "999",
                "district": "Bairro",
                "complement": "Complemento",
                "city": str(city.id),
            },
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Professional.objects.count() == 1

        professional = Professional.objects.first()
        profile = professional.profile
        address = professional.address

        assert professional.picture == "picture.png"
        assert professional.bio == "lorem ipsum"
        assert professional.genre == "M"
        assert professional.birthday.strftime("%Y-%m-%d") == "1995-01-01"

        assert profile.first_name == "First"
        assert profile.last_name == "Last"
        assert profile.email == "professional@example.com"
        assert profile.username == "professional"
        assert profile.phone == "99999999"
        assert profile.password is not None

        assert address.street == "Rua"
        assert address.number == "999"
        assert address.district == "Bairro"
        assert address.complement == "Complemento"
        assert str(address.city.id) == str(city.id)

    @staticmethod
    def test_signup_atomiticy(admin_api, city, plan, profession):
        url = reverse("api:sign-up-professional")

        data = {
            "picture": "picture.png",
            "bio": "lorem ipsum",
            "genre": "M",
            "birthday": "date to throw error",
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "professional@example.com",
            "username": "professional",
            "phone": "99999999",
            "address": {
                "street": "Rua",
                "number": "999",
                "district": "Bairro",
                "complement": "Complemento",
                "city": str(city.id),
            },
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        assert Professional.objects.count() == 0
        assert Address.objects.count() == 0
        assert Profile.objects.count() == 1  # Only the admin profile

    @staticmethod
    def test_signup_patient(admin_api, professional):
        url = reverse("api:sign-up-patient")

        data = {
            "professional": str(professional.id),
            "notify_pending_payment": False,
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "patient@example.com",
            "username": "patient",
            "phone": "99999999",
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        assert Patient.objects.count() == 1

        patient = Patient.objects.first()
        profile = patient.profile

        assert patient.notify_pending_payment == False

        assert profile.first_name == "First"
        assert profile.last_name == "Last"
        assert profile.email == "patient@example.com"
        assert profile.username == "patient"
        assert profile.phone == "99999999"
        assert profile.password is not None

    @staticmethod
    def test_signup_patient_atomocity(admin_api, professional):
        url = reverse("api:sign-up-patient")

        data = {
            "professional": str(professional.id),
            "notify_pending_payment": False,
            "first_name": "First",
            "last_name": "Last",
            "password": "password",
            "email": "email to throw error",
            "username": "patient",
            "phone": "99999999",
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        assert Patient.objects.count() == 0
        assert Profile.objects.count() == 2  # Only the admin and professional profile
