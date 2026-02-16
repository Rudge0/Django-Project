from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView, book_detail_view

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),

]

app_name = "catalog"