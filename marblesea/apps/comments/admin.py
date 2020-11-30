from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
  list_display = ('id', 'book', 'active')
  list_display_links = ('id', 'book')
  list_editable = ('active',)
  search_fields = ('text',)
  list_per_page = 20

admin.site.register(Comment, CommentAdmin)