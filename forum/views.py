from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Forum, Comment
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted!'
            )

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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Forum.objects.order_by("-created_on")
        forum = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.forum = forum
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('forum_detail', args=[slug]))