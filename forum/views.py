from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Comment
from .forms import CommentForm, CreateForum
from . import forms

# Create your views here.


class ForumList(generic.ListView):
    queryset = Forum.objects.order_by("-created_on")
    template_name = "forum_list.html"


def forum_detail(request, slug):
    """
    Display an individual :model:`forum.Forum`.

    **Context**
    ``forum``
        An instance of :model:`forum.Forum`.
    ``comments``
        All comments related to the forum.
    ``comment_count``
        A count of comments related to the forum.
    ``comment_form``
        An instance of :form:`forum.CommentForm`.

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

# Create Edit for comment


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**
    ``forum``
        An instance of :model:`forum.Forum`.
    ``comment``
        A single comment related to the forum.
    ``comment_form``
        An instance of :form:`forum.CommentForm`.
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
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('forum-detail', args=[slug]))


# Create Delete view for comment


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**
    ``forum``
        An instance of :model:`forum.Forum`.
    ``comment``
        A single comment related to the forum.
    """
    queryset = Forum.objects.order_by("-created_on")
    forum = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('forum-detail', args=[slug]))


# Create new forum views and request the logged-in user
@login_required(login_url="/accounts/login/")
def forum_new(request):
    """
    Allow user to create a new forum.

    **Context**
    ``form``
        An instance of :form: `forum.form`.

    **Template:**
    :template:`forum/forum_new.html`
    """
    if request.method == "POST":
        form = forms.CreateForum(request.POST)
        if form.is_valid():
            newforum = form.save(commit=False)
            newforum.author = request.user
            newforum.save()
            messages.add_message(request, messages.SUCCESS, 'Forum Submitted!')
            return redirect("forum")
    else:
        form = forms.CreateForum()
    form = forms.CreateForum()
    return render(request, "forum/forum_new.html", {"form": form})


# Edit a forum
def forum_edit(request, forum_id):
    """
    Display an individual forum for edit.

    **Context**
    ``forum``
        An instance of :model:`forum.Forum`.
    ``form``
        An instance of :form:`forum.CreateForum`.
    """
    forum = Forum.objects.get(pk=forum_id)
    form = CreateForum(request.POST or None, instance=forum)

    if form.is_valid() and forum.author == request.user:
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Forum Updated!')
        return redirect('forum')

    return render(request, 'forum/forum_edit.html',
                  {'forum': forum,
                   'form': form})


# Delete a forum
def forum_delete(request, forum_id):
    """
    Delete a forum.

    **Context**
    ``forum``
        An instance of :model:`forum.Forum`.
    """
    forum = get_object_or_404(Forum, pk=forum_id)

    if forum.author == request.user:
        forum.delete()
        messages.add_message(request, messages.SUCCESS, 'Forum deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own forums!')
    return HttpResponseRedirect(reverse('forum'))
