from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
]