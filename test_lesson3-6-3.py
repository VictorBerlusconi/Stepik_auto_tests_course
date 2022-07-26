import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(3)
    textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
    textarea.send_keys(answer())
    button1 =WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    button1.click()
    #time.sleep(2)
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    actual_result = result.text
    assert actual_result == "Correct!",\
        f"Result is not correct!, got >>>{actual_result}<<<"

