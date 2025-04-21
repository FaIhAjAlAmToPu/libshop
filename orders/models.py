from django.db import models
from django.contrib.auth.models import User
from libraries.models import StoreContent
from datetime import timedelta

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storeContent = models.ForeignKey(StoreContent, on_delete=models.CASCADE)
    bought_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.user.username} bought {self.storeContent.content.title} from {self.storeContent.store.name}"

class OrderRequest(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('halted', 'Halted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storeContent = models.ForeignKey(StoreContent, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ordered')
    purchase_deadline = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.purchase_deadline:
            self.purchase_deadline = self.ordered_at + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} requested {self.storeContent.content.title} from {self.storeContent.store.name} ({self.status})"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storeContent = models.ForeignKey(StoreContent, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart: {self.quantity} of {self.storeContent.content.title}"