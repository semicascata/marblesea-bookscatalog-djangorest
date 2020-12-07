from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('edituser/<int:pk>', views.edit_user_admin, name='user'),
    path('<int:pk>', views.edit_user, name='edit_user'),
]
