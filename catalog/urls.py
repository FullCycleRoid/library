from django.conf.urls import url
from . import views

app_name = 'catalog'

urlpatterns = [
    url(r'^book_reserve/$', views.book_reserve, name='book_reserve'),
    url(r'^author/$', views.AuthorListView.as_view(), name='author_list'),
    url(r'^search_result/$', views.SearchView.as_view(), name='search'),
    url(r'^genre/$', views.GenreListView.as_view(), name='genre_list'),
    url(r'^genre_filter_result/(?P<slug>[-\w]+)/$', views.GenreFilterView.as_view(), name='genre_filter'),
    url(r'^$', views.BookListView.as_view(), name='book_list'),
    url(r'^author/(?P<slug>[-\w]+)/$', views.AuthorDetailView.as_view(), name='author_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.BookDetailView.as_view(), name='book_detail'),

]
