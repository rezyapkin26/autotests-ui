import  pytest
from _pytest.fixtures import SubRequest

# 1, 2, 3, -1

@pytest.mark.parametrize("number", [1, 2, 3, -1]) # параметризация для единичного аргумента
def test_numbers_1(number: int):
    print(f'Number: {number}')
    assert number > 0



@pytest.mark.parametrize("number, expected", [(1,1), (2, 4), (3, 9)])  # параметризация для нескольких аргументов. Number совпадает с первым числов в скодках, expected- совпадает со вторым числом.
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os',['Windows', 'Linux', 'Macos', 'Debian'] )  # Параметризация с преумножением. Запуск тестов на разных ос и браузерах одновременно
@pytest.mark.parametrize("browser", ['chromium', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])  # Параметризация фикстур. request.param => параметры из фикстуры
def browser(request):
    return request.param #request.param => параметры из фикстуры

def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara']) # Параметризация классов.
class TestOperations:
    @pytest.mark.parametrize('account,', ['Credit card', 'Debit card'])
    def test_users_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_users_without_operations(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+70000000000': 'User with money on bank account',
    '+71111111111': 'User without money on bank account',
    '+72222222222': 'User with operations on bank account',
}



@pytest.mark.parametrize(
    'phone_number',
     users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}') # контекстная функция

def test_identifiers(phone_number: str):
    ...