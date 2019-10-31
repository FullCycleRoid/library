from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import FormView
from django.shortcuts import render


# Create your views here.


class SignUpFormView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        if form.is_valid:
            form.save()
            return super(SignUpFormView, self).form_valid(form)


