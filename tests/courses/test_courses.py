import pytest
import allure
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories
from allure_commons.types import Severity

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.COURSES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStories.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStories.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list') # Проверьте отображение пустого списка курсов
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')# Создать курс
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible()

        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title="",
                                                            max_score="0",
                                                            min_score="0",
                                                            description="",
                                                            estimated_time="")

        create_course_page.create_course_exercises_toolbar_view.check_visible()

        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            max_score="100",
            min_score="10",
            description="Playwright",
            estimated_time="2 weeks"
        )

        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.image_upload_widget.upload_preview_image(
            "./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title="Playwright",
                                                   estimated_time="3 weeks",
                                                   description="Python",
                                                   max_score="100",
                                                   min_score="10",
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright",
                                                    max_score="100",
                                                    min_score="10",
                                                    estimated_time="3 weeks")
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(title="Playwright1",
                                                   estimated_time="4 weeks",
                                                   description="Python1",
                                                   max_score="90",
                                                   min_score="15",)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0,
                                                    title="Playwright1",
                                                    max_score="90",
                                                    min_score="15",
                                                    estimated_time="4 weeks")


# реализация без тестового класса
# @pytest.mark.courses
# @pytest.mark.regression
# def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
#     create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
#
#     create_course_page.create_course_toolbar_view.check_visible()
#     # реализация без компонента CreateCourseToolbarViewComponent
#     # create_course_page.check_disabled_create_course_button()
#     # create_course_page.check_visible_image_preview_empty_view()
#     create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
#     create_course_page.create_course_form.check_visible(title="",
#                                                         max_score="0",
#                                                         min_score="0",
#                                                         description="",
#                                                         estimated_time="")
#     #реализация без компонента CreateCourseFormComponent
#     # create_course_page.check_visible_create_course_form(
#     #     title="", max_score="0", min_score="0", description="", estimated_time=""
#     # )
#     create_course_page.create_course_exercises_toolbar_view.check_visible()
#     # реализовно в компоненте class CreateCourseExercisesToolbarViewComponent
#     # реализация без компонента class CreateCourseExercisesToolbarViewComponent
#     # create_course_page.check_visible_exercises_title()
#     # create_course_page.check_visible_create_exercises_button()
#     create_course_page.check_visible_exercises_empty_view()
#
#     create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
#     create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
#     create_course_page.create_course_form.fill(
#          title="Playwright",
#          max_score="100",
#          min_score="10",
#          description="Playwright",
#          estimated_time="2 weeks"
#     )
#     # реализация без компонента CreateCourseFormComponent
#     # create_course_page.fill_create_course_form(
#     #     title="Playwright",
#     #     max_score="100",
#     #     min_score="10",
#     #     description="Playwright",
#     #     estimated_time="2 weeks"
#     # )
#     # реализация без компонента CreateCourseToolbarViewComponent
#     # create_course_page.click_create_course_button()
#     create_course_page.create_course_toolbar_view.click_create_course_button()
#
#     courses_list_page.toolbar_view.check_visible()
#     # courses_list_page.check_visible_create_course_button()
#     courses_list_page.course_view.check_visible(
#         index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
#     )
