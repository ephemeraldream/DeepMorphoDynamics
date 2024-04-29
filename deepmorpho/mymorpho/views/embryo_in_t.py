from mymorpho.models.embryo_in_t import EmbryoInT
from rest_framework import viewsets
from mymorpho.serializers import EmbryoInTSerializer
from rest_framework.permissions import AllowAny



class EmbryoInTViewSet(viewsets.ModelViewSet):
    queryset = EmbryoInT.objects.all()
    serializer_class = EmbryoInTSerializer
    permission_classes = [AllowAny]


