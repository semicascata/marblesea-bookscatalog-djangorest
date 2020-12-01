from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='MarbleSea - Books Catalog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('marblesea.apps.books.urls')),
    path('comments/', include('marblesea.apps.comments.urls')),
    path('auth/', include('marblesea.apps.auth.urls')),
    path('docs/', schema_view),
]
