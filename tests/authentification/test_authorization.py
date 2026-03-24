import pytest
import allure
from pages.authentification.login_page import LoginPage
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories
from allure_commons.types import Severity

@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTags.REGRESSION, AllureTags.AUTHORIZATION) # тэги принято писать капсом
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStories.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.title('User login with correct email and password')
    @allure.severity(Severity.BLOCKER)

    def test_successful_authorization(self, registration_page: RegistrationPage,
                                      dashboard_page: DashboardPage,
                                      login_page: LoginPage,):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='rezyapkin.petr1211@yandex.ru',
                                                 username='username',
                                                 password='password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()

        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='rezyapkin.petr1211@yandex.ru', password='password')
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()



    @pytest.mark.parametrize('email, password',
                             [
                                 ("user.name@gmail.com", "password"),
                                 ("user.name@gmail.com", '  '),
                                 ('  ', 'password')
                             ]
                             )
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.title('User login with wrong email or password') # allure заголовок для отчета
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str,
                                                   password: str):  # тест с PageObject
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        # реализация без компонента LoginFormComponent
        # login_page.fill_login_form(email=email, password=password)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


    @allure.tag(AllureTags.NAVIGATION)
    @allure.title("Navigation from login page to registration page")
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self,
                                                         login_page: LoginPage,
                                                         registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()
        registration_page.registration_form.check_visible(email='', password='', username='')

# реализация без тестового класса
# @pytest.mark.regression
# @pytest.mark.authorization
# @pytest.mark.parametrize('email, password',
#                          [
#                           ("user.name@gmail.com","password"),
#                           ("user.name@gmail.com", '  '),
#                           ('  ', 'password')
#                           ]
#                          )
# def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str): #тест с PageObject
#     login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
#     #реализация без компонента LoginFormComponent
#     # login_page.fill_login_form(email=email, password=password)
#     login_page.login_form.fill(email = email, password = password)
#     login_page.click_login_button()
#     login_page.check_visible_wrong_email_or_password_alert()


# тест обычный.

    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    #
    # email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    # email_input.fill('user.name@gmail.com')
    #
    # password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    # password_input.fill('password')
    #
    # login_button = chromium_page.get_by_test_id('login-page-login-button')
    # login_button.click()
    #
    # wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # expect(wrong_email_or_password_alert).to_be_visible()
    #
    # expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')