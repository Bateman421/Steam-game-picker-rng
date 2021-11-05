from selenium.webdriver.opera.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = Options()
options.binary_location = r'C:\Program Files\Opera\80.0.4170.63\Opera.exe'


class Scrapper():
    def gameList(steam_id):

        # Selenium driver, en teoria solo deveria correr "server side" Cliente final
        # no deberia toparse con esta funcionalidad corriendo en su terminal
        driver = webdriver.Opera(
            options=options, executable_path=r'C:\Program Files\Opera\80.0.4170.63\operadriver.exe')
        driver.get('https://steamcommunity.com/id/'+steam_id+'/games/?tab=all')
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        games = soup.find_all('div', class_='gameListRow')
        driver.close()
        return games
