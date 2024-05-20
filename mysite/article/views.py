from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ArticleModel
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from article.forms import ArticleCommentForm

# Create your views here.




class ArticleListView(ListView):
    model = ArticleModel
    template_name = "article/ArticleListView.html"
    context_object_name  = "articles"

    def get_queryset(self):
        return ArticleModel.objects.filter(Status='published')
    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticleModel
    fields = ["Title", "Body", "Status"]
    template_name = "article/ArticleCreateView.html"
    success_url = reverse_lazy("ArticleListView_url")
    
    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    

class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = "article/ArticleDetailView.html"
    context_object_name  = "articles"
    form_class = ArticleCommentForm
    

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['form'] = ArticleCommentForm(initial={"article":self.object, "writer":self.request.user})
        return context
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(self.request.POST)
        
        if form.is_valid():
                form.save()
                return redirect(self.get_success_url())
        else:
                return self.render_to_response(self.get_context_data(form=form))
            
    def get_success_url(self):
        return reverse("ArticleDetailView_url", kwargs={"pk": self.object.id})


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ArticleModel
    fields = ["Title", "Body"]
    template_name = "article/ArticleUpdateView.html"
    success_url = reverse_lazy("ArticleListView_url")

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.Author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ArticleModel
    template_name = "article/ArticleDeleteView.html"
    success_url = reverse_lazy("ArticleListView_url")
    context_object_name = "articles"


    def test_func(self):
        article = self.get_object()
        return self.request.user == article.Author
    
    

    