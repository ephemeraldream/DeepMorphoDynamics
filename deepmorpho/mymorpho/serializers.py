from mymorpho.models.cycle_type import CycleType
from mymorpho.models.well_timeline_frames import WellTimelineFrames
from mymorpho.models.embryo import Embryo
from mymorpho.models.whole_image import WholeImage
from mymorpho.models.embryo_in_t import EmbryoInT
from .models.image_with_classification_predictions import (
    ImageWithClassificationPredictions,
)
from .models.images import Images
from rest_framework import serializers
from rest_framework.serializers import (
    Serializer,
    ImageField,
    ListSerializer,
    IntegerField,
    FloatField,
    ListField,
    ModelSerializer,
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
        fields = (
            "wtf_wtl_id",
            "wtf_ed_uuid",
            "wtf_rel_focus",
            "wtf_frame",
            "wtf_dif",
            "wtf_stabilized",
        )


class GetLabelsSerializer(Serializer):
    classification_pred = ListSerializer(child=IntegerField())
    regression_pred = ListSerializer(child=ListSerializer(child=FloatField()))
    hole_pred = IntegerField()
    image = ImageField(max_length=None, use_url=True)

    class Meta:
        fields = ("classification_pred", "regression_pred", "hole_pred", "image")


class EmbryoSerializer(ModelSerializer):
    class Meta:
        fields = ("id",)
        model = Embryo


class EmbryoInTSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "image",
            "source_image",
            "embryo",
            "class_type",
            "well_number",
        )
        model = EmbryoInT


class WholeImageSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "image",
            "time",
        )
        read_only_fields = ("time",)
        model = WholeImage


class WholeImagesSerializer(Serializer):
    images = ListField(child=ImageField())

    class Meta:
        fields = ("images",)
