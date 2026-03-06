from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


# компонент страницы, когда нет добавленных курсов и этот же компонент повторяется при добавлении курса.
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    def check_visible(self, title: str, description: str):
        # проверяем видимость иконки
        expect(self.icon).to_be_visible()
        # проверяем видимость заголовка и текст
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        # проверяем видимость описания и текст
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)