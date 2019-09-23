from django.contrib import admin
from .models import Genre, Subject, Book

# Register your models here.


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Genre, GenreAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subject, SubjectAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','description', 'price', 'publisher', 'datePosted', 'rating', 'quality', 'image']
    list_editable =['price', 'quality', 'description', 'image']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)