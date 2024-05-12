from django.contrib import admin
from .models import ArticleModel 

# Register your models here.


# admin.site.register(ArticleModel)


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["Title", "Author","Created", "Edited", "Status"]
    list_filter  = ["Status"]
    search_fields= ["Title", "Author__username"]
    
    
    readonly_fields = ("Created", "Edited", "slug")

    fieldsets = (

        (None,{
            "fields" : ("Title", "Author", )
        }),
        ("Important Dates",{
            "fields" : ("Created", "Edited",)
        }),
        ("Content",{
            "fields" : ("Body", "Status")
        })
    
    )





    