import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("First name")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Last name")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("myemail@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button1.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()