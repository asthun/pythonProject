import time
from selenium.webdriver.common.by import By
import pytest
import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#browser.get('https://suninjuly.github.io/xpath_examples')

def test_open():
    browser.get('https://suninjuly.github.io/cats.html')
    #time.sleep(5)


def test_find_element():
    test_open()
    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    print(bullet_cat.text)

def test_find_view_buttons():
    test_open()
    view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_buttons)
    assert len(view_buttons) == 4, 'wrong length'