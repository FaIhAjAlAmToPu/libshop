from django.db import models
from django.contrib.auth.models import User
from library_shop.contents.models import Book
from datetime import timedelta

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.user.username} bought {self.book.title}"

class OrderRequest(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('halted', 'Halted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ordered')
    purchase_deadline = models.DateTimeField()
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if not self.purchase_deadline:
            self.purchase_deadline = self.ordered_at + timedelta(days=7)  # Should borrow the book before Default 2-day
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} requested {self.book.title} ({self.status})"