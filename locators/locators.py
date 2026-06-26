from selenium.webdriver.common.by import By

class Locators:

    # Главная страница

    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"

    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип "Stellar Burgers"

    # Кнопка "Оформить заказ"

    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

    # Конструктор

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"

    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"

    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"

    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]")  # Активная вкладка

    # Форма регистриции

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле "Имя"

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле "Email"

    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле "Пароль"

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"

    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"

    LOGIN_LINK_ON_REGISTER = (By.XPATH, "//a[text()='Войти']")  # Кнопка "Войти"

    # Форма входа

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name' and @type='text']")  # Поле "Email"

    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль' and @type='password']")  # Поле "Пароль"

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"

    # Форма восстановления пароля

    EMAIL_INPUT_ON_FORGOT_PASSWORD = (By.XPATH, "//input[@name='name' and @type='text']")  # Поле "Email"

    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Кнопка "Восстановить"

    LOGIN_LINK_ON_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти"

    # Личный кабинет

    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка "Выйти"


