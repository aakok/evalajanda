from django import forms

from property.models import Property, PropertyComment


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('contributors', 'user')


class PropertyCommentForm(forms.ModelForm):
    class Meta:
        model = PropertyComment
        exclude = ('user', 'property')
