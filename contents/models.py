from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)
    available_for_borrow = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Story(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(User)
    posted_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('laugh', 'Laugh'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'story')  # Ensures a user can react to a story only once

    def __str__(self):
        return f"{self.user.username} reacted '{self.reaction_type}' to {self.story.title}"