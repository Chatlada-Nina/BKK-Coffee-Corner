from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    content = models.TextField()
    created_on = models.DateField()

# Add a Meta class to define order of contents
    class Meta:
        ordering = ["-created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"{self.title} | written by {self.author}"