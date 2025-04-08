import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from stuff.calc import Calculator

@pytest.fixture
def calculator():
    return Calculator()

print("DONE with the tests")

