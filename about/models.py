from django.db import models

# Create your models here.
class About(models.Model):
    """
    Store a single about us text.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    # Display class object as a string to improve readable for admin
    def __str__(self):
        return self.title