from django.db import models


class Images(models.Model):
    subgroup_id = models.CharField(max_length=50)
    image = models.ImageField()