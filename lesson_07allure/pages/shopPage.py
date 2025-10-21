from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации пользователя (https://www.saucedemo.com)."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver: webdriver.Chrome) -> None:
        """
        Инициализация объекта страницы логина.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу авторизации.
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход пользователя в систему.

        :param username: имя пользователя.
        :param password: пароль.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


class InventoryPage:
    """Страница со списком товаров (инвентаря)."""

    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы товаров.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param product_name: название товара, отображаемое на странице.
        """
        locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button",
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


class CartPage:
    """Страница корзины пользователя."""

    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def checkout(self) -> None:
        """
        Нажимает кнопку 'Checkout' для перехода к оформлению заказа.
        """
        self.driver.find_element(By.ID, "checkout").click()


class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму данными покупателя и продолжает оформление.

        :param first_name: имя покупателя.
        :param last_name: фамилия покупателя.
        :param postal_code: почтовый индекс покупателя.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Возвращает текст с итоговой суммой заказа.

        :return: строка с суммой, например 'Total: $32.39'.
        """
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text