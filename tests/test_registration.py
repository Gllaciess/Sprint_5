from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators as locators
from helpers.helpers import generate_email, generate_password, generate_name


class TestRegistration:

    def test_successful_registration(self, driver):

        driver.get("https://stellarburgers.education-services.ru/register")

        name = generate_name()
        email = generate_email()
        password = generate_password()

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("stellarburgers.education-services.ru/login")
        )

        assert "login" in driver.current_url

    def test_registration_invalid_password_error(self, driver):

        driver.get("https://stellarburgers.education-services.ru/register")

        name = generate_name()
        email = generate_email()
        password = "12345"

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        error = driver.find_element(*locators.PASSWORD_ERROR)
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text


