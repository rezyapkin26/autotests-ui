from components.base_component import BaseComponent
from playwright.sync_api import Page , expect
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Menu')
        self.edit_menu_button = Button(page, 'course-view-menu-button', 'Edit')
        self.delete_menu_button = Button(page, 'course-view-menu-button', 'Delete')

    def click_edit(self, index: int):
        self.menu_button.click(nth=index)
        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    def click_delete(self, index: int):
        self.menu_button.click(nth=index)
        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)

    # реализация с паттерном PageComponent (без паттерна Page Factory)
    #     self.menu_button = page.get_by_test_id('course-view-menu-button')
    #     self.edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
    #     self.delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')
    # # проверка полноценного нажатия
    # def click_edit(self ,index: int):
    #     self.menu_button.nth(index).click()
    #
    #     expect(self.edit_menu_button.nth(index)).to_be_visible()
    #
    #     self.edit_menu_button.nth(index).click()
    #
    # def click_delete(self ,index: int):
    #     self.menu_button.nth(index).click()
    #
    #     expect(self.delete_menu_button.nth(index)).to_be_visible()
    #
    #     self.delete_menu_button.nth(index).click()
