from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://www.saucedemo.com/')
user_name=driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('standard_user')
password=driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')

login=driver.find_element(By.CSS_SELECTOR, '#login-button').click()

add_backpack=driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
add_bolt=driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
add_onesie=driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

cart=driver.find_element(By.CSS_SELECTOR, 'span[class="shopping_cart_badge"]').click()
checkout=driver.find_element(By.CSS_SELECTOR, '#checkout').click()
first_name=driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('Dmitriy')
last_name= driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('Palkin')
postal_code=driver.find_element(By.CSS_SELECTOR, '#postal-code')
postal_code.send_keys('665813')
continue_btn=driver.find_element(By.CSS_SELECTOR, '#continue').click()
total=driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
print (total)

assert total =='Total: $58.29'

sleep(10)