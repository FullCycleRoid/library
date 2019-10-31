from django.conf.urls import url
from . import views

app_name = 'catalog'


urlpatterns = [
    url(r'^author/$', views.AuthorListView.as_view(), name='author_list'),
    url(r'search_result/$', views.SearchView.as_view(), name='search'),
    url(r'^genres/$', views.GenreListView.as_view(), name='genre_list'),
    url(r'^$', views.BookListView.as_view(), name='book_list'),
    url(r'^author/(?P<slug>[-\w]+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name='book_detail'),
    # url(r'^book_reservation/$', views.BookInstanceView, name='book_instance')


]
