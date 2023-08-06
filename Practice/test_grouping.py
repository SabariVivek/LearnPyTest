# test_grouping.py

"""
To execute this --> pytest test_grouping.py -rA -m "smoke"
"""


def test_method_one(login_logout):
    print("In Method 1...")


def test_method_two(login_logout):
    print("In Method 2...")
