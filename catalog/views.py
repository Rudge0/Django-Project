from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Book, Author, LiteraryFormat


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.prefetch_related("books")

def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    book = Book.objects.select_related("format").prefetch_related("author").get(id=pk)
    context = {
        "book": book,
    }
    return render(request=request, context=context, template_name="catalog/book_detail.html")
