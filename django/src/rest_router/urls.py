from rest_framework.routers import DefaultRouter
from .views import ExampleViewSet

router = DefaultRouter()
router.register(r'router', ExampleViewSet, basename='router')

urlpatterns = router.urls
