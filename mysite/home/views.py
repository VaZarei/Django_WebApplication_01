from django.shortcuts import render
from django.views.generic import TemplateView




# Create your views here.


# Static Variables



class HomeView(TemplateView):
    template_name = "home/home.html"


  
class HomeLogoutView(TemplateView):
    template_name = "home/logout.html"
    