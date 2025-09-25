from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

search_field = driver.find_element(By.CSS_SELECTOR, 'input')
search_field.send_keys("12345")

sleep(3)
search_field.clear()

search_field.send_keys("54321")
sleep(3)
driver.quit()

