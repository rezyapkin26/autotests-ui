import pytest
from playwright.sync_api import  Page, Playwright

# from fixtures.pages import registration_page
from pages.authentification.registration_page import RegistrationPage
from _pytest.fixtures import  SubRequest
import allure

from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute

@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
# def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(record_video_dir='./videos')
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#
#     yield page
#
#     context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
#     browser.close()
#
#     allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
#     allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )

# def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state="browser-state.json", record_video_dir='./videos')
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#
#     yield page
#
#     context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
#     browser.close()
#
#     allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
#     allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

# def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
#
#         # yield from initialize_playwright_page(playwright, test_name=request.node.name)
#
#
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(record_video_dir= './videos')
#         context.tracing.start(screenshots=True, snapshots=True, sources= True)
#         page = context.new_page()
#
#
#         yield page
#
#         context.tracing.stop(path= f'./tracing/{request.node.name}.zip')
#
#         browser.close()
#
#         allure.attach.file(f'./tracing/{request.node.name}.zip', name = 'trace', extension = 'zip')
#         allure.attach.file(page.video.path(), name = 'video', attachment_type= allure.attachment_type.WEBM)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(base_url=settings.get_base_url())
        page = context.new_page()

        registration_page = RegistrationPage(page = page)
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(email=settings.test_user.email,
                                                 username=settings.test_user.username,
                                                 password=settings.test_user.password
        )
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

        context.storage_state(path=settings.browser_state_file)
        browser.close()

