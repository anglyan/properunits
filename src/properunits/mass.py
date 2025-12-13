from .base import Magnitude

_mass_names = {
    'kg' : ['kilo'],
    'g' : ['gram'],
    'lb' : ['pound', 'lbs'],
    'oz' : ['ounce', 'ounces'],
    't' : ['tonne'],
    'Da' : ['u', 'amu']
}

_mass_conv = {
    'g' : lambda x: 1e-3*x,
    'lb' : lambda x: 0.45359237*x,
    'oz' : lambda x: 28.349523125e-3*x,
    't' : lambda x: 1e3*x,
    'Da' : lambda x: 1.66053906892e-27*x
}

class Mass(Magnitude):

    _unit = 'kg'

    def _convert(self, val, unit):
        key = self._check_unit(unit, _mass_names)
        if key == Mass._unit:
            self._x = val
        else:
            self._x = _mass_conv[key](val)

    @property
    def unit(self):
        return Mass._unit

    def list_units():
        return list(_mass_names.keys())
