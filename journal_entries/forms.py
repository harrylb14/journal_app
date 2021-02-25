from django import forms
from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        exclude = ['pub_date']

    title = forms.CharField(
        label='Title',
        max_length=50
    )

    description = forms.CharField(
        label='Description',
        max_length=200
    )

    link = forms.URLField()

    language = forms.CharField(
        label='Add Language',
        max_length=50
    )

    framework = forms.CharField(
        label='Add Framework',
        max_length=50
    )
