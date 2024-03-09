from mymorpho.views.image_view_set import ImageViewSet
from mymorpho.views.cycle_type import CycleTypeViewSet
from mymorpho.views.well_timeline_view import WellTimelineFrameViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cycle_type", CycleTypeViewSet, basename="cycle_type")
router.register(r"well_timeline_frame", WellTimelineFrameViewSet, basename="well_timeline_frame")
router.register("images", ImageViewSet)
router
urlpatterns = router.urls
