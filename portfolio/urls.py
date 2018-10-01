from django.conf.urls import url

from .views import get_portfolio, get_project

urlpatterns = [
    url(r'^portfolio/$', get_portfolio),
    url(r'^portfolio/(?P<slug>[-\w]+)/$', get_project)
]