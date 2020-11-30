from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.comments, name='comments'),
    path('comment/', views.comments_all, name='comment'),
    path('comment/<int:pk>', views.comment, name='comment')
]
