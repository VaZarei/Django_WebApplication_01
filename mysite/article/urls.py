from django.urls import path
from . views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('', ArticleListView.as_view(), name = "ArticleListView_url"),
    path('<slug:slug>/', ArticleDetailView.as_view(), name = "ArticleDetailView_url"),
    path('<slug:slug>/updateview/', ArticleUpdateView.as_view(), name = "ArticleUpdateView_url"),
    path('<slug:slug>/deleteview/', ArticleDeleteView.as_view(), name = "ArticleDeleteView_url"),


]
