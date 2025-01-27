from django.db import models
from django.contrib.auth.models import User

# A draft is defined as zero and published as one. (From the I think therefore I blog CL project)
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Create Post Cafes model
class Post(models.Model):
    cafename = models.CharField(max_length=100, unique=True)
    cafeinfo = models.TextField()
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cafe_posts")
    address = models.TextField()
    phone = models.TextField()
    opentime = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


