from mymorpho.models.embryo import Embryo
from rest_framework import viewsets
from mymorpho.serializers import EmbryoSerializer
from rest_framework.permissions import AllowAny



class EmbryoViewSet(viewsets.ModelViewSet):
    queryset = Embryo.objects.all()
    serializer_class = EmbryoSerializer
    permission_classes = [AllowAny]


