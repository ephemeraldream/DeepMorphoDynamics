from mymorpho.models.images import Images
from rest_framework import viewsets
from mymorpho.serializers import ImagesSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser, FormParser)
