from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView
from library.asgi import application

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("books/", BookListView.as_view(), name="book-list")

]

app_name = "catalog"