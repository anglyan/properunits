from .base import Magnitude

_T_names = {
    'C' : ['C', 'Celsius', 'Centigrades'],
    'K' : ['K', 'Kelvin'],
    'F' : ['F', 'Farenheit']
}

_T_conv = {
    'C' : lambda x: x + 273.15,
    'F' : lambda x: (x-32)/1.8
}

class Temperature(Magnitude):

    _unit = 'K'

    def _convert(self, val, unit):
        key = self._check_unit(unit, _T_names)
        if key == Temperature._unit:
            self._x = val
        else:
            self._x = _T_conv[key](val)

    @property
    def units(self):
        return Temperature._unit

    def list_units():
        return list(_T_names.keys())
