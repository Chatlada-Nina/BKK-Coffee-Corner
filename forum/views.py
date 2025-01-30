from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Forum

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

    return render(
        request,
        "forum/forum_detail.html",
        {"forum": forum},
    )
