from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from ataps.apps.mothers_calendar.backends import SMSSyncBackendView
from ataps.apps.mothers_calendar.views import HomeView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       # RapidSMS core URLs
                       (r'^accounts/', include('rapidsms.urls.login_logout')),
                       url(r'^$', HomeView.as_view(), name='rapidsms-dashboard'),
                       # RapidSMS contrib app URLs
                       (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
                       #(r'^locations/', include('rapidsms.contrib.locations.urls')),
                       (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
                       (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
                       (r'^registration/', include('rapidsms.contrib.registration.urls')),
		       url(r'^backends/smssync/$', SMSSyncBackendView.as_view()),

                       # Third party URLs
                       (r'^selectable/', include('selectable.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}),
    )