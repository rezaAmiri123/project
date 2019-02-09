from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'book'
urlpatterns = [
    path('authors/', views.AuthorList.as_view(), name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/detail/<int:id>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('author/update/<int:pk>/', views.author_update, name='author_update'),
    path('author/delete/<int:pk>/', views.author_delete, name='author_delete'),

    path('publishers/', views.PublisherList.as_view(), name='publisher_list'),
    path('publisher/create/', (login_required)(views.PublisherCreate.as_view()), name='publisher_create'),
    path('publisher/update/<int:pk>/', (login_required)(views.PublisherUpdate.as_view()), name='publisher_update'),
    path('publisher/delete/<int:pk>/', (login_required)(views.PublisherDelete.as_view()), name='publisher_delete'),

    path('', views.BookList.as_view(), name='book_list'),
    path('create/', (login_required)(views.BookCreate.as_view()), name='book_create'),
    path('update/<int:pk>/', (login_required)(views.BookUpdate.as_view()), name='book_update'),
    path('delete/<int:pk>/', (login_required)(views.BookDelete.as_view()), name='book_delete'),
]

