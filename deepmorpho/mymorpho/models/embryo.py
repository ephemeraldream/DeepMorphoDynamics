from django.db import models



class Embryo(models.Model):
    id = models.TextField(max_length=100, primary_key=True, unique=True)





