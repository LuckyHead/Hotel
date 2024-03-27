from rest_framework.routers import DefaultRouter

from .views import (
    GuestViewSet,
    GuestDetailViewSet
)

router=DefaultRouter()
router.register('guest', GuestViewSet, basename='guest-list'),
router.register('guest/<int:pk>', GuestDetailViewSet, basename='guest-detail')

urlpatterns=[]
urlpatterns+=router.urls
