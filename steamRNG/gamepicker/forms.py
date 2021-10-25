from django import forms


class SteamIdForm(forms.Form):
    text = forms.CharField(
        label='Enter your steam id here', widget=forms.Textarea)
