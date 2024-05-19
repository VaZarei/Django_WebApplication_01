from django.contrib import admin
from .models import ArticleModel, ArticleCommentsModel

# Register your models here.


# admin.site.register(ArticleModel)

class CommnetInLineAdmin(admin.StackedInline):
    model = ArticleCommentsModel
    extra = 0



#@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["Title", "Author","Created", "Edited", "Status"]
    list_filter  = ["Status"]
    search_fields= ["Title", "Author__username"]
    inlines = [CommnetInLineAdmin]
    
    
    readonly_fields = ("Created", "Edited")

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

admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(ArticleCommentsModel)



    