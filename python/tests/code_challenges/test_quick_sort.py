import pytest
from code_challenges.quick_sort import quick_sort



def test_length_zero():
  arr = []
  actual = quick_sort(arr, 0, len(arr)-1)
  expected = []
  assert actual == expected

def test_length_one():
  arr = [5]
  actual = quick_sort(arr, 0, len(arr)-1)
  expected = [5]
  assert actual == expected

def test_non_repeat_list():
  arr = [5, 6, 4, 2, 1, 3]
  actual = quick_sort(arr, 0, len(arr)-1)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected


def test_repeated_list():
  arr = [5, 5, 6, 4, 2, 1, 3]
  actual = quick_sort(arr, 0, len(arr)-1)
  expected = [1, 2, 3, 4, 5, 5, 6]
  assert actual == expected
