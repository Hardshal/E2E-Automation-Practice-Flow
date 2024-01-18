import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for phone in phones:
    name = phone.find_element(By.XPATH,'div/h4/a').text
    if name == 'Blackberry':
        phone.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary").click()

driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

driver.find_element(By.ID, "country").send_keys("In")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))

driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.CSS_SELECTOR, "label[for = 'checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()

success = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success" in success
