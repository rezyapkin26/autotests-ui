from components.base_component import BaseComponent
from playwright.sync_api import Page , expect
from elements.text import Text
from elements.button import Button
import allure

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title' )
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course' )

    @allure.step('Check visible create course toolbar view') #проверка видимости иконки создания курса
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    @allure.step('Check ')
    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()

    # реализация с паттерном PageComponent (без паттерна PageFactory)
    #     self.title = page.get_by_test_id('create-course-toolbar-title-text')
    #     self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')
    #
    # def check_visible(self, is_create_course_disabled: bool = True):
    #     expect(self.title).to_be_visible()
    #     expect(self.title).to_have_text('Create course')
    #
    #     expect(self.create_course_button).to_be_visible()
    #
    #     if is_create_course_disabled:
    #         expect(self.create_course_button).to_be_disabled()
    #     if not is_create_course_disabled:
    #         expect(self.create_course_button).to_be_enabled()
    #
    # def click_create_course_button(self):
    #     self.create_course_button.click()
    #
    # def check_disabled_create_course_button(self):
    #     expect(self.create_course_button).to_be_disabled()
