from django import forms
from django_select2.forms import Select2MultipleWidget

from .models import Resource, Language, Framework


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields=['title', 'description', 'link', 'language', 'framework']

    title = forms.CharField(
        label='Title',
        max_length=50
    )

    description = forms.CharField(
        label='Description',
        max_length=200
    )

    link = forms.URLField()

    language = forms.ModelMultipleChoiceField(
        label='Add Language',
        queryset=Language.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                'style': 'float: center; width: 370px',
                'data-maximum-selection-length': 10
            },
        )
    )

    framework = forms.ModelMultipleChoiceField(
        label='Add Framework/Technology',
        queryset=Framework.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                'style': 'float: center; width: 370px',
                'data-maximum-selection-length': 10
            },
        )
    )


