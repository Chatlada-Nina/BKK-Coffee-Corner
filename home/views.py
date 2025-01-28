from django.shortcuts import render
from django.views import generic 
from .models import Post

# Create your views here.
# Create a homepage with generic views credited by I think threfore I blog: CL project"
class PostList(generic.ListView):
    queryset = Post.objects.order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 6