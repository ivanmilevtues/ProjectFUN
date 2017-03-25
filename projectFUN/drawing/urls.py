from django.conf.urls import url

from drawing.views import enter_username

urlpatterns = [
    url(r'^drawing/', enter_username),
] + STATIC_ROOT
