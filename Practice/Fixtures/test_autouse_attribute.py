# test_autouse_attribute.py

"""
If we provide (autouse = true) in fixture method...
we don't want to give it as an argument in every method...
"""


def test_a():
    print("In Test A...")


def test_b():
    print("In Test B...")
