from rest_framework.routers import DefaultRouter

from .views import (
    BookingViewSet,
    BookingDetailViewSet,
)

router=DefaultRouter()
router.register('booking', BookingViewSet, basename='booking-list-api'),
router.register('booking/<int:pk>', BookingDetailViewSet, basename='booking-detail-api')

urlpatterns=[]
urlpatterns+=router.urls