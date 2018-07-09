import pytest

import sample


@pytest.fixture
def dummy_value():
    return 1


def test_some_function(dummy_value):
    assert sample.some_function() == dummy_value

