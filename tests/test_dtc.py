import pytest

from app.dtc import is_valid_dtc


@pytest.mark.parametrize("code", ["P0301", "p0301", " C1234 ", "U3FFF"])
def test_valid_codes(code):
    assert is_valid_dtc(code) is True


@pytest.mark.parametrize("code", ["X0301", "P4301", "P031", "P03011", ""])
def test_invalid_codes(code):
    assert is_valid_dtc(code) is False
