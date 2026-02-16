from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView
from library.asgi import application

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("authors/", AuthorListView.as_view(), name="author-list"),

]

app_name = "catalog"