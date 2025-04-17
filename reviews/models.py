from django.contrib.auth.models import User
from django.db import models
from contents.models import Content


class ContentReaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('laugh', 'Laugh'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'content')  # Ensures a user can react to a content only once

    def __str__(self):
        return f"{self.user.username} reacted '{self.reaction_type}' to {self.content.title}"


class ContentReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'content')  # One review per content per user

    def __str__(self):
        return f"{self.user.username} reviewed {self.content.title} {self.rating}"
