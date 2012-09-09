from django.contrib import admin
from property.models import PropertyType, Property, PropertyComment


admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(PropertyComment)
