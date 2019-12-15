import uuid
from django.db import models


class Registration(models.Model):
    """Pet registration information"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name="Дата регистрации")
    # TODO!

    def __str__(self):
        return self.date.strftime("%d-%m-%Y")


class Owner(models.Model):
    """Information about owner"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256, verbose_name="Имя")
    lastname = models.CharField(max_length=256, verbose_name="Фамилия")
    note = models.CharField(max_length=256, verbose_name="Описание")

    def __str__(self):
        return self.firstname + " " + self.lastname
