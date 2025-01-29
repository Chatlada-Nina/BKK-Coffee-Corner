from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import ReviewForm

# Create your views here.
# Create a homepage with generic views credited by I think threfore I blog: CL project"
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

    return render(request,
        "home/post_detail.html",
        {
            "post": post,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )