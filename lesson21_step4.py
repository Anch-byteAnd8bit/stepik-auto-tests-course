from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector(".nowrap#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_css_selector("input#answer")
    input.send_keys(y)
    checkbox = browser.find_element_by_css_selector(".form-check-input#robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector(".form-check-input#robotsRule")
    radiobox.click()    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



