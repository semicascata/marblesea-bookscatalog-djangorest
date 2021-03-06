from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Marble Sea - Books Catalog',
        default_version='v1',
        description='Books Catalog',
        # terms_of_service='',
        contact=openapi.Contact(email='admin@gmail.com'),
        # license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    # urls
    path('admin/', admin.site.urls),
    path('books/', include('marblesea.apps.books.urls')),
    path('comments/', include('marblesea.apps.comments.urls')),
    path('auth/', include('marblesea.apps.auth.urls')),
    path('lists/', include('marblesea.apps.lists.urls')),
    path('users/', include('marblesea.apps.users.urls')),

    # doc - swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
]
