from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    # url(r'^$',  views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    # url(r'^new/$', views.new_room, name='new_room'),
    # url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    url(r'^temperature/$', views.temperature, name='temperature'),

]
