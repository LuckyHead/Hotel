from rest_framework.routers import DefaultRouter

from .views import (
    RoomViewSet,
    RoomDetailViewSet
)

router=DefaultRouter()
router.register('room', RoomViewSet, basename='room-list'),
router.register('room/<int:pk>', RoomDetailViewSet, basename='room-detail')

urlpatterns=[]
urlpatterns+=router.urls
