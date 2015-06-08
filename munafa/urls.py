from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'zope.views.home', name='home'),
                       # url(r'^register/$', 'zope.views.register', name='register'),
                       # url(r'^login/$', 'zope.views.login', name='login'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^accounts/', include('registration.backends.simple.urls')),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       )
