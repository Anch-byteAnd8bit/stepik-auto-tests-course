from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
succeed = "Congratulations! You have successfully registered!"


def tst(link):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element_by_css_selector(".first_block .first")
    fname.send_keys("Maria")
    lname = browser.find_element_by_css_selector(".first_block .second")
    lname.send_keys("Ivanova")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("masha@list.bk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(succeed, tst(link1), "Ошибка в 1 тесте!")

    def test_abs2(self):
        self.assertEqual(succeed, tst(link2), "Ошибка во 2 тесте!")


if __name__ == "__main__":
    unittest.main()
