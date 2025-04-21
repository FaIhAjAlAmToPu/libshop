from django.contrib.gis.db import models
from contents.models import Content


class Store(models.Model):
    STORE_TYPE_CHOICES = [
        ('library', 'Library'),
        ('bookshop', 'Bookshop'),
        ('both', 'You can buy or borrow'),
    ]

    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100, null=True, blank=True)
    store_type = models.CharField(
        max_length=10,
        choices=STORE_TYPE_CHOICES,
        default='both'
    )
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    contents = models.ManyToManyField(Content, through='StoreContent', blank=True)


class StoreContent(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
