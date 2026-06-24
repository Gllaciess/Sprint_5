from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators as locators


class TestLogout:

    def test_logout_from_personal_account(self, driver, register_new_user):

        email, password = register_new_user

        driver.get("https://stellarburgers.education-services.ru/login")

        driver.find_element(*locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 15).until(
            EC.url_contains("stellarburgers.education-services.ru")
        )

        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("stellarburgers.education-services.ru")
        )

        driver.find_element(*locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("stellarburgers.education-services.ru/login")
        )

        assert "login" in driver.current_url


