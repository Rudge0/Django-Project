from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Book, Author, LiteraryFormat


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 10

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    queryset = Author.objects.prefetch_related("books")


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


@login_required
def test_session_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        "<h1>Test session</h1>"
    )