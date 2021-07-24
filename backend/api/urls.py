from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'brand', BrandViewSet)
router.register(r'car', CarViewSet)
router.register(r'dealer', DealerViewSet)

urlpatterns = router.urls

