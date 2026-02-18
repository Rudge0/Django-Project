from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView, BookDetailView, test_session_view

urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-formats-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("test-session/", test_session_view, name="session-view"),
    path("authors/", AuthorListView.as_view(), name="author-list"),

]

app_name = "catalog"