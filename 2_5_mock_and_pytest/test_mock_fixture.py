import os
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_fixture():
    with patch("os.system") as mock:
        mock.return_value = "nope"
        yield

def test_mock_fixture(mock_fixture):
    assert "nope" == os.system("echo yes")

