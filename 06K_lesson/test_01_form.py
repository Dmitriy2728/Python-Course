from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

#driver.implicitly_wait(16)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.CSS_SELECTOR, 'input[name ="first-name"]')
first_name.send_keys('Иван')
last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
last_name.send_keys('Петров')
address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
address.send_keys('Ленина, 55-3')
city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
city.send_keys('Москва')
country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
country.send_keys('Россия')
email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
email.send_keys('test@skypro.com')
phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
phone.send_keys('+7985899998787')
job = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
job.send_keys('QA')
company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
company.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


zip_code = driver.find_element(By.ID, 'zip-code')

zip_color = zip_code.value_of_css_property ("background-color")

assert zip_color == "rgba(248, 215, 218, 1)"

fields = ['#first-name', '#last-name', '#city', '#e-mail', '#address', '#job-position', '#country', '#phone', \
          '#company'
]
for field in fields:
    element = driver.find_element(By.CSS_SELECTOR, field)
    assert "rgba(209, 231, 221, 1)" in element.value_of_css_property ("background-color")

driver.quit()




