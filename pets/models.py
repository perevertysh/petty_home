import uuid

from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Порода")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Pet(models.Model):
    """Main pet description"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="Кличка")
    age = models.IntegerField(verbose_name="Возраст",
                              validators=[validators.MaxValueValidator(100)])
    doc = models.ForeignKey('petdocs.Registration', on_delete=models.CASCADE,
                            verbose_name="Регистрационный документ")
    breed = models.ForeignKey('pets.Breed', on_delete=models.CASCADE,
                              verbose_name="Порода")
    owner = models.ForeignKey("petdocs.Owner", on_delete=models.CASCADE,
                              verbose_name="Владелец", blank=True, null=True)

    def make_word_end(self):
        word = "студентов"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.breed,
                                    self.make_word_end())
