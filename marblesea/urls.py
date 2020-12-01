from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('marblesea.apps.books.urls')),
    path('comments/', include('marblesea.apps.comments.urls')),
    path('auth/', include('marblesea.apps.auth.urls')),
    path('admin/', admin.site.urls)
]
