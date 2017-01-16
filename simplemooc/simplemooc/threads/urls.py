from django.conf.urls import url
from simplemooc.threads import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]