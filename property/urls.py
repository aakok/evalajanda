from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^add/$', 'property.views.add_update_property',
        name='add-property'),
    url(r'^view/(?P<property_id>\d+)/$',
        'property.views.view_property',
        name='view-property'),
    url(r'^update/(?P<property_id>\d+)/$',
        'property.views.add_update_property',
        name='update-property'),
    url(r'^add/comment/(?P<property_id>\d+)/$',
        'property.views.add_comment',
        name='add-comment'),
    url(r'^calculate/compound/interest/$',
        'property.views.calculate_compound_interest',
        name='calculate-compound-interest'),
)
