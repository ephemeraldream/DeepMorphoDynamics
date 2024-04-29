from mymorpho.views.image_view_set import ImageViewSet
from mymorpho.views.cycle_type import CycleTypeViewSet
from mymorpho.views.embryo import EmbryoViewSet
from mymorpho.views.embryo_in_t import EmbryoInTViewSet
from mymorpho.views.whole_image import WholeImageViewSet
from mymorpho.views.well_timeline_view import WellTimelineFrameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("embryo", EmbryoViewSet, basename="embryo")
router.register("embryo_in_t", EmbryoInTViewSet, basename="embryo_in_t")
router.register("whole_image", WholeImageViewSet, basename="whole_image")
urlpatterns = router.urls
