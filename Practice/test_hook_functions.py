# test_hook_functions.py

"""
It is an alternate method of fixtures...
    * setup_function(function)
    * teardown_function(function)
    * setup_module(function)
    * teardown_module(module)
"""


def setup_module(function):
    print("Extent Report Initialized")


def teardown_module(function):
    print("Extent Report Flushed Out")


def setup_function(function):
    print("Browser Launched")


def teardown_function(function):
    print("Browser Closed")


def test_method_one():
    print("I am in Test Method One")


def test_method_two():
    print("I am in Test Method Two")
