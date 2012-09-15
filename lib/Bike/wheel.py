#! /usr/bin/env python

# Copyright 2010 Will Bickerstaff
# This file is part of PyCycle.
#
# PyCycle is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# PyCycle is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# PyCycle. If not, see http://www.gnu.org/licenses/.

from math import pi

from lib.Units import Unit
from lib.Units.distance_units import inch
from lib.Units.speed_units import kmh
from lib.Units.time_units import minute
from lib.Calc.std_calc import std


class wheel(object):

    def __init__(self, rim_size=26):
        self.rim_size = Unit(inch, rim_size)
        self.circ = self._rolling_distance()
        self.speed = Unit(kmh)

    def _rolling_distance(self):
        """ Return a float that represents the circumference of the wheel """
        return Unit(inch, self.rim_size.value * pi)

    def act_speed(self, rpm=60, pref_unit=kmh):
        """ Return a speed unit that represents the travelling speed when
            turned at the given rpm.

            Keyword Arguments:
            rpm -- The rpm the wheel is turning (default 60)
            pref_unit -- The desired speed unit to be returned
        """
        self.circ = self._rolling_distance()
        calc = std()
        calc.speed = Unit(pref_unit)
        calc.distance = self.circ
        calc.distance.value *= rpm
        calc.time = (Unit(minute, 1))
        calc.calc()
        self.speed = calc.speed
        return self.speed
