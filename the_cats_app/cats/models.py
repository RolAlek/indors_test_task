from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Cat(models.Model):
    name = models.CharField(verbose_name="Кличка", max_length=32)
    color = models.CharField(verbose_name="Окрас", max_length=16)
    hairiness = models.CharField(verbose_name="Волосатость", max_length=16)
    birth_year = models.IntegerField(verbose_name="Год")

    owner = models.ForeignKey(
        User,
        related_name="cats",
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owner'],
                name='unique_name_owner',
            ),
        ]

    def __str__(self) -> str:
        return self.name
