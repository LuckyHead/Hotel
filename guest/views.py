from rest_framework.viewsets import ModelViewSet

from .serializers import GuestSerializer
from .models import User

class GuestListViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=GuestSerializer

class GuestDetailViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=GuestSerializer