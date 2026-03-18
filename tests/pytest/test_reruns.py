# для перезапуска тестов устанавливаем плагин pip install pytest-rerunfailures

import pytest
import random

PLATFORM = 'Windows'

@pytest.mark.flaky(reruns=3, reruns_delay=2) #reruns=3 - сколько раз перезапустится тест, reruns_delay=2 - интервал между перезапусками 2 секунды
def test_reruns():
    assert random.choice([True, False]) == True

@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_reruns_1(self):
        assert random.choice([True, False])

    def test_reruns_2(self):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition = PLATFORM == 'Windows' )
def test_rerun_with_condition():
    assert random.choice([True, False])