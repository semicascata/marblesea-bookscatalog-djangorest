from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('<int:pk>', views.edit_user, name='user'),
]
