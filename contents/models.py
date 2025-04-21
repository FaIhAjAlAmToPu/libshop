from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

class Content(PolymorphicModel):
    title = models.CharField(max_length=60)
    posted_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(Content):
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200, blank=True)
    year_published = models.CharField(max_length=20, blank=True, null=True)
    cover_image = models.URLField(blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    publishers = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=10, blank=True)  # 'eng', 'spa', etc.
    physical_format = models.CharField(max_length=50, blank=True)


class Story(Content):
    author = models.ManyToManyField(User)


