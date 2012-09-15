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

from lib.Bike.gearing import gear_assembly, wheel
from lib.Units.distance_units import inch
from lib.Units import Unit


class bike(object):

    def __init__(self):
        self._front_wheel = wheel(27)
        self._rear_wheel = wheel(27)

        self.gearing = gear_assembly()
        self.gearing.wheel = self._rear_wheel
        self.make = ""
        self.model = ""
        self.frame_num = ""
        self.year = ""

    def chainset(self, cass=None):
        if cass != None:
            self.gearing.front_assembly(cass)
        return self.gearing.front_rings

    def cassette(self, cass=None):
        if cass != None:
            self.gearing.rear_assembly(cass)
        return self.gearing.rear_rings

    def wheel_size(self, size):
        if isinstance(size, Unit):
            size = size.convert_to(inch)

        self._front_wheel = wheel(int(size))
        self._rear_wheel = wheel(int(size))
        self.gearing.wheel = self._rear_wheel

    def num_gears(self):
        return self.gearing.num_gears()
"""
module test
from gearing import *
b = bike()
b.cassette(cassette(11,13,15,18,21,24,28,32))
b.chainset(chainset(50,38))
b.gearing.to_string()
b.chainset(chainset(52,38))
b.gearing.to_string()
b.wheel_size(28)
b.gearing.to_string()
print b.num_gears(),"Speed bike"
"""
