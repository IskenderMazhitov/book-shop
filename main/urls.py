from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', book_list, name='book-list'),
    path('author/<int:pk>/', author_detail, name='author-detail')
]