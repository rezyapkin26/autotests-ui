from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.input import Input
from elements.textarea import TextArea
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated time' )
        self.description_textarea = TextArea(page, 'create-course-form-description-input', 'Description' )
        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score' )
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score' )


    @allure.step('Check visible create course form') # проверить видимость формы создания курса
    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.check_visible()
        self.title_input.check_have_value(title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.check_visible()
        self.description_textarea.check_have_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(min_score)

    @allure.step('Fill create course form') #заполнить форму создания курса
    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(estimated_time)
        self.estimated_time_input.check_have_value(estimated_time)

        self.description_textarea.fill(description)
        self.description_textarea.check_have_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_have_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_have_value(min_score)
    # реализация с паттерном PageComponent (без паттерна PageFactory)
    #     self.title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
    #     self.estimated_time_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
    #     self.description_textarea = page.get_by_test_id('create-course-form-description-input').locator('textarea').first  #first - выбираем первую textarea, если их несколько
    #     self.max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
    #     self.min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')
    #
    # def fill(self,title: str, estimated_time: str, description: str, max_score: str, min_score: str ):
    #     self.title_input.fill(title)
    #     expect(self.title_input).to_have_value(title)
    #
    #     self.estimated_time_input.fill(estimated_time)
    #     expect(self.estimated_time_input).to_have_value(estimated_time)
    #
    #     self.description_textarea.fill(description)
    #     expect(self.description_textarea).to_have_value(description)
    #
    #     self.max_score_input.fill(max_score)
    #     expect(self.max_score_input).to_have_value(max_score)
    #
    #     self.min_score_input.fill(min_score)
    #     expect(self.min_score_input).to_have_value(min_score)
    #
    # def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
    #     expect(self.title_input).to_be_visible()
    #     expect(self.title_input).to_have_value(title)
    #
    #     expect(self.estimated_time_input).to_be_visible()
    #     expect(self.estimated_time_input).to_have_value(estimated_time)
    #
    #     expect(self.description_textarea).to_be_visible()
    #     expect(self.description_textarea).to_have_value(description)
    #
    #     expect(self.max_score_input).to_be_visible()
    #     expect(self.max_score_input).to_have_value(max_score)
    #
    #     expect(self.min_score_input).to_be_visible()
    #     expect(self.min_score_input).to_have_value(min_score)
