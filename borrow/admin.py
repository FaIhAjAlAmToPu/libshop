from django.contrib import admin
from .models import Borrow, BorrowRequest

admin.site.register(Borrow)
admin.site.register(BorrowRequest)