# Generated by Django 4.1.7 on 2023-04-12 21:51

import uuid
from decimal import Decimal

import django.contrib.auth.models
import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=32)),
                ("last_name", models.CharField(max_length=32)),
                (
                    "username",
                    models.CharField(db_index=True, max_length=64, unique=True),
                ),
                (
                    "email",
                    models.EmailField(db_index=True, max_length=254, unique=True),
                ),
                ("phone", models.CharField(max_length=32, null=True, unique=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("email_verified", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(max_length=64)),
                ("number", models.CharField(max_length=16)),
                ("district", models.CharField(blank=True, max_length=32, null=True)),
                ("complement", models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField()),
                (
                    "type",
                    models.CharField(
                        choices=[("online", "Online"), ("presential", "Presencial")],
                        max_length=16,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=128, null=True)),
                ("link", models.CharField(max_length=255, null=True)),
                ("notify_appointment", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Calendar",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, null=True)),
                ("duration", models.PositiveSmallIntegerField()),
                ("interval", models.PositiveSmallIntegerField(default=0)),
                ("is_default", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=32)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amapá"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espirito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MT", "Mato Grosso"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        max_length=4,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Cities",
            },
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profession",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Professional",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("picture", models.CharField(max_length=128, null=True)),
                (
                    "genre",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminimo"), ("O", "Outro")],
                        max_length=1,
                    ),
                ),
                ("birthday", models.DateField(null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "address",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="professional",
                        to="api.address",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="professionals",
                        to="api.plan",
                    ),
                ),
                (
                    "profession",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="professionals",
                        to="api.profession",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professional",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ThirdParty",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[("google-calendar", "Google Calendar")], max_length=32
                    ),
                ),
                ("access_token", models.TextField()),
                ("refresh_token", models.TextField(null=True)),
                ("expire_at", models.DateTimeField(null=True)),
                (
                    "scopes",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=255),
                        blank=True,
                        size=None,
                    ),
                ),
                (
                    "professional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="third_parties",
                        to="api.professional",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Third Parties",
            },
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "week_day",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Domingo"),
                            (1, "Segunda"),
                            (2, "Terça"),
                            (3, "Quarta"),
                            (4, "Quinta"),
                            (5, "Sexta"),
                            (6, "Sábado"),
                        ]
                    ),
                ),
                ("time_start", models.TimeField()),
                ("time_end", models.TimeField()),
                (
                    "calendar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sessions",
                        to="api.calendar",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("partial", models.BooleanField(default=False)),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to="api.appointment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("notify_appointment", models.BooleanField(default=True)),
                ("notify_pending_payment", models.BooleanField(default=True)),
                (
                    "professional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patients",
                        to="api.professional",
                    ),
                ),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="calendar",
            name="professional",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calendars",
                to="api.professional",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="appointments",
                to="api.patient",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="professional",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="appointments",
                to="api.professional",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="session",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="appointment",
                to="api.session",
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to="api.city",
            ),
        ),
        migrations.AddConstraint(
            model_name="calendar",
            constraint=models.UniqueConstraint(
                condition=models.Q(("deleted_at", None)),
                fields=("professional", "is_default", "is_active"),
                name="professional_default_active",
            ),
        ),
    ]
