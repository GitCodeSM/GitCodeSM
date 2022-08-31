
# Create your views here.
from django.shortcuts import render
from django.contrib import admin

# Create your views here.
def home(request):
    return render(request, "home.html")

def plan_page(request):
    return render(request, "plan_page.html")
