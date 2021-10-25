from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.opera.options import Options
from selenium import webdriver
import time
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
            # time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            games_names = soup.select('div.gameListRowItemName.ellipsis')
            # games_hours = soup.find_all('h5')
            # games_imgs = soup.find_all('img')
            driver.close()
            for i in range(0, len(games_names)):
                print(games_names[i].text)
            # print(games_hours)
            # print(games_imgs)

    form = SteamIdForm()
    return render(request, 'home.html', {'form': form})
