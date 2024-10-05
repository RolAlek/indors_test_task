from django.db import models


class Cat(models.Model):
    name = models.CharField(verbose_name='Кличка', max_length=32)
    color = models.CharField(verbose_name='Окрас',max_length=16)
    hairiness = models.CharField(verbose_name='Волосатость', max_length=16)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return self.name
