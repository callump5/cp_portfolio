from django.conf.urls import url

from .views import get_portfolio, get_project

urlpatterns = [
    url(r'^portfolio/', get_portfolio, name='portfolio'),
    url(r'^(?P<slug>[-\w]+)/$', get_project, name='project')
]