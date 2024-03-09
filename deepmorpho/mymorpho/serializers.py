from mymorpho.models.cycle_type import CycleType
from mymorpho.models.well_timeline_frames import WellTimelineFrames
from .models.image_with_classification_predictions import (
    ImageWithClassificationPredictions,
)
from .models.images import Images
from rest_framework import serializers
from rest_framework.serializers import (
    Serializer,
    ListSerializer,
    IntegerField,
    FloatField,
)


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

class WellTimelineFramesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellTimelineFrames
        fields = ("wtf_wtl_id", "wtf_ed_uuid", "wtf_rel_focus", "wtf_frame", "wtf_dif", "wtf_stabilized")


class GetLabelsSerializer(Serializer):
    classification_pred = ListSerializer(child=IntegerField())
    regression_pred = ListSerializer(child=ListSerializer(child=FloatField()))
    hole_pred = IntegerField()

    class Meta:
        fields = (
            "classification_pred",
            "regression_pred",
            "hole_pred",
        )