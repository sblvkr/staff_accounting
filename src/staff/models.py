from django.db import models


class Position(models.Model):
    """Model Positions."""
    title = models.CharField(
        max_length=150,
        blank=False,
    )

    class Meta:
        default_related_name = 'positions'

    def __str__(self) -> str:
        return self.title


class Employer(models.Model):
    """Model Employers"""
    name = models.CharField(
        max_length=100,
        blank=False,
    )
    surname = models.CharField(
        max_length=100,
        blank=False,
    )
    patronymic = models.CharField(
        max_length=100,
        blank=False,
    )
    date_contract = models.DateField()
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_DEFAULT,
        default=1,
        blank=False,
    )

    class Meta:
        default_related_name = 'employers'

    def __str__(self) -> str:
        return f'{self.name} {self.surname} - {self.position}'
