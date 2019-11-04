from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from catalog.forms import BookReserveForm
from .models import Book, Author, BookInstance, Genre


# Create your views here.
class BookListView(ListView):
    template_name = 'catalog/book_list.html'
    model = Book

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        context['visits'] = self.request.session['num_visits']
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    form_class = BookReserveForm

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['book_instance'] = BookInstance.objects.filter(book__slug=self.kwargs['slug'], status='m')
        return context



def book_reserve(request):

    current_book = request.POST.get('book_id')
    book = Book.objects.get(id=current_book)
    slug = book.slug
    book_instance = BookInstance.objects.filter(book=book, status='m').first()
    book_instance.status = 'r'
    book_instance.borrower = request.user
    book_instance.save()
    return redirect("catalog:book_detail", slug=slug)

class AuthorListView(ListView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

class GenreListView(ListView):
    model = Genre
    template_name = 'catalog/genre_list.html'
    context_object_name = 'genre'

class GenreFilterView(ListView):
    template_name = 'catalog/genre_filter.html'
    model = Book
    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.kwargs['slug'])
        context = super(GenreFilterView, self).get_context_data(**kwargs)
        context['book_data'] = Book.objects.filter(genre__slug=self.kwargs['slug'])
        return context


class SearchView(ListView):
    template_name = 'catalog/search_result.html'
    model = Book

    def get_queryset(self):
        query = self.request.GET.get('user_input')
        book_data = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query)
                                        | Q(genre__name__icontains=query) | Q(author__name__icontains=query)
                                        | Q(language__name__icontains=query))

        return book_data


