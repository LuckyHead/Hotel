from rest_framework.routers import DefaultRouter

from .views import (
    HotelListViewSet,
    HotelDetailViewSet
)

router=DefaultRouter()
router.register('hotel', HotelListViewSet, basename='hotel-list'),
router.register('hotel/<int:pk>', HotelDetailViewSet, basename='hotel-detail')

urlpatterns=[]
urlpatterns+=router.urls