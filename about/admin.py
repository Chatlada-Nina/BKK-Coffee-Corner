from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About



# Add @admin.register() decorator 
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Customizes the Django admin interface for the About model.
    """
    summernote_fields = ('content',)


# Register your models here.