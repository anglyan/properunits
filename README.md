# Properunits
A simple framework to work with physical magnitudes


## Motivation

Properunits does one simple job: it helps
you define physical magnitudes in Python using units
and automatically convert them to SI units so that
downstream calculations are all done consistently.

Properunits does not attempt to do universal unit conversion
or tries to implement operations that preserve and transform
the units. It is meant to extract numerical values that can
be used anywhere without having to worry about unit conversion.


## Status

Properunits is still in development. Please check spikelearn's
documentation in [readthedocs]


## Quick install

Through pypi:

```
pip install properunits
```

## Usage

```
from properunits import Temperature, Pressure

T = Temperature(100, 'C')
p = Pressure(1, 'bar')

print(T.x, p.x) # Return value in SI units.
```

## Copyright and license

Properunits is distributed under the terms of MIT License. 

