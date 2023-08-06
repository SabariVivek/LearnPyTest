# test_user_defined_marker.py
import pytest

"""
To execute the marker --> pytest -rA -m "smoke"
                      --> pytest -rA -m "smoke or regression" --> But we will be getting warning...
                      
To overcome the issue, we have to create pytest.ini file...
"""


@pytest.mark.smoke
def test_method_one():
    print("In Method 1...")


@pytest.mark.regression
def test_method_two():
    print("In Method 2...")


@pytest.mark.smoke
def test_method_three():
    print("In Method 3...")


@pytest.mark.regression
def test_method_four():
    print("In Method 4...")
