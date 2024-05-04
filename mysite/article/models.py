from django.db import models


# Create your models here.


class ArticleModel(models.Model):
    Title = models.CharField(max_length=150)
    Body  = models.TextField(max_length=10000)
    Author= models.ForeignKey("auth.user", on_delete=models.CASCADE)
    Date  = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.Title