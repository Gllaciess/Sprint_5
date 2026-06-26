from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators as locators
from helpers.helpers import generate_email, generate_password, generate_name
from constants import Urls
from data import TestData


class TestRegistration:

    def test_successful_registration(self, driver):

        driver.get(Urls.REGISTER_URL)

        name = generate_name()
        email = generate_email()
        password = generate_password()

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 15).until(
            EC.url_to_be(Urls.LOGIN_URL)
        )

        assert driver.current_url == Urls.LOGIN_URL

    def test_registration_invalid_password_error(self, driver):

        driver.get("https://stellarburgers.education-services.ru/register")

        name = TestData.VALID_NAME
        email = TestData.VALID_EMAIL
        password = TestData.INVALID_PASSWORD

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        error = driver.find_element(*locators.PASSWORD_ERROR)
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text


