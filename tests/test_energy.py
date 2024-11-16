from properunits import Energy
import pytest


def test_precursor():
    en = Energy(100, 'BTU')
    assert en.x == pytest.approx(1.0551e5)

    