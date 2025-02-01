from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    """
    Allow user contact requests.
    **Context**
    ``contact_form``
        An instance of :form: `contact.ContactForm`.
    **Template:**
    :template:`contact/contactus.html`
    """
    contact_form = ContactForm()

    return render(
        request,
        "contact/contactus.html",
        {"contact_form": contact_form},
    )