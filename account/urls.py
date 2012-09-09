from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',
        name='login', kwargs={'template_name': 'account/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout'),
)
