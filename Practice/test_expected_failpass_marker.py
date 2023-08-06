# test_expected_failpass_marker.py
import pytest


@pytest.mark.xfail
def test_method_one():
    print("In Method 1...")
    assert False


@pytest.mark.xfail
def test_method_two():
    print("In Method 2...")


@pytest.mark.xfail
def test_method_three():
    print("In Method 3...")
    assert False


@pytest.mark.xfail
def test_method_four():
    print("In Method 4...")
