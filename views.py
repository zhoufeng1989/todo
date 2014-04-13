from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from todo.forms import RegisterForm, LoginForm
from todo.models import User, Item


class RegisterView(FormView):
    template_name = 'todo/register.html'
    success_url = 'login'
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'todo/login.html'
    success_url = reverse_lazy('list')
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['email'],
                            password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            render(self.request, self.template_name, {'form': form})


class TodoListView(ListView):
    template_name = 'todo/list.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.request.user.id)
        return Item.objects.filter(user=self.user)
