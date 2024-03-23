from rest_framework.routers import DefaultRouter

from .views import (
    RoomListViewSet,
    RoomDetailViewSet
)

router=DefaultRouter()
router.register('room', RoomListViewSet, basename='room-list'),
router.register('room/<int:pk>', RoomDetailViewSet, basename='room-detail')

urlpatterns=[]
urlpatterns+=router.urls
