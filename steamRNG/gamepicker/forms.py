from django import forms
from .models import GameRng


class SteamIdForm(forms.ModelForm):

    class Meta:
        model = GameRng
        fields = ['id_game']
        labels = {'id_game': 'Insert Steam Id'}


class SharedSteamGames(forms.Form):
    model = GameRng
    id_1 = forms.CharField(label='Insert your Steam Id', max_length=100)
    id_2 = forms.CharField(
        label='Insert your friend\'s steam id', max_length=100)
