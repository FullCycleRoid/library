from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    url('^$', views.OrderBookView.as_view(), name='your_books')
]