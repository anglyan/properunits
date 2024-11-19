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
   Area           m2, nm2, A2, ha, ac
   Energy         J, eV, cal, kWh, Btu
   Force          N, dyn, lbf, pdl
   Length         m, nm, A, in, mi, yd, ft
   Mass           kg, g, lb, oz, t, Da
   Pressure       Pa, Torr, mTorr, atm, psi, ksi, bar
   Temperature    K, C, F
   Volume         m3, l, cm3, gal(US)
   =============  ======

Working with arrays
-------------------

``properunits`` can also work with matrices and arrays:

>>> import numpy as np
>>> t = np.arange(0,200,10)
>>> t
array([  0,  10,  20,  30,  40,  50,  60,  70,  80,  90, 100, 110, 120,
       130, 140, 150, 160, 170, 180, 190])
>>> t_k = Temperature(t, 'C')
>>> t_k.x
array([273.15, 283.15, 293.15, 303.15, 313.15, 323.15, 333.15, 343.15,
       353.15, 363.15, 373.15, 383.15, 393.15, 403.15, 413.15, 423.15,
       433.15, 443.15, 453.15, 463.15])
>>> 


