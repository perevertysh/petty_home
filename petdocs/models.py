import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models

from pets.models import Pet


class Registration(models.Model):
    """Pet registration information"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name="Дата регистрации")
    cage = models.CharField(max_length=10, verbose_name=_("Номер клетки"))
    reg_num = models.CharField(max_length=256, auto_created=True,
                               null=True, blank=True,
                               verbose_name=_("Регистрационный номер"))

    # pet = models.ForeignKey("pets.Pet", on_delete=models.CASCADE,
    #                         verbose_name=_("Питомец"),
    #                         null=False, related_name="registration_pet")

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")


class Owner(models.Model):
    """Information about owner"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256, verbose_name=_("Имя"))
    lastname = models.CharField(max_length=256, verbose_name=_("Фамилия"))
    note = models.CharField(max_length=256, verbose_name=_("Описание"))

    def __str__(self):
        return "{} {}".format(self.lastname, self.firstname)
