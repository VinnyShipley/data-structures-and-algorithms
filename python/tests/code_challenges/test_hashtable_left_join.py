import pytest
from code_challenges.hashtable_left_join import left_join
from data_structures.hashtable import Hashtable


def test_exists():
    assert left_join


def test_example():
    table_a = Hashtable()
    table_b = Hashtable()

    table_a.set('diligent', 'employed')
    table_a.set('fond', 'enamored')
    table_a.set('guide', 'usher')
    table_a.set('outfit', 'garb')
    table_a.set('wrath', 'anger')

    table_b.set('diligent', 'idle')
    table_b.set('fond', 'averse')
    table_b.set('guide', 'follow')
    table_b.set('flow', 'jam')
    table_b.set('wrath', 'delight')

    expected = [
        ["diligent", "employed", "idle"],
        ["outfit", "garb", None],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["wrath", "anger", "delight"]
    ]

    actual = left_join(table_a, table_b)

    assert actual == expected




# #@pytest.mark.skip("TODO")
# def test_example():
#     synonyms = {
#         "diligent": "employed",
#         "fond": "enamored",
#         "guide": "usher",
#         "outfit": "garb",
#         "wrath": "anger",
#     }
#     antonyms = {
#         "diligent": "idle",
#         "fond": "averse",
#         "guide": "follow",
#         "flow": "jam",
#         "wrath": "delight",
#     }

#     expected = [
#         ["fond", "enamored", "averse"],
#         ["wrath", "anger", "delight"],
#         ["diligent", "employed", "idle"],
#         ["outfit", "garb", "NONE"],
#         ["guide", "usher", "follow"],
#     ]

#     actual = left_join(synonyms, antonyms)

#     assert actual == expected


