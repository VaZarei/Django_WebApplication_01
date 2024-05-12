from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ArticleModel

# Create your views here.




class ArticleListView(ListView):
    model = ArticleModel
    template_name = "article/ArticleListView.html"
    context_object_name  = "articles"

class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = "article/ArticleDetailView.html"
    context_object_name  = "articles"