from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    print('Start browser')
    driver = webdriver.Chrome(service=Service()) #mac
    driver.maximize_window()
    yield driver
    driver.quit()