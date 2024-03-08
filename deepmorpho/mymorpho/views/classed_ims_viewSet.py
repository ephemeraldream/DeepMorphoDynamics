from deepmorpho.mymorpho.models.image_with_classification_predictions import ImageWithClassificationPredictions
from deepmorpho.mymorpho.serializers import ClassificationSerializer


class ClassedImsViewSet(viewsets.ModelViewSet):
    queryset = ImageWithClassificationPredictions.objects.all()
    serializer_class = ClassificationSerializer
    permission_classes = [AllowAny]