                                    ## Задание №2    ###

from typing import Callable, Tuple


def create_handlers(callback: Callable) -> Tuple[Callable]:
    handlers = tuple([lambda step=step: callback(step) for step in range(5)])
    return handlers


def execute_handlers(handlers: Tuple[Callable]) -> None:
    for handler in handlers:
        handler()

                                    ## Задание №3    ###

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from typing import Tuple


def get_html(url: str) -> str:
    browser = webdriver.Chrome()
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "main-content")))
    html = browser.page_source
    return html


def get_tags(html: str) -> Tuple[int]:
    soup = BeautifulSoup(html, 'html.parser')
    total_tags = len(soup.find_all())
    non_empty_tags = len([tag for tag in soup.find_all() if tag.text.strip() != ''])
    return total_tags, non_empty_tags


url = 'https://greenatom.ru/'
# html = get_html(url)
# total_tags, non_empty_tags = get_tags(html)
#
# print(f"Всего тегов:{total_tags}")
# print(f"Всего непустых тегов:{non_empty_tags}")

                                        ## Задание 4 ###
import requests


def get_ip() -> str:
    url = ('https://ipwho.is/', 'https://ident.me/json/')
    req = requests.get(url[0])
    if not req:
        req = requests.get(url[1])
    if not req:
        raise ValueError('Не удалось получить данные по ip')
    req_json = req.json()
    return req_json.get('ip')


# print(get_ip())


                                        ## Задание 5 ###
import re


class VersionComparison:

    @classmethod
    def change(cls, value: str) -> float:
        if value[0] == '0':
            value = value.replace('0', '0.', 1)
        return float(value)

    def __call__(self, v1: str, v2: str) -> int:
        self.validator(v1)
        self.validator(v2)
        ver1 = list(map(self.change, v1.split('.')))
        ver2 = list(map(self.change, v2.split('.')))
        temp = zip(ver1, ver2)
        for i in temp:
            if i[0] == i[1]:
                continue
            return -1 if i[0] < i[1] else 1
        if len(ver1) == len(ver2):
            return 0
        else:
            return -1 if len(ver1) < len(ver2) else 1

    @staticmethod
    def validator(value: str) -> None:
        if not value or not isinstance(value, str):
            raise ValueError('Вводимое значение должно быть непустой строкой')
        val = value.replace('.', '')
        if not val.isdigit() or re.findall(r"^[.]|[.]$", value):
            raise TypeError('допустимый формат проверки версии xx.xx.xx -где x любое число')

# check = VersionComparison()
# print(check('1.22', '1.12.33.1'))
