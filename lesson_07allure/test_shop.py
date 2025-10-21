import pytest
import allure
from selenium import webdriver
from pages.shopPage import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    """Инициализация и завершение работы WebDriver."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы покупки в интернет-магазине")
@allure.description("Тест выполняет авторизацию, добавление товаров в корзину, оформление заказа и проверку итоговой суммы.")
@allure.feature("Интернет-магазин — расчет итоговой суммы")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total(driver):
    """Тест проверяет корректность итоговой суммы заказа."""

    with allure.step("Открытие страницы авторизации"):
        login_page = LoginPage(driver)
        login_page.open()

    with allure.step("Авторизация пользователя"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Ivan", "Ivanov", "123456")

    with allure.step("Получение итоговой суммы"):
        total = checkout_page.get_total()

    with allure.step("Проверка корректности итоговой суммы"):
        assert total == "Total: $58.29", f"Ожидалось 'Total: $58.29', получено {total}"
