import pytest
import allure
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка корректности сложения чисел на онлайн-калькуляторе")
@allure.description("Тест выполняет вычисление 7 + 8 и проверяет, что результат равен 15.")
@allure.feature("Онлайн-калькулятор — операция сложения")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc_sum(driver):
    """Тест проверяет, что калькулятор корректно выполняет сложение."""

    calc_page = CalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()

    with allure.step("Установка задержки перед вычислением"):
        calc_page.set_delay(45)

    with allure.step("Ввод первого числа: 7"):
        calc_page.press_number(7)

    with allure.step("Выбор операции сложения '+'"):
        calc_page.press_operator("+")

    with allure.step("Ввод второго числа: 8"):
        calc_page.press_number(8)

    with allure.step("Нажатие кнопки '=' для вычисления"):
        calc_page.press_equal()

    with allure.step("Получение результата вычисления"):
        result = calc_page.get_result(expected="15")

    with allure.step("Проверка корректности результата"):
        assert result == "15", f"Expected 15, but got {result}"