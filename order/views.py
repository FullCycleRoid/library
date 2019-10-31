from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from catalog.models import BookInstance
from django.views.generic.detail import SingleObjectMixin


class OrderBookView(LoginRequiredMixin, ListView):
    model =  BookInstance
    template_name = 'order/your_books.html'
    context_object_name = 'order'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by("return_date")

