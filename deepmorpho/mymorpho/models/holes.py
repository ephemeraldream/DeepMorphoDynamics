from django.db import models


class Holes(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    group_id = models.CharField(max_length=50)
    subgroup_id = models.CharField(max_length=50)
    image = models.ImageField()
    condition = models.CharField(max_length=50)