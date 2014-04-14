from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from todo import views


urlpatterns = patterns(
    '',
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^list/$',
        login_required(
            views.TodoListView.as_view(), login_url=reverse_lazy('login')
        ),
        name='list'),
    url(r'^item/create/$',
        login_required(
            views.ItemCreateView.as_view(), login_url=reverse_lazy('login')
        ),
        name='create'),
    url(r'^item/(?P<pk>\d+)/$',
        login_required(
            views.ItemDetailView.as_view(), login_url=reverse_lazy('login')
        ),
        name='detail')
)
