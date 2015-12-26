from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^create/$', views.create_user, name='create_user'),
)
