from django.contrib import admin

from .models.image_with_classification_predictions import ImageWithClassificationPredictions

from .models.images import Images
from .models.holes import Holes

admin.site.register(ImageWithClassificationPredictions)
admin.site.register(Holes)
admin.site.register(Images)

