from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Страница онлайн-калькулятора (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)."""

    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """
        Открывает страницу калькулятора в браузере.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку выполнения вычислений.

        :param seconds: количество секунд задержки (целое число).
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_number(self, number: int) -> None:
        """
        Нажимает на кнопку с указанным числом.

        :param number: число, отображаемое на кнопке калькулятора.
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{number}']").click()

    def press_operator(self, operator: str) -> None:
        """
        Нажимает на кнопку оператора (например '+', '-', '*', '/').

        :param operator: символ оператора, отображаемый на кнопке.
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{operator}']").click()

    def press_equal(self) -> None:
        """
        Нажимает кнопку '=' для получения результата.
        """
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self, expected: str = "15", timeout: int = 50) -> str:
        """
        Ожидает появления ожидаемого результата и возвращает значение с экрана калькулятора.

        :param expected: ожидаемое значение результата.
        :param timeout: максимальное время ожидания в секундах.
        :return: строка с отображаемым на экране результатом.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), expected)
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
    