# test_soft_asserts.py

"""
Have to install --> pip install pytest-soft-assertions
To Execute single file --> pytest FILE_NAME --soft--asserts
To Execute all files --> pytest --soft--asserts
"""


def test_one():
    print("I am the test one...")
    assert False


def test_two():
    print("I am the test two...")
    assert False


def test_three():
    print("I am the test three...")
