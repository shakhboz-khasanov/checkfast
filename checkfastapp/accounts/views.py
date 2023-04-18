from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Account


from django.views.generic import CreateView, UpdateView
from .forms import RegisterForm, ProfileForm
# Create your views here.

def register(request):
  return render(request, 'register.html') 

# Sign Up View
class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
   
def login(request):
    return render(request, 'login.html')

# Edit Profile View
class ProfileView(UpdateView):
    model = Account
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'profile.html'
    

def dashboard(request):
  return render(request, 'dashboard.html') 