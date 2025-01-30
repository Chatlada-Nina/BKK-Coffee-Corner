from django.shortcuts import render
from django.views import generic
from .models import Forum

# Create your views here.
class ForumList(generic.ListView):
    queryset = Forum.objects.all()
    template_name = "forum_list.html"
