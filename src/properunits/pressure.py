from .base import Magnitude

_p_names = {
    'Pa' : ['Pa', 'Pascal', 'Pascals'],
    'Torr' : ['Torr', 'torr', 'Torrs'],
    'mTorr' : ['mTorr', 'mtorr'],
    'atm' : ['atm', 'Atm', 'Atmos'],
    'psi' : ['PSI', 'Psi'],
    'ksi' : ['KSI'],
    'bar' : ['bar', 'Bar', 'bars']
}

_p_conv = {
    'Torr' : lambda x: 133.322*x,
    'mTorr' : lambda x: 0.133322*x,
    'atm' : lambda x: 101325*x,
    'psi' : lambda x: 6.894757e3*x,
    'ksi' : lambda x: 6.894757e6*x,
    'bar' : lambda x: 1e5*x
}

class Pressure(Magnitude):

    _unit = 'Pa'

    def _convert(self, val, unit):
        key = self._check_unit(unit, _p_names)
        if key == Pressure._unit:
            self._x = val
        else:
            self._x = _p_conv[key](val)

    @property
    def unit(self):
        return Pressure._unit
    
    def list_units():
        return list(_p_names.keys())


