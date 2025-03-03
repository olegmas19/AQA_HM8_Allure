import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene import browser



def test_github_issue_clear_selene():
    browser.open("https://github.com")
    browser.element(".search-input").click()
    browser.element("#query-builder-test").type("eroshenkoam/allure-example").submit()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element('//span[contains(text(),"One piece")]').should(be.visible)


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.description("Тестовая аннотация")
@allure.suite("UI-Тесты")
@allure.link("https://github.com", name="Testing")
def test_github_issue_allure_step():

    with allure.step("Открываем главную страницу"):
      browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
      browser.element(".search-input").click()
      browser.element("#query-builder-test").type("eroshenkoam/allure-example").submit()

    with allure.step("Переходим по ссылке репозитория"):
      browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
      browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с именем One piece"):
      browser.element('//span[contains(text(),"One piece")]').should(be.visible)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.description("Тестовая аннотация")
@allure.suite("UI-Тесты")
@allure.link("https://github.com", name="Testing")
def test_github_issue_allure_step_decor():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_name("One piece")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").type(repo).submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()

@allure.step("Проверяем наличие Issue с именем {name}")
def should_see_issue_with_name(name):
    browser.element(f'//span[contains(text(),"{name}")]').should(be.visible)






