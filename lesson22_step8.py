from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
#import math
import os

#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element_by_css_selector("input[name='firstname']")
    fname.send_keys("Alexandr")
    
    lname = browser.find_element_by_css_selector("input[name='lastname']")
    lname.send_keys("Pushkin")
    
    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys("alex@ya.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполн€емого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавл€ем к этому пути им€ файла 
    ffile = browser.find_element_by_css_selector("input#file")
    ffile.send_keys(file_path)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    
    # ќтправл€ем заполненную форму
    dis = button.get_attribute("disabled")
    if dis!="disabled":
        button.click()
        # ожидание
        time.sleep(10)
    else:
        assert "Error"
finally:
    # закрываем браузер после всех манипул€ций
    browser.quit()




