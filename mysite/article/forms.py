from django import forms
from .models import ArticleCommentsModel



class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleCommentsModel
        fields = ("writer", "comment", "article") 
        widgets = {
            "article": forms.HiddenInput(),
            "writer":  forms.HiddenInput(),

        }
       
