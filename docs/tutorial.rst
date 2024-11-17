Tutorial
========

``Properunits`` helps us to work with non SI units, providing a straightforward way
of converting them to SI units. This helps bring consistency to any downstream computations.

Installation
------------

Using ``pip``::

    pip install -U properunits

Basic usage
-----------

Let's start by importing a specific physical magnitude:

>>> from properunits import Temperature

The first thing that we can do is query which units are available:

>>> Temperature.list_units()
['C', 'K', 'F']

Here it shows that we have the option of using Celsius, Kelvin, or Farenheit.

Let's create an object:

>>> t = Temperature(200, 'C')
>>> 

We can now query the SI magnitude:

>>> t.x
473.15

And its units:

>>> t.units
'K'

Or remenber the original value:

>>> t.value
(200, 'C')

The key idea of ``properunits`` is that it returns a ``float`` value that can
be used elsewhere.

Magnitudes in properunits
-------------------------

Here is a table of the magnitudes and units supported by ``properunits``:

.. table:: Magnitudes and units in properunits
   :widths: auto

   =============  ======
   Magnitude      Units
   =============  ======
   Area           m2, nm2, A2, ha
   Energy         J, eV, cal, kWh, Btu
   Force          N, dyn, lbf, pdl
   Length         m, nm, A, in, mi, yd
   Mass           kg, g, lb, oz, t, Da
   Pressure       Pa, Torr, mTorr, atm, psi, ksi, bar
   Temperature    K, C, F
   Volume         m3, l, cm3
   =============  ======

More details TBD

