from django.contrib import admin
from .models import ImageWithClassificationPredictions, Holes

admin.site.register(ImageWithClassificationPredictions)
admin.site.register(Holes)

