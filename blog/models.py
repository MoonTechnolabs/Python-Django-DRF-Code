from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Unique title field
    description = models.TextField()  # Description field
    author = models.ForeignKey(User, related_name='blogs',
                               on_delete=models.CASCADE)  # One-to-many relationship with User

    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the created date
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the updated date

    def __str__(self):
        return self.title
