import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_open_page():
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_check_title():
    # driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_input_search_field():
    driver.get('https://openweathermap.org/')
    #driver.implicitly_wait(10)
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys("New York")
    search_option = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)']")
    search_option.click()

    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    search_button.click()
    #time.sleep(10)
    driver.implicitly_wait(10)
    displayed_text = driver.find_element(By.XPATH, '//*[@id="weather-widget"]//h2')
    assert displayed_text == 'New York City, US'
