from .models import Review
from django import forms

# Create ReviewForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("body", "rating",)