from django import forms


class CartAddBookForm(forms.Form):
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)