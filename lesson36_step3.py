import pytest
import time
import math
from selenium import webdriver

answer = math.log(int(time.time()))

urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', urls)
def test_guest_should_see_login_link(browser, url):
    link = url
    browser.get(link)
    input1 = browser.find_element_by_css_selector("#ember100")
    input1.send_keys(answer)
    like = browser.find_element_by_css_selector("#ember47")
    like.click()
    button1 = browser.find_element_by_css_selector(".submit-submission")
    button1.click()
    # ожидание
    time.sleep(10)

# запуск: pytest -s -v lesson36_step3.py
