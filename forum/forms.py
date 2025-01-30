from .models import Comment
from django import forms


# Create CommentForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)