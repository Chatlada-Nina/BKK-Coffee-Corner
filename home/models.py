from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image

# A draft is defined as zero and published as one. (From the I think therefore I blog CL project)
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Create Post Cafes model
class Post(models.Model):
    cafename = models.CharField(max_length=100, unique=True)
    cafeinfo = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cafe_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    address = models.TextField()
    phone = models.TextField()
    opentime = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

# Add a Meta class to define order of contents
    class Meta:
        ordering = ["-created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"{self.cafename} | written by {self.author}"


# Create Review model
class Review(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    created_on = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    body = models.TextField()
    image = models.ImageField(blank=True)


    # Add a Meta class to define order of reviews
    class Meta:
        ordering = ["created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"Review: {self.body} | by {self.author}"
