from django.urls import path

from catalog.views import (index,
                           LiteraryFormatListView,
                           BookListView,
                           AuthorListView,
                           BookDetailView,
                           test_session_view,
                           AuthorCreateView,
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
    path("test-session/", test_session_view, name="session-view"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/create", AuthorCreateView.as_view(), name='author-create-view'),

]

app_name = "catalog"