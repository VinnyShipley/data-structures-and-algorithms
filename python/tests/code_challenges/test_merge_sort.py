import pytest
from code_challenges.merge_sort import merge_sort

def test_length_zero():
  arr = []
  actual = merge_sort(arr)
  expected = []
  assert actual == expected

def test_length_one():
  arr = [5]
  actual = merge_sort(arr)
  expected = [5]
  assert actual == expected

def test_non_repeat_list():
  arr = [5, 6, 4, 2, 1, 3]
  actual = merge_sort(arr)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected


def test_repeated_list():
  arr = [5, 5, 6, 4, 2, 1, 3]
  actual = merge_sort(arr)
  expected = [1, 2, 3, 4, 5, 5, 6]
  assert actual == expected
