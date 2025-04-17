from django.contrib import admin
from .models import BookWishlist, StoryWishlist, StoreWishlist, WishBookByAuthor, WishStoryByAuthor
from django.contrib.gis.admin import GISModelAdmin

@admin.register(BookWishlist)
class BookWishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'store', 'comments', 'created_at')
    search_fields = ('user__username', 'book__title', 'store__name')

@admin.register(StoryWishlist)
class StoryWishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'plot', 'comments', 'created_at')
    search_fields = ('user__username', 'story_plot')

@admin.register(WishBookByAuthor)
class BookWishlistByAuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'author', 'genre', 'comments', 'created_at')
    search_fields = ('user__username', 'author__first_name', 'author__last_name', 'genre')

@admin.register(WishStoryByAuthor)
class StoryWishlistByAuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'author', 'comments', 'created_at')
    search_fields = ('user__username', 'author__username')

@admin.register(StoreWishlist)
class StoreWishlistAdmin(GISModelAdmin):
    list_display = ('user', 'location', 'comments', 'created_at')
    search_fields = ('user__username', 'location')
