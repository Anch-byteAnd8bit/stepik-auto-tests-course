import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="Так надо!")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")

        # @pytest.mark.smoke - обычная метка
        # @pytest.mark.skip - пометка "пропустить"
        # @pytest.mark.xfail(reason="reason of fail") - пометка заведомопадающего теста

        # pytest -s -v -m smoke test_fixture10.py - тесты по маркировке
        # pytest -s -v -m "not smoke" test_fixture10.py - инверсия
        # pytest -s -v -m "smoke or regression" test_fixture10.py - объединение маркировки
        # pytest -s -v -m "smoke and win10" test_fixture10.py - через логич. И
        # pytest -rsx test_fixture10.py - тест с учетом зараннее помеченных падающих тестов

        # -v - режим verbous (многословный). Детально расскажет о прохождении.
        #
        # -rx - report on XFAIL (отчитаться о наличии метки XFAIL).
        #   В целом, даже без (remark = "") покажет в каком тесте была метка.
        #
        # show extra test summary info as specified by chars:
        #                         (f)ailed, (E)rror, (s)kipped, (x)failed, (X)passed,
        #                         (p)assed, (P)assed with output, (a)ll except passed
        #                         (p/P), or (A)ll. Warnings are displayed at all times
        #                         except when --disable-warnings is set.
