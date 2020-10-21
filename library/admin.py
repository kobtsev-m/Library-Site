from django.contrib import admin
from library.models import PublishingHouse, Author, Book, Comment, ContentImage

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author',
              'publishing_house', 'price', 'image')

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass

@admin.register(ContentImage)
class ContentImage(admin.ModelAdmin):
    pass