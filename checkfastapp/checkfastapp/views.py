from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
  return render(request, 'home.html')

def about_us(request):
  return render(request, 'aboutus.html')

def pricing(request):
  return render(request, 'pricing.html')