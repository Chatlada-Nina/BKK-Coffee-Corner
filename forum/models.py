from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    """
    Store a single forum entry related to : model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)

# Add a Meta class to define order of contents
    class Meta:
        ordering = ["-created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    

# Create Comment model
class Comment(models.Model):
    """
    Store a single comment entry related to : model:`auth.User`and :model:`forum.Forum`.
    """
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    created_on = models.DateField(auto_now_add=True)
    body = models.TextField()


    # Add a Meta class to define order of reviews
    class Meta:
        ordering = ["created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"Comment: {self.body} | by {self.author}"