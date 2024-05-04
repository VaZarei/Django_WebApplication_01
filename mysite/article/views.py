from django.shortcuts import render
from django.views.generic import ListView
from .models import ArticleModel

# Create your views here.




class ArticleListView(ListView):
    model = ArticleModel
    template_name = "article/article.html"
    context_object_name  = "articles"