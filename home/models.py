from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image

# A draft is defined as zero and published as one. (From the I think therefore I blog CL project)
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Create Post Cafes model
class Post(models.Model):
    """
    Store a single post entry related to : model:`auth.User`.
    """
    cafename = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    cafeinfo = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cafe_posts")
    featured_image_1 = CloudinaryField('image', default='placeholder')
    featured_image_2 = CloudinaryField('image', default='placeholder')
    featured_image_3 = CloudinaryField('image', default='placeholder')
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
    """
    Store a single review entry related to : model:`auth.User` and :model:`home.Post`.
    """
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    created_on = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    body = models.TextField()
    image = models.ImageField(blank=True)


    # Add a Meta class to define order of reviews
    class Meta:
        ordering = ["created_on"]

# Display class object as a string to improve readable for admin
    def __str__(self):
        return f"Review: {self.body} | by {self.author}"
