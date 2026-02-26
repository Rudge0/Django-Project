from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import AuthorCreationForm, BookForm
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


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-formats-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-formats-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    success_url = reverse_lazy("catalog:literary-formats-list")
    template_name = "catalog/literary_format_confirm_delete.html"


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    queryset = Author.objects.prefetch_related("books")


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    queryset = Author.objects.all().prefetch_related("books")
