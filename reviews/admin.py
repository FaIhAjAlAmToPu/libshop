from django.contrib import admin
from .models import ContentReaction, ContentReview
# Register your models here.

@admin.register(ContentReaction)
class ContentReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'reaction_type')
    search_fields = ('user__username', 'content__title')


@admin.register(ContentReview)
class ContentReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'rating', 'created_at')
    search_fields = ('user__username', 'content__title')