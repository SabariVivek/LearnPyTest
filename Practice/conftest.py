# conftest.py
import pytest


@pytest.fixture(autouse=False, scope="function")
def login_logout():
    print("Launching the URL")
    print("Login into an application")
    yield
    print("Logging out from the application")
    print("Closing the browser")
