from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('books/', include('marblesea.apps.books.urls')),
    path('comments/', include('marblesea.apps.comments.urls')),
    path('admin/', admin.site.urls)
]
