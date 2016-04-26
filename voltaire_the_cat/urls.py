from django.conf.urls import url, include
from django.contrib import admin
from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(blog_urls)),
]
