from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)