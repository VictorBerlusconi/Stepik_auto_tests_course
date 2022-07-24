import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_url1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        #проверяем заполнение обязательных полей
        element1 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control first\"]")
        element1.send_keys("myinput1")
        element2 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control second\"]")
        element2.send_keys("myinput2")
        element3 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control third\"]")
        element3.send_keys("myinput3")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is not correct")

    def test_url2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # проверяем заполнение обязательных полей
        element1 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control first\"]")
        element1.send_keys("myinput1")
        element2 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control second\"]")
        element2.send_keys("myinput2")
        element3 = browser.find_element(By.XPATH, "//input[@required and @class=\"form-control third\"]")
        element3.send_keys("myinput3")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text is not correct")


if __name__ == "__main__":
    pytest.main()
