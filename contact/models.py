from django.db import models

# Create your models here.


class Contact(models.Model):
    """
    Store a single contact request message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact from {self.name}"
