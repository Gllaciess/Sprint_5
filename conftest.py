import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.helpers import generate_email, generate_password, generate_name
from locators.locators import Locators as locators
from constants import Urls

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def register_new_user(driver):

    driver.get(Urls.REGISTER_URL)

    name = generate_name()
    email = generate_email()
    password = generate_password()

    driver.find_element(*locators.NAME_INPUT).send_keys(name)
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()

    driver.get(Urls.LOGIN_URL)

    return email, password


@pytest.fixture
def login_user(driver, register_new_user):

    email, password = register_new_user

    driver.get(Urls.LOGIN_URL)

    driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.LOGIN_BUTTON).click()

    import time
    time.sleep(2)

    return email, password


