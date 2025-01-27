from django.contrib import admin
from .models import Post, Review
from django_summernote.admin import SummernoteModelAdmin

# Add @admin.register() decorator 
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ("cafename", "slug", "status")
    search_fields = ["cafename"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("cafename",)}
    summernote_fields = ("content",)

# Register your models here.
admin.site.register(Review)
