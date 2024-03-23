from rest_framework.routers import DefaultRouter

from .views import (
    GuestListViewSet,
    GuestDetailViewSet
)

router=DefaultRouter()
router.register('guest', GuestListViewSet, basename='guest-list'),
router.register('guest/<int:pk>', GuestDetailViewSet, basename='guest-detail')

urlpatterns=[]
urlpatterns+=router.urls
