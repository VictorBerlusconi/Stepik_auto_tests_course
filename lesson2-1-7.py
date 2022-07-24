import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton1.click()
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button1.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

