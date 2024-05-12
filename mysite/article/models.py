from django.db import models
from django.utils.text import slugify


# Create your models here.


class ArticleModel(models.Model):

    Title = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.Title
    


    Body  = models.TextField(max_length=10000)
    Author= models.ForeignKey("auth.user", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)


    edited = models.DateTimeField(auto_now=True) 

    STATUS_OF_ARTICLE = (
        ("checking" , "Checking"),
        ("rejected" , "Rejected"),
        ("published" , "Published"),
    )
    status = models.CharField(max_length=15, choices=STATUS_OF_ARTICLE, default="checking")
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super().save(*args, **kwargs)

    


    