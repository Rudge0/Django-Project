from django.urls import path

from catalog.views import (
    index,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,

    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,

    LiteraryFormatListView,
    LiteraryFormatCreateView,
    LiteraryFormatUpdateView,
    LiteraryFormatDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("literary-formats/create", LiteraryFormatCreateView.as_view(), name="literary-formats-create"),
    path("literary-formats/<int:pk>update/", LiteraryFormatUpdateView.as_view(), name="literary-formats-update"),
    path("literary-formats/<int:pk>delete/", LiteraryFormatDeleteView.as_view(), name="literary-formats-delete"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),

    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create", AuthorCreateView.as_view(), name='author-create'),

]

app_name = "catalog"
