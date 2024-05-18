from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import ArticleModel
from django.urls import reverse_lazy

# Create your views here.




class ArticleListView(ListView):
    model = ArticleModel
    template_name = "article/ArticleListView.html"
    context_object_name  = "articles"

    def get_queryset(self):
        return ArticleModel.objects.filter(Status='published')
    

class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = "article/ArticleDetailView.html"
    context_object_name  = "articles"


class ArticleUpdateView(UpdateView):
    model = ArticleModel
    fields = ["Title", "Body"]
    template_name = "article/ArticleUpdateView.html"
    context_object_name = "articles"
    success_url = reverse_lazy("ArticleListView_url" )

    