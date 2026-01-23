import pytest


@pytest.fixture(autouse=True) # автоматически запускаяется на каждый тест по дефолту (если укажем scope="class" то будет запускаться на каждый class
def send_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')



@pytest.fixture(scope= 'session')  # запускается один раз на всю тестовую сессию
def settings():
    print('[SESSION] Инициализируем настройки автотестов')


@pytest.fixture(scope = 'class') # запускается один раз на тетовый класс
def user():
    print('[CLASS] Создаем данные пользователя один раз на тестовый класс')


@pytest.fixture(scope = 'function') #запускается один раз на всю тестовую функцию
def browser():
    print('[FUCTION] Открываем браузер на каждый автотест')


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...
    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...