from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Forum
from .forms import CommentForm

# Create your views here.
class ForumList(generic.ListView):
    queryset = Forum.objects.all()
    template_name = "forum_list.html"


def forum_detail(request, slug):
    """
    Display an individual :model:`forum.Forum`.

    **Context**

    ``forum``
        An instance of :model:`forum.Forum`.

    **Template:**

    :template:`forum/forum_detail.html`
    """

    queryset = Forum.objects.order_by("created_on")
    forum = get_object_or_404(queryset, slug=slug)
    comments = forum.comments.all().order_by("-created_on")
    comment_count = forum.comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.forum = forum
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "forum/forum_detail.html",
        {
            "forum": forum,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
