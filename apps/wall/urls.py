from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^wall$', views.wall),
    url(r'^logout$', views.logout), 
    url(r'^create_post$', views.create_post),
    url(r'^create_comment/(?P<post_id>\d+)$', views.create_comment),
    url(r'^delete_comment/(?P<comment_id>\d+)$', views.delete_comment),
    url(r'^delete_post/(?P<post_id>\d+)$', views.delete_post),
]
