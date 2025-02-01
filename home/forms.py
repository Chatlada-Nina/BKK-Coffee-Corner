from django import forms
from .models import Review

# Create ReviewForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("body", "rating",)