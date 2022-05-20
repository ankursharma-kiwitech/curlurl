from django import forms


# creating a form
class url(forms.Form):
    url_field = forms.URLField()
