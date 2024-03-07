from rest_framework import serializers
from .models import ImageWithClassificationPredictions, Holes, Images
from rest_framework.serializers import (
    Serializer,
    ListSerializer,
    IntegerField,
    FloatField,
    ImageField
)

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'subgroup_id', 'image']

class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageWithClassificationPredictions
        fields = ['id', 'group_id', 'image', 'locations', 'classification', 'dimension']


class HolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageWithClassificationPredictions
        fields = ['id', 'group_id', 'subgroup_id', 'image', 'condition']
