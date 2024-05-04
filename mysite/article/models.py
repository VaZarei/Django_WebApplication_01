from django.db import models


# Create your models here.


class ArticleModel(models.Model):
    Title = models.CharField()
    Body  = models.TextField()
    Auther= models.ForeignKey("auth.user", on_delete=models.CASCADE)
    Date  = models.DateTimeField(auto_now=True, auto_now_add=True)


    def __str__(self) -> str:
        return self.Title