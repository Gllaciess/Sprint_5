from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators as locators
from constants import Urls

class TestConstructor:

    def test_switch_to_buns_tab(self, driver):

        driver.get(Urls.BASE_URL)

        sauces_element = driver.find_element(*locators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", sauces_element)

        buns_element = driver.find_element(*locators.BUNS_TAB)
        driver.execute_script("arguments[0].click();", buns_element)

        active_tab = driver.find_element(*locators.ACTIVE_TAB)
        assert "Булки" in active_tab.text

    def test_switch_to_sauces_tab(self, driver):

        driver.get(Urls.BASE_URL)

        element = driver.find_element(*locators.SAUCES_TAB)
        driver.execute_script("arguments[0].click();", element)

        active_tab = driver.find_element(*locators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text

    def test_switch_to_fillings_tab(self, driver):

        driver.get(Urls.BASE_URL)
        element = driver.find_element(*locators.FILLINGS_TAB)

        driver.execute_script("arguments[0].click();", element)
        active_tab = driver.find_element(*locators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text


