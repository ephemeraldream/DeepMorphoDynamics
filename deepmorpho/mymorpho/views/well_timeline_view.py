


from mymorpho.models.well_timeline_frames import WellTimelineFrames
from mymorpho.serializers import WellTimelineFramesSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class WellTimelineFrameViewSet(ModelViewSet):
    queryset = WellTimelineFrames.objects.all().filter(wtf_rel_focus=3)
    serializer_class = WellTimelineFramesSerializer
    permission_classes = (AllowAny,)