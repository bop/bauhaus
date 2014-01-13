from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sysadmin.views.home', name='home'),
    # url(r'^sysadmin/', include('sysadmin.foo.urls')),
                       url(r'^$', include('sysadmin.foundation.urls')),
                       url(r'^index.html/$', include('sysadmin.foundation.urls')),
                       url(r'^blog/', include('sysadmin.blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += patterns('django.contrib.flatpages.views',
                        (r'^(?P<url>.*/)$', 'flatpage'),
                        )
