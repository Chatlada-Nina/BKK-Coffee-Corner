from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Review
from .forms import ReviewForm

# Create your views here.
# Create a homepage with generic views
# credited by I think threfore I blog: CL project


class PostList(generic.ListView):
    queryset = Post.objects.order_by("-created_on")
    template_name = "home/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`home.Post`.

    **Context**
    ``post``
        An instance of :model:`home.Post`.
    ``reviews``
        All reviews related to the post.
    ``review_count``
        A count of reviews related to the post.
    ``review_form``
        An instance of :form:`home.ReviewForm`.
    **Template:**
    :template:`home/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    reviews = post.reviews.all().order_by("-created_on")
    review_count = post.reviews.count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.post = post
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Review submitted! Thank you for sharing."
            )

    review_form = ReviewForm()

    return render(request, "home/post_detail.html", {
            "post": post,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    Display an individual review for edit.

    **Context**
    ``post``
        An instance of :model:`home.Post`.
    ``review``
        A single review related to the post.
    ``review_form``
        An instance of :form:`home.ReviewForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.order_by("-created_on")
        post = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.post = post
            review.save()
            messages.add_message(request, messages.SUCCESS, "Review Updated!")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating review!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def review_delete(request, slug, review_id):
    """
    Delete an individual review.

    **Context**
    ``post``
        An instance of :model:`home.Post`.
    ``review``
        A single review related to the post.
    """
    queryset = Post.objects.order_by("-created_on")
    post = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
