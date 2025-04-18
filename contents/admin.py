from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import Book, Story, Content, Author

class BookAdmin(PolymorphicChildModelAdmin):
    base_model = Book
    list_display = ('title', 'author')
    list_filter = ('genre',)
    search_fields = ('title', 'author')

class StoryAdmin(PolymorphicChildModelAdmin):
    base_model = Story
    list_display = ('title', 'posted_at')  # or any other relevant field
    search_fields = ('title',)

class ContentParentAdmin(PolymorphicParentModelAdmin):
    base_model = Content
    child_models = (Book, Story)

admin.site.register(Book, BookAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Content, ContentParentAdmin)

admin.site.register(Author)
