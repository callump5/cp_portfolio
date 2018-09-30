from django.conf.urls import url

from .views import get_about, get_contact

urlpatterns = [
    url(r'^about/$', get_about),
    url(r'^contact-details/$', get_contact)
]