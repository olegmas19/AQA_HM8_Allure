from selene import browser, by, be
from selene.support.shared.jquery_style import s

def test_github():
    browser.open("https://github.com")
