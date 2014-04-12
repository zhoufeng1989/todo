from django.conf.urls import patterns, url
from todo.views import RegisterView, RegisterSuccView, LoginView


urlpatterns = patterns(
    '',
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^register_succ/$', RegisterSuccView.as_view(), name='register_succ'),
    url(r'^login/$', LoginView.as_view(), name='login')
)
