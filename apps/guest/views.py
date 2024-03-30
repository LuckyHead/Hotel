from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .forms import SignupForm

from .serializers import GuestSerializer
from apps.guest.models import Guest

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=SignupForm()
    return render(request, "registration/signup.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password. Please try again.'
    else:
        error_message = None

    return render(request, 'registration/login.html', {'error_message': error_message})
