from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Review


# Add @admin.register() decorator 
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ("cafename", "slug", "status", "created_on")
    search_fields = ["cafename"]
    list_filter = ("status", "created_on",)
    prepopulated_fields = {"slug": ("cafename",)}
    summernote_fields = ("cafeinfo",)

# Register your models here.
admin.site.register(Review)
