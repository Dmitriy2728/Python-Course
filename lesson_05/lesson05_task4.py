from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

search_field = driver.find_element(By.XPATH,'//input[@id="username"]')
search_field.send_keys("tomsmith")
search_field = driver.find_element(By.XPATH,'//input[@id="password"]')
search_field.send_keys("SuperSecretPassword!")

button=driver.find_element(By.CSS_SELECTOR, "button.radius")
button.click()

flash=driver.find_element(By.CSS_SELECTOR, 'div.flash').text

print(flash)

sleep(10)

driver.quit()
