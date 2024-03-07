from django.db import models


class Images(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    subgroup_id = models.CharField(max_length=50)
    image = models.ImageField()


class ImageWithClassificationPredictions(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    group_id = models.CharField(max_length=50)
    image = models.ImageField()
    locations = models.TextField()
    classification = models.TextField()
    dimension = models.CharField(max_length=50)


class Holes(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    group_id = models.CharField(max_length=50)
    subgroup_id = models.CharField(max_length=50)
    image = models.ImageField()
    condition = models.CharField(max_length=50)

