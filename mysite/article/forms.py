from django import forms
from article.models import ArticleCommentsModel


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleCommentsModel
        fields = ["article", "comment", "writer"]
        # widgets = {
        #     "article": forms.HiddenInput(),
        #     "writer" : forms.HiddenInput(),
        # }