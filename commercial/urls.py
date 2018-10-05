from django.conf.urls import url

from .views import get_commercial

urlpatterns = [
    url(r'^commercial/$', get_commercial, name='home'),
]