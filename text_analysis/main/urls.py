from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns(
    '',
    url(r'^parse$', views.parse, name='parse'),
    url(r'^reading$', views.reading, name='reading'),
)
