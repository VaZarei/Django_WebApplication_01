from django.db import models
from django.utils.text import slugify


# Create your models here.


class ArticleModel(models.Model):

    STATUS_OF_ARTICLE = (
        ("checking" , "Checking"),
        ("rejected" , "Rejected"),
        ("published" , "Published"),
    )

    Title = models.CharField(max_length=150)
    Body  = models.TextField(max_length=10000)
    Author= models.ForeignKey("auth.user", on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    Edited = models.DateTimeField(auto_now=True) 
    Status = models.CharField(max_length=15, choices=STATUS_OF_ARTICLE, default="checking")
    

    def __str__(self) -> str:
        return self.Title
    

    class Meta:
        ordering = ("-Created",)

 

        
    


    