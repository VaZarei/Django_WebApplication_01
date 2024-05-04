from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# Static Variables



class HomeView(TemplateView):
    template_name = "home/home.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "my_variable" : "Hello, world!",
            "phoneNumber" : "+44-789-999-54",
                   }
        return context
    
    