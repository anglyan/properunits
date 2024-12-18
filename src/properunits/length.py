from .base import Magnitude

_length_names = {
    'm' : ['meter'],
    'nm' : ['nanometers'],
    'A' : ['Angstroms'],
    'in' : ['inch', 'inches'],
    'mi' : ['mile', 'miles'],
    'yd' : ['yard', 'yards'],
    'ft' : ['foot', 'feet']
}

_length_conv = {
    'nm' : lambda x: 1e-9*x,
    'A' : lambda x: 1e-10*x,
    'in' : lambda x: 2.54e-2*x,
    'mi' : lambda x: 1609.34*x,
    'yd' : lambda x: 0.9144*x,
    'ft' : lambda x: 0.3048*x
}

_area_names = {
    'm2' : ['m^2'],
    'nm2' : ['nm^2'],
    'A2' : ['A^2'],
    'ha' : ['hectarea'],
    'ac' : ['acre']
}

_area_conv = {
    'nm2' : lambda x: 1e-18*x,
    'A2' : lambda x: 1e-20*x,
    'ha' : lambda x: 1e4*x,
    'ac' : lambda x: 4046.856*x
}

_volume_names = {
    'l' : ['liter', 'liters'],
    'cm3' : ['cm^3'],
    'm3' : ['m^3'],
    'gal' : ['gallons', 'gallon']
}

_volume_conv = {
    'l' : lambda x: 1e-6*x,
    'cm3' : lambda x: 1e-6*x,
    'gal' : lambda x: 3.785411784e-6*x
}


class Length(Magnitude):

    _units = 'm'

    def _convert(self, val, units):
        key = self._check_units(units, _length_names)
        if key == Length._units:
            self._x = val
        else:
            self._x = _length_conv[key](val)

    @property
    def units(self):
        return Length._units

    def list_units():
        return list(_length_names.keys())


class Area(Magnitude):

    _units = 'm2'

    def _convert(self, val, units):
        key = self._check_units(units, _area_names)
        if key == Area._units:
            self._x = val
        else:
            self._x = _area_conv[key](val)

    @property
    def units(self):
        return Area._units

    def list_units():
        return list(_area_names.keys())


class Volume(Magnitude):

    _units = 'm3'

    def _convert(self, val, units):
        key = self._check_units(units, _volume_names)
        if key == Volume._units:
            self._x = val
        else:
            self._x = _volume_conv[key](val)

    @property
    def units(self):
        return Volume._units

    def list_units():
        return list(_volume_names.keys())
