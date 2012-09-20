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


class CompoundInterestForm(forms.Form):
    price = forms.FloatField()
    months = forms.IntegerField()
    monthly_interest = forms.FloatField()
