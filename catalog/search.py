from django.db.models import Q
from .models import Book, Author



# def search_through(request):
#         query = request.GET.get('user_input')
#
#         book_data = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query)
#                                         | Q(genre__name__icontains=query) | Q(author__name__icontains=query)
#                                         | Q(language__name__icontains=query))
#         return {'search_result': book_data}