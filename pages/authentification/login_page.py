import re

from playwright.sync_api import Page , expect

from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.text import Text
from elements.link import Link
import allure


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        # реализовано в компоненте LoginFormComponent
        # реализация без компонента LoginFormComponent
        # self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        # self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page,'login-page-registration-link', 'Registration')
        self. wrong_email_or_password_alert = Text(page,'login-page-wrong-email-or-password-alert', name='Wrong email or password')


        # реализовано в компоненте LoginFormComponent
        # реализация без компонента LoginFormComponent
    # def fill_login_form(self , email: str, password: str):
    #     self.email_input.fill(email)
    #     expect(self.email_input).to_have_value(email)
    #
    #     self.password_input.fill(password)
    #     expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()
        self.check_current_url(re.compile('.*/#/auth/registration'))


    @allure.step('Check visible wrong email or password alert')
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')

# Из чего состоит метод PageObject например fill_login_form
# 1 слово fill - действие что мы будем делать с элементом
# 2 слово login - контекст с чем мы будем работать какое поле мы заполняем
# 3 слово form - c чем конкретно мы будем работать. (Форма, кнопка, ссылка, аллерт и тд) в данном примере с формой
