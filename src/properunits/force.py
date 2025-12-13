from .base import Magnitude

_f_names = {
    'N' : ['Newton'],
    'dyn' : ['Dyne, dyne'],
    'lbf' : ['pound-force'],
    'pdl' : ['poundal']
}

_f_conv = {
    'dyn' : lambda x: 1e-5*x,
    'lbf' : lambda x: 4.448222*x,
    'pdl' : lambda x: 0.1382550*x
}

class Force(Magnitude):

    _unit = 'N'

    def _convert(self, val, unit):
        key = self._check_unit(unit, _f_names)
        if key == Force._unit:
            self._x = val
        else:
            self._x = _f_conv[key](val)

    @property
    def unit(self):
        return Force._unit

    def list_units():
        return list(_f_names.keys())
