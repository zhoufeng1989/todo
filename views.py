from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from todo.forms import RegisterForm


class RegisterView(FormView):
    template_name = 'todo/register.html'
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('register_succ'))
        return render(request, self.template_name, {'form': form})


class RegisterSuccView(View):
    template_name = 'todo/register_succ.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(FormView):
    pass
