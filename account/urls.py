from django.conf.urls import url
from .views import SignUpFormView

urlpatterns = [
    url(r'^sign_up/$', SignUpFormView.as_view(), name='sign_up'),
]