from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import home, addEvent
from iceberg import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^addevent/$', addEvent, name='addevent'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )