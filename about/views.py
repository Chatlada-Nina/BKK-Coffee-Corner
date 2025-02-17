from django.shortcuts import render
from .models import About

# Create your views here.
def about_us(request):
    """
    Render the most recent information on the website
    Display an individual instance of :model: `about.About`.
    **Context**
    ``about``
        The most recent instance of :model: `about.About`.
    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )