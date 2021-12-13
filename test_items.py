import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add(browser):
    browser.get(link)
    buttons = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(buttons) > 0, "No button for add"

