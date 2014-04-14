from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from datetime import datetime
from todo.forms import RegisterForm, LoginForm, ItemForm
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


class ItemView(FormView):
    form_class = ItemForm
    template_name = 'todo/create.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        item = form.save(commit=False)
        item.update_time = datetime.now()
        if form.cleaned_data.get('new'):
            item.create_time = datetime.now()
            item.user_id = self.request.user.id
        item.save()
        return super(ItemView, self).form_valid(form)


class ItemCreateView(ItemView, CreateView):
    def form_valid(self, form):
        form.cleaned_data['new'] = True
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(ItemView, UpdateView):
    pass


class ItemDetailView(DetailView):
    model = Item
    template_name = 'todo/item.html'
