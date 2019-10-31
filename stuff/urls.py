from django.conf.urls import url
from . import views

app_name = 'stuff'

urlpatterns = [
    url(r'^author/create/$', views.AuthorCreateView.as_view(), name='author_create'),
    url(r'^book/create/$', views.BookCreateView.as_view(), name='book_create'),
    url(r'^author/(?P<slug>[-\w]+)/update/$', views.AuthorUpdateView.as_view(), name='author_update'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdateView.as_view(), name='book_update'),
    url(r'^author/(?P<slug>[-\w]+)/delete/$', views.AuthorDeleteView.as_view(), name='author_delete'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDeleteView.as_view(), name='book_delete'),
]