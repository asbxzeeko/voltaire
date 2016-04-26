from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post, name="post"),
    url(r'^tag/(?P<tag>\w+)/$', views.tag, name="tag"),
    url(r'^about/$', views.about, name="about"),
    url(r'^search/$', views.search_page, name='search_page'),
    url(r'^search/results/$', views.search, name='search'),
    # pagination
    url(r'^page/(?P<page>[0-9]+)/$', views.index, name="index_pages"),
    url(r'^tag/(?P<tag>\w+)/page/(?P<page>[0-9]+)/$', views.tag, name="tag_pages"),
]