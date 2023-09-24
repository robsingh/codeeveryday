import inspect

from day1 import calculate_sum

def test_sum_numbers_default_args():
    assert calculate_sum() == 5050
    assert calculate_sum(numbers=None) == 5050


def test_sum_numbers_various_inputs():
    assert calculate_sum(range(1,11)) == 55
    assert calculate_sum([1,2,3]) == 6
    assert calculate_sum([1,2,3]) == 6
    assert calculate_sum([]) == 0