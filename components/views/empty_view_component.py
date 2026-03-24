from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.icon import Icon
import allure

# компонент страницы, когда нет добавленных курсов и этот же компонент повторяется при добавлении курса.
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon' )
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Title' )
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Description' )

    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)

    # реализация с патерном PageComponents (без патерна PageFactory)
    #     self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
    #     self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
    #     self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')
    #
    # def check_visible(self, title: str, description: str):
    #     # проверяем видимость иконки
    #     expect(self.icon).to_be_visible()
    #     # проверяем видимость заголовка и текст
    #     expect(self.title).to_be_visible()
    #     expect(self.title).to_have_text(title)
    #     # проверяем видимость описания и текст
    #     expect(self.description).to_be_visible()
    #     expect(self.description).to_have_text(description)