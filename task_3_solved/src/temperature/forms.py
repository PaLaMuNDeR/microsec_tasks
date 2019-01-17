from django import forms


class UpdateValueForm(forms.Form):
    value = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )