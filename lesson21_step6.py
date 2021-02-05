from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_css_selector(".check-input#robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector(".check-input#robotsRule")
    radiobox.click()    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    dis = button.get_attribute("disabled")
    if dis!="disabled":
        button.click()
        # ожидание
        time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

