from django.conf.urls import url
from django.contrib.auth.views import login, logout
from simplemooc.accounts.views import register, dashboard


urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
]
