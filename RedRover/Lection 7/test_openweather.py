import time

from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=Service()) #mac

''' -------------Win----------------
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
'''


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_check_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_input_search_field(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys("New York")
    search_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[class='button-round dark']")))
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")))
    search_option.click()
    displayed_text = driver.find_element(By.XPATH, '//*[@id="weather-widget"]//h2')
    assert displayed_text.text == 'New York City, US'


def test_login_error_text(driver, faker):
    driver.get('https://home.openweathermap.org/users/sign_in')
    driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_email']").send_keys(faker.email())
    driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='user_password']").send_keys(faker.password())
    driver.find_element(By.XPATH, "//div[@class='sign-form']//input[@value='Submit']").click()
    assert driver.find_element(By.XPATH, "//div[@class='panel-body']").text == 'Invalid Email or password.'
