import time
import random
from django.http.response import JsonResponse
from selenium.webdriver.opera.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from .forms import SteamIdForm
from .models import GameRng
# Create your views here.

options = Options()
options.binary_location = r'C:\Program Files\Opera\80.0.4170.63\Opera.exe'


def home(request):
    if request.method == 'POST':
        filled_form = SteamIdForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']

            # Selenium driver, en teoria solo deveria correr "server side" Cliente final
            # no deberia toparse con esta funcionalidad corriendo en su terminal
            driver = webdriver.Opera(
                options=options, executable_path=r'C:\Program Files\Opera\80.0.4170.63\operadriver.exe')
            driver.get('https://steamcommunity.com/id/'+text+'/games/?tab=all')
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            games_ids = soup.find_all('div', class_='gameListRow')
            driver.close()

            # Sopa que extrae individualmente y inserta en variables los datos requeridos
            # de cada juego
            num = random.randint(0, len(games_ids))
            name = games_ids[num].select('div.gameListRowItemName.ellipsis')
            for h in range(0, len(name)):
                r_name = name[h].text
            img = games_ids[num].findAll('img', class_='game_capsule')
            for j in img:
                # if j['src'].endswith('.jpg'):
                r_img = j['src']
            r_id = games_ids[num].get('id')

            # Checke e insercion en el modelo en caso de no existir para cumplir
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
