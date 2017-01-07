from django.conf.urls import url
from django.contrib.auth.views import login, logout
from simplemooc.accounts.views import register, dashboard, edit, edit_password, password_reset


urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^nova-senha/$', password_reset, name='password_reset'),
    url(r'^editar/$', edit, name='edit'),
    url(r'^editar-senha/$', edit_password, name='edit_password'),
]
