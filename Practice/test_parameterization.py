# test_parameterization.py
import pytest


@pytest.mark.parametrize("username, password",
                         [("Sabari", "Sabari@123"), ("Mukesh", "Mukesh@123"), ("Rajesh", "Rajesh@123")])
def test_method_one(username, password):
    print(username + " : " + password)
