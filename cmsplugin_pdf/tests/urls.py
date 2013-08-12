"""Test urls for the ``cmsplugin_pdf`` app."""
from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(
            r'%s(?P<path>.*)' % settings.MEDIA_URL[1:],
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
