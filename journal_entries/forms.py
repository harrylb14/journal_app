from django import forms


class ResourceForm(forms.Form):
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
        label='Add Language'
    )
    framework = forms.ModelChoiceField(
        label='Add Framework'
    )
