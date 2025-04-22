from django.db import models
from django.contrib.auth.models import User
from libraries.models import StoreContent
from datetime import timedelta

class Borrow(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),  # Order in progress
        ('returned', 'Returned'),  # Order finished
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storeContent = models.ForeignKey(StoreContent, on_delete=models.CASCADE, null=True)
    borrow_date = models.DateField(auto_now_add=True)
    return_deadline = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def save(self, *args, **kwargs):
        if not self.return_deadline:
            self.return_deadline = self.borrow_date + timedelta(days=14)  # Default 2-week borrow period
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} borrowed {self.storeContent.content.title} from {self.storeContent.store.name}"

class BorrowRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storeContent = models.ForeignKey(StoreContent, on_delete=models.CASCADE, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    borrow_deadline = models.DateTimeField(null=True, blank=True)
    comment = models.TextField()

    # def save(self, *args, **kwargs):
    #     if not self.borrow_deadline:
    #         self.return_deadline = self.requested_at + timedelta(days=2)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} requested {self.storeContent.content.title} from {self.storeContent.store.name} ({self.status})"