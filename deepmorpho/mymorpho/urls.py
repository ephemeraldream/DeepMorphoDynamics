from mymorpho.views.image import ImageViewSet
from mymorpho.views.cycle_type import CycleTypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cycle_type", CycleTypeViewSet, basename="cycle_type")
router.register("images", ImageViewSet)

urlpatterns = router.urls
