from django.db import models


class Embryo(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название эмбриона",
        null=True,
        blank=True,
    )
