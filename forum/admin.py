from django.contrib import admin
from .models import Forum, Comment
from django_summernote.admin import SummernoteModelAdmin

# Give the admin panel greater functionality and clarity.
@admin.register(Forum)
class ForumAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created_on')
    search_fields = ['title']
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)