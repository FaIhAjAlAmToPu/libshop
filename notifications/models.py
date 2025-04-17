from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.gis.db import models as gis_models
from contents.models import Book, Author
from libraries.models import Store



# Create your models here.
class Wishlist(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} wishes for {self.comments}'

class BookWishlist(Wishlist):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

class StoryWishlist(Wishlist):
    plot = models.TextField()

class WishBookByAuthor(Wishlist):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30)

class WishStoryByAuthor(Wishlist):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class StoreWishlist(Wishlist):
    location = gis_models.PointField()