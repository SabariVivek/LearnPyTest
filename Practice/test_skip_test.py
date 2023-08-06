# test_skip_test.py
import pytest

"""
skip --> It is a inbuilt marker...c
"""


@pytest.mark.skip
def test_method_one():
    print("In Method 1...")


@pytest.mark.regression
def test_method_two():
    print("In Method 2...")


@pytest.mark.smoke
def test_method_three():
    print("In Method 3...")


@pytest.mark.skip
def test_method_four():
    print("In Method 4...")
