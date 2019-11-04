from django import forms


class BookReserveForm(forms.Form):
    approve = forms.CheckboxInput()
    text = forms.Textarea()
