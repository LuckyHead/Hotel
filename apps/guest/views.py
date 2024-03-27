from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .forms import SignupForm, LoginForm

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

def login(request):
    if request.user.is_authenticated:
        return redirect("hotel_list")
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('hotel_list')
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('login')
        else:
            form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
