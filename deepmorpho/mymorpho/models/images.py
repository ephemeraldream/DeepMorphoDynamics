from django.db import models


class Images(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    subgroup_id = models.CharField(max_length=50)
    image = models.ImageField()