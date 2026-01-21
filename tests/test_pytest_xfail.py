import pytest


@pytest.mark.xfail(reason = "Найден баг в приложении, из-за которого тест падает с ошибкой") # применяется если в приложении есть баг
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason = "Баг уже исправлен, но на тест все еще висит марктровка xfail" )
def test_without_bug():
    ...

