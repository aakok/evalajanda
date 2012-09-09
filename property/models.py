from django.db import models


class PropertyType(models.Model):
    type = models.CharField(max_length=256)

    def __unicode__(self):
        return self.type


class Property(models.Model):
    user = models.ForeignKey(
        'auth.User', related_name="createdproperty_set")
    type = models.ForeignKey('property.PropertyType')
    price = models.FloatField()
    gross_area = models.PositiveIntegerField()
    net_area = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField()
    rooms = models.PositiveIntegerField()
    saloons = models.PositiveIntegerField()
    floors_in_building = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    auto_park = models.BooleanField()

    vendor_name = models.CharField(max_length=256)
    vendor_phone = models.CharField(max_length=32)

    contributors = models.ManyToManyField(
        'auth.User', related_name='contributionproperty_set')


class PropertyComment(models.Model):
    user = models.ForeignKey('auth.user')
    property = models.ForeignKey('property.Property')
    comment = models.TextField()
