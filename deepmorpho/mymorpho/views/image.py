from rest_framework.viewsets import ModelViewSet
from mymorpho.models.images import Images
from mymorpho.serializers import ImagesSerializer
from rest_framework.permissions import AllowAny


class ImageViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [AllowAny]
