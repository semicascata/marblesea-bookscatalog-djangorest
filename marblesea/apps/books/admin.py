from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'author', 'active')
  list_display_links = ('id', 'title')
  list_editable = ('active',)
  search_fields = ('title', 'author')
  list_per_page = 20

admin.site.register(Book, BookAdmin)
