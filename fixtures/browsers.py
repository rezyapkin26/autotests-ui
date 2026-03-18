import pytest
from playwright.sync_api import  Page, Playwright

# from fixtures.pages import registration_page
from pages.authentification.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page = page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='rezyapkin.petr1211@yandex.ru',username='username', password='password')
        registration_page.click_registration_button()
        # реализация без паттернов
        # page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        #
        # email_input = page.get_by_test_id("registration-form-email-input").locator('input')
        # email_input.fill('rezyapkin.petr1211@yandex.ru')
        #
        # username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        # username_input.fill('username')
        #
        # password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        # password_input.fill('password')
        #
        # registration_button = page.get_by_test_id('registration-page-registration-button')
        # registration_button.click()

        context.storage_state(path='browser-state.json')
        browser.close()

@pytest.fixture(scope="function")
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page :
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        yield context.new_page()
        browser.close()
