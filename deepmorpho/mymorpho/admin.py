from django.contrib import admin
from .models import ImageWithClassificationPredictions, Holes, Images

admin.site.register(ImageWithClassificationPredictions)
admin.site.register(Holes)
admin.site.register(Images)

