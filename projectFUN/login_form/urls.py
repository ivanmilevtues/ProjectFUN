from django.conf.urls import url

from login_form import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile')
]
