from mymorpho.models.cycle_type import CycleType
from .models.image_with_classification_predictions import (
    ImageWithClassificationPredictions,
)
from .models.images import Images
from rest_framework import serializers


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "subgroup_id", "image"]


class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageWithClassificationPredictions
        fields = ["id", "group_id", "image", "locations", "classification", "dimension"]


class HolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageWithClassificationPredictions
        fields = ["id", "group_id", "subgroup_id", "image", "condition"]


class CycleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleType
        fields = ("ct_id", "ct_tname")
