import pytest
from insertion_sort import insertion_sort

def test_sample_case(sample_array):
    assert insertion_sort(sample_array) == [4,8,15,16,23,42]
    
def test_reverse_sorted(reverse_sorted):
    assert insertion_sort(reverse_sorted) == [-2,5,8,12,18,20]

def test_few_uniques(few_uniques):
    assert insertion_sort(few_uniques) == [5,5,5,7,7,12]

def test_nearly_sorted(nearly_sorted):
    assert insertion_sort(nearly_sorted) == [2,3,5,7,11,13]

@pytest.fixture
def sample_array():
    return [8,4,23,42,16,15]

@pytest.fixture  
def reverse_sorted():
    return [20,18,12,8,5,-2]

@pytest.fixture  
def few_uniques():
    return [5,12,7,5,5,7]

@pytest.fixture  
def nearly_sorted():
    return [2,3,5,7,13,11]