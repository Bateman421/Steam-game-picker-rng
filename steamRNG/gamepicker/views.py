import random
from selenium.webdriver.opera.options import Options
from django.shortcuts import render, redirect
from .forms import SharedSteamGames, SteamIdForm
from .models import GameRng
from .scrapper import Scrapper

# Create your views here.


def home(request):
    if request.method == 'POST':
        filled_form = SteamIdForm(request.POST)
        if filled_form.is_valid():
            steam_id = filled_form.cleaned_data['id_game']
            games_list = Scrapper.gameList(steam_id)
            # Sopa que extrae individualmente y inserta en variables los datos requeridos
            # de cada juego
            num = random.randint(0, len(games_list))
            name = games_list[num].select('div.gameListRowItemName.ellipsis')
            for h in range(0, len(name)):
                r_name = name[h].text
            img = games_list[num].findAll('img', class_='game_capsule')
            for j in img:
                # if j['src'].endswith('.jpg'):
                r_img = j['src']
            r_id = games_list[num].get('id')

            # Checkeo e insercion en el modelo en caso de no existir para cumplir
            # con la funcion del diseño Modelo-Vista
            try:
                GameRng.objects.get(id_game=r_id)
            except GameRng.DoesNotExist:
                game = GameRng()
                game.id_game = r_id
                game.name = r_name
                game.img = r_img
                game.save()
            return redirect('gamePicker', game=r_id)
    form = SteamIdForm()
    return render(request, 'home.html', {'form': form})


def gamePicker(request, game):
    id_game = GameRng.objects.get(id_game=game)
    return render(request, 'gamePicker.html', {'game': id_game})


def sharedGames(request):
    if request.method == 'POST':
        filled_form = SharedSteamGames(request.POST)
        if filled_form.is_valid():
            id_1 = filled_form.cleaned_data['id_1']
            id_2 = filled_form.cleaned_data['id_2']
            games_list1 = Scrapper.gameList(id_1)
            games_list2 = Scrapper.gameList(id_2)
            shared_games_names = []
            shared_games_imgs = []
            shared_games_ids = []

            for i in range(0, len(games_list1)):
                var = games_list1[i].select(
                    'div.gameListRowItemName.ellipsis')
                for k in range(0, len(var)):
                    name1 = (var[k].text)
                for j in range(0, len(games_list2)):
                    var2 = games_list2[j].select(
                        'div.gameListRowItemName.ellipsis')
                    for l in range(0, len(var2)):
                        name2 = (var2[l].text)
                    if (name1 == name2):
                        shared_games_names.append(name1)
                        var2 = games_list1[i].findAll(
                            'img', class_='game_capsule')
                        for l in var2:
                            shared_games_imgs.append(l['src'])
                        shared_games_ids.append(games_list1[i].get('id'))
                        break
            for i in shared_games_names:
                print(i)

    form = SharedSteamGames()
    return render(request, 'sharedGames.html', {'form': form})
