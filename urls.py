from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from todo.views import RegisterView, LoginView, TodoListView


urlpatterns = patterns(
    '',
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^list/$',
        login_required(
            TodoListView.as_view(),
            login_url=reverse_lazy('login')
        ),
        name='list')
)
