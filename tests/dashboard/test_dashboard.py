from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories
from allure_commons.types import Severity
from tools.routes import AppRoute

@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.DASHBOARD, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')  #Проверьте отображение страницы dashboard
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible('username')

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_activities_chart()

# реализация без тестового класса
# def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
#     dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
#
#     dashboard_page_with_state.sidebar.check_visible()
#     dashboard_page_with_state.navbar.check_visible('username')
#
#
#     dashboard_page_with_state.dashboard_toolbar_view.check_visible()
#     dashboard_page_with_state.check_visible_students_chart()
#     dashboard_page_with_state.check_visible_scores_chart()
#     dashboard_page_with_state.check_visible_courses_chart()
#     dashboard_page_with_state.check_visible_activities_chart()
#
