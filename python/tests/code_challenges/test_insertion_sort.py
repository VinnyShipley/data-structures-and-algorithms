import pytest
from code_challenges.insertion_sort import insertion_sort

def test_length_zero():
  arr = []
  actual = insertion_sort(arr)
  expected = []
  assert actual == expected

def test_length_one():
  arr = [5]
  actual = insertion_sort(arr)
  expected = [5]
  assert actual == expected

def test_non_repeat_list():
  arr = [5, 6, 4, 2, 1, 3]
  actual = insertion_sort(arr)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected


def test_repeated_list():
  arr = [5, 5, 6, 4, 2, 1, 3]
  actual = insertion_sort(arr)
  expected = [1, 2, 3, 4, 5, 5, 6]
  assert actual == expected
