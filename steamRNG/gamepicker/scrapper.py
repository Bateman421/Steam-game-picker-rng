from selenium.webdriver.opera.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time


class Scrapper():
    def gameList(steam_id):

        # Selenium driver, en teoria solo deveria correr "server side" Cliente final
        # no deberia toparse con esta funcionalidad corriendo en su terminal
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            '.\gamepicker\WebDriver\chromedriver',
            options=options)
        driver.get('https://steamcommunity.com/id/'+steam_id+'/games/?tab=all')
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        games = soup.find_all('div', class_='gameListRow')
        driver.close()
        return games
