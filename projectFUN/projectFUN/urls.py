"""projectFUN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin

from drawing.views import play, request_game, count_users, final_room


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('login_form.urls')),
    url(r'^play/', request_game, name='request_game'),
    url(r'^start_playing/', play, name='play'),
    url(r'^ready_for_play/', count_users, name='count_users'),
    url(r'^result_room/', final_room, name='final_room')
]
