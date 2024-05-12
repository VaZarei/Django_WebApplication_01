from django.urls import path
from . views import ArticleListView, ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name = "ArticleListView_url"),
    path('<int:pk>/', ArticleDetailView.as_view(), name = "ArticleDetailView_url"  )
]
