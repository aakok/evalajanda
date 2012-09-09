from django.db import models

class Profile(models.Model):
    user = models.ForeignKey('auth.User')
    birth_data = models.DateField()
