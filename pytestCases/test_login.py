import pytest

""" Login test cases
 Understanding the pytest framework
pytest - x  # stop after first failure
pytest to run the scripts in the file
pytest test_login.py --> pytest to run the scripts in the specific file
pytest test_login.py -s -v --> to print the print statement of the tests
# pytest - -maxfail = 2  # stop after two failures
# pytest --pdb
 """


def test_login():
    # driver.get("http:")
    print("Running the first test case")
    print("Logging in")

    # In the command line enter pytest to execute the tests one after the other
    # pytest to run the


def test_logout():
    print("Running the second test case")
    print("Logging out")
    # Added failure line to fail the TC
    var = 2 == 5
    assert var == True
    # To debug the failure
    # pytest - x  # stop after first failure
    # pytest - -maxfail = 2  # stop after two failures
    # pytest --pdb


def test_login_as():
    print("Running the third test case")
    print("Logging as Thrilling_Hero")
    print("I love Python Programming ")
