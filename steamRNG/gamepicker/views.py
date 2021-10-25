import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.opera.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from django.shortcuts import render
from.forms import SteamIdForm
# Create your views here.

options = Options()
options.binary_location = r'C:\Program Files\Opera\80.0.4170.63\Opera.exe'


def home(request):
    if request.method == 'POST':
        filled_form = SteamIdForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            driver = webdriver.Opera(
                options=options, executable_path=r'C:\Program Files\Opera\80.0.4170.63\operadriver.exe')
            driver.get('https://steamcommunity.com/id/'+text+'/games/?tab=all')
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            soup = BeautifulSoup(driver.page_source, 'lxml')
            games_ids = soup.find_all('div', class_='gameListRow')

            driver.close()
            for i in range(0, len(games_ids)):

                # Sopa y ciclo especifico para obtener el nombre de la bibloteca de juegos
                name = games_ids[i].select('div.gameListRowItemName.ellipsis')
                for h in range(0, len(name)):
                    print(name[h].text)

                # Sopa y ciclo especifico para obtener la fuente de la imagen del juego
                img = games_ids[i].findAll('img', class_='game_capsule')
                for j in img:
                    if j['src'].endswith('.jpg'):
                        print(j['src'])

                # Imprecion del Id especifico del juego
                print(games_ids[i].get('id'))

                # print(games_imgs[i])

            # print(games_hours)
            # print(games_imgs)

    form = SteamIdForm()
    return render(request, 'home.html', {'form': form})
