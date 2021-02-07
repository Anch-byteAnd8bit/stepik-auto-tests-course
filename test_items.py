link = "http://selenium1py.pythonanywhere.com/"


def test_check_item_in_cart(browser):
    browser.get(link)
    btn = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert btn, "Button not found!"
