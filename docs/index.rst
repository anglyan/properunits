.. properunits documentation master file, created by
   sphinx-quickstart on Sat Nov 16 16:12:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Properunits documentation
=========================

A simple framework to work with physical magnitudes


Motivation
----------

``Properunits`` does one simple job: it helps
you define physical magnitudes in Python using units
and automatically convert them to SI units so that
downstream calculations are all done consistently.

``Properunits`` does not attempt to do universal unit conversion
or tries to implement operations that preserve and transform
the units. It is meant to extract numerical values that can
be used anywhere without having to worry about unit conversion.


Status
------

Properunits is still in development. Please check the documentation.


Quick install
-------------

Through pypi::

   pip install properunits


Usage
-----

::

   from properunits import Temperature, Pressure

   T = Temperature(100, 'C')
   p = Pressure(1, 'bar')

   print(T.x, p.x) # Return value in SI units.


Copyright and license
---------------------

Properunits is distributed under the terms of MIT License. 


Table of contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tutorial
   

