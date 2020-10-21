from django.urls import path
from os.path import join, dirname, abspath
from . import views


app_name = "library"

urlpatterns = [
    path(
        'books/',
        views.books,
        name="books"
    ),
    path(
        'books/<int:isbn>/',
        views.book_page,
        name="book_page"
    ),
    path(
        'books/add_vote/<str:vote>/',
        views.add_vote,
        name="add_vote"
    ),
    path(
        'books/<int:isbn>/add_comment/',
        views.add_comment,
        name="add_comment"
    ),
    path(
        'ph/',
        views.ph,
        name="ph"
    )
]
