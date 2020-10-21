from django.urls import path
from os.path import join, dirname, abspath

from . import views


app_name = "library"
urlpatterns = [
    path('', views.books, name="base"),
    path('<int:isbn>/', views.book_page, name="book_page"),
    path('<int:isbn>/add_comment/', views.add_comment, name="add_comment"),
    path('add_vote/<str:vote>', views.add_vote, name="add_vote")
]
