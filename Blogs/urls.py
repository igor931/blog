from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.comment_add, name='comment_add'),
    url(r'^about$', views.about, name='about'),
   # url(r'^contact$', views.contact, name='contact'),

]