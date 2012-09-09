from django import forms

from property.models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('contributors', 'user')
