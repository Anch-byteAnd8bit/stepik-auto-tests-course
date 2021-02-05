from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)
    
    checkbox = browser.find_element_by_css_selector(".form-check-input#robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector(".form-check-input#robotsRule")
    radiobox.click()
    
    # Отправляем заполненную форму
    dis = button.get_attribute("disabled")
    if dis!="disabled":
        button.click()
        # ожидание
        time.sleep(10)
    else:
        assert "Error"
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()



