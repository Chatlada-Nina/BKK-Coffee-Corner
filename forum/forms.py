from django import forms
from .models import Comment, Forum


# Create CommentForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


# Create ForumForm that inherit from a built-in Django class.
# Use Meta to tell ModelForm what models and fields we want in our form.
class CreateForum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["title","slug","content",]