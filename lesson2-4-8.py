from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button1 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button1.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()