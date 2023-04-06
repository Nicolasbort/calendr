from functools import cached_property

from api.models.base_model import BaseModel
from api.models.city import City
from django.db import models


class Address(BaseModel):
    street = models.CharField(max_length=64)
    number = models.CharField(max_length=16)
    district = models.CharField(max_length=32, null=True, blank=True)
    complement = models.CharField(max_length=32, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="addresses")

    def __str__(self) -> str:
        return f"{self.street, self.number}"

    @cached_property
    def full_address(self):
        address = f"{self.street}, {self.number}"
        address += f", {self.complement}" if self.complement else ""
        address += f", {self.district}" if self.district else ""
        address += f", {self.city.name} - {self.city.state}"

        return address

    class Meta:
        verbose_name_plural = "Addresses"
