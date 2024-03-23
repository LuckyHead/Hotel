from rest_framework.routers import DefaultRouter

from .views import (
    BookingListViewSet,
    BookingDetailViewSet
)

router=DefaultRouter()
router.register('booking', BookingListViewSet, basename='booking-list'),
router.register('booking/<int:pk>', BookingDetailViewSet, basename='booking-detail')

urlpatterns=[]
urlpatterns+=router.urls