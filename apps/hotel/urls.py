from rest_framework.routers import DefaultRouter

from .views import (
    HotelViewSet,
    HotelDetailViewSet
)

router=DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel-list'),
router.register('hotel/<int:pk>', HotelDetailViewSet, basename='hotel-detail')

urlpatterns=[]
urlpatterns+=router.urls