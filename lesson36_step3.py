import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def answer():
    return str(math.log(int(time.time())))


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
    # простое ожидание открытия страницы 5 сек
    browser.implicitly_wait(7)
    input1 = browser.find_element_by_css_selector(".textarea.string-quiz__textarea.ember-text-area.ember-view")
    input1.send_keys(answer())
    button1 = browser.find_element_by_css_selector(".submit-submission")
    button1.click()
    # ожидание появления элемента
    # time.sleep(3)
    res = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    # res = browser.find_element_by_css_selector(".smart-hints__hint")
    # assert res.text == "Correct!", "I's fail =("
    print(res.text)

# запуск: pytest -s -v lesson36_step3.py
