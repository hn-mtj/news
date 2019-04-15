from django.contrib import admin

from .models import Post, Author, Category, Language, File

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(File)

