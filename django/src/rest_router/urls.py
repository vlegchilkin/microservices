from rest_framework.routers import DefaultRouter
from .views import ExampleViewSet, ExampleViewSetOnActions

router = DefaultRouter()
router.register(r'view-set', ExampleViewSet, basename='view-set')
router.register(r'view-set-on-actions', ExampleViewSetOnActions, basename='view-set-on-actions')

urlpatterns = router.urls
