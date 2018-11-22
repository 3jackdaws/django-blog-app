from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)

    # I assume this is post content
    description = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)


