from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from catalog.models import Author, Book
from django.views.generic.base import View


class AuthorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'stuff/author_form.html'
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = '__all__'


class BookCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'stuff/book_form.html'
    permission_required = 'catalog.can_mark_returned'
    model = Book
    fields = '__all__'


class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'stuff/author_form.html'
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = ['date_of_dead']

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'stuff/book_form.html'
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = '__all__'


class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'stuff/author_delete.html'
    permission_required = 'catalog.can_mark_returned'
    model = Author
    template_name_suffix = '_delete'
    success_url = reverse_lazy('catalog:author_list')


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'stuff/book_delete.html'
    permission_required = 'catalog.can_mark_returned'
    model = Book
    success_url = reverse_lazy('catalog:book_list')


