from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Email" )
        self.password_input = Input(page, 'registration-form-password-input', 'Password' )
        self.username_input = Input(page, 'registration-form-username-input', 'Username' )
    @allure.step('Fill registration form')
    def fill(self, email: str, password: str, username: str):
            self.email_input.fill(email)
            self.email_input.check_have_value(email)

            self.password_input.fill(password)
            self.password_input.check_have_value(password)

            self.username_input.fill(username)
            self.username_input.check_have_value(username)
    @allure.step('Check visible registration form')
    def check_visible(self, email: str, password: str, username: str):
            self.email_input.check_visible()
            self.email_input.check_have_value(email)

            self.password_input.check_visible()
            self.password_input.check_have_value(password)

            self.username_input.check_visible()
            self.username_input.check_have_value(username)



    # реализация с патерном PageComponents
    #     self.email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    #     self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #     self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #
    # def fill(self, email:str, username:str, password:str):
    #     self.email_input.fill(email)
    #     expect(self.email_input).to_have_value(email)
    #
    #     self.username_input.fill(username)
    #     expect(self.username_input).to_have_value(username)
    #
    #     self.password_input.fill(password)
    #     expect(self.password_input).to_have_value(password)
    #
    # def check_visible(self, email:str, username:str, password:str):
    #     expect(self.email_input).to_be_visible()
    #     expect(self.email_input).to_have_value(email)
    #
    #     expect(self.username_input).to_be_visible()
    #     expect(self.username_input).to_have_value(username)
    #
    #     expect(self.password_input).to_be_visible()
    #     expect(self.password_input).to_have_value(password)