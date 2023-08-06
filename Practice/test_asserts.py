# test_asserts.py

def test_assert_one():
    a = 10
    b = 20
    assert a == b, "The value is not equal"


def test_assert_two():
    a = "Sabari"
    b = "Sabari"
    assert a.__eq__(b), "Two names are not equal"
