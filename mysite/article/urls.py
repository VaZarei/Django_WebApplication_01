from django.urls import path
from . views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView


urlpatterns = [
    path('', ArticleListView.as_view(), name = "ArticleListView_url"),
    path('newarticle/', ArticleCreateView.as_view(), name = "ArticleCreateView_url"),
    path('<int:pk>/', ArticleDetailView.as_view(), name = "ArticleDetailView_url"),
    path('<int:pk>/updateview/', ArticleUpdateView.as_view(), name = "ArticleUpdateView_url"),
    path('<int:pk>/deleteview/', ArticleDeleteView.as_view(), name = "ArticleDeleteView_url"),


]
