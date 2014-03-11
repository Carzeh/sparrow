from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns

from django.conf import settings
from menuapp.models import Food, Drink
from menuapp import urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Patterns for Django-CMS Admin Panel and CMS, and also custom patterns for general website navigation for menuapp 
urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('menuapp.urls')),
    url(r'^', include('cms.urls')),
)




if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
