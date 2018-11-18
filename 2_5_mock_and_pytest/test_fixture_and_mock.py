import os
import pytest
from unittest.mock import patch

@pytest.fixture
def fixture():
    print("Fixture executed")

    
@patch("os.system")
def test_right_order(mock, fixture):
    pass
