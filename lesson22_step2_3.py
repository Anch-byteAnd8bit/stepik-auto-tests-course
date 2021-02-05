from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
try: 
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    z = int(x) + int(y)
    print(z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
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


