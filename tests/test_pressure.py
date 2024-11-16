from properunits import Pressure
import pytest


def test_precursor():
    p = Pressure(100, 'bar')
    assert p.x == pytest.approx(1e7)

    