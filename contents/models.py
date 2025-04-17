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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(Content):
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30, blank=True)
    published_date = models.DateField()
    cover_image = models.URLField(blank=True)


class Story(Content):
    author = models.ManyToManyField(User)


