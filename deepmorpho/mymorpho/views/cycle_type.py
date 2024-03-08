from mymorpho.models.cycle_type import CycleType
from mymorpho.serializers import CycleTypeSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class CycleTypeViewSet(ModelViewSet):
    queryset = CycleType.objects.all()
    serializer_class = CycleTypeSerializer
    permission_classes = (AllowAny,)
