from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^add/$', 'property.views.add_update_property',
        name='add-property'),
    url(r'^update/(?P<property_id>\d+)/$',
        'property.views.add_update_property',
        name='update-property'),
)
