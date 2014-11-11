from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^admin/', include(admin.site.urls)),
)
