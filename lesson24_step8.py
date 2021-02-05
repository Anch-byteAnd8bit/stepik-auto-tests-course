from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока цена не станет равна 100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    
    button = browser.find_element_by_css_selector("#book")
    button.click()

    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)


    button = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    # Отправляем заполненную форму
    dis = button.get_attribute("disabled")
    button.click()
    # ожидание
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()