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

from lib.Units.distance_units import base_unit as dist_base
from lib.Units.speed_units import base_unit as speed_base
from lib.Units.time_units import base_unit as time_base
from lib.Units import Unit


class CalcError(Exception):

    def __init__(self, s, t, d):
        err_str = "Can't complete caclulation too few parameters given, "
        err_str += "speed={0:2f}, distance={1:2f} time={3:2f}".format(s, d, t)
        print err_str


class std(object):

    def __init__(self):
        self.speed = Unit(speed_base)
        self.distance = Unit(dist_base)
        self.time = Unit(time_base)

    def calc(self):
        """ Calculate the unset value """

        # Calculate speed
        if self.speed.value == 0:
            if self.distance.value > 0 and self.time.value > 0:
                s = Unit(speed_base,
                        self.distance.convert_to_base() /
                        self.time.convert_to_base())
                self.speed.value = s.convert_to(self.speed)
                return self.speed
            else:
                raise CalcError(self.speed.value, self.time.value,
                                self.distance.value)

        # Calculate distance
        if self.distance.value == 0:
            if self.speed.value > 0 and self.time.value > 0:
                d = Unit(dist_base,
                        self.time.convert_to_base() /
                        self.speed.convert_to_base())
                self.distance.value = d.convert_to(self.distance)
                return self.distance
            else:
                raise CalcError(self.speed.value, self.time.value,
                                self.distance.value)

        # Calculate time
        if self.time.value == 0:
            if self.speed.value > 0 and self.distance.value > 0:
                t = Unit(time_base,
                        self.distance.convert_to_base() /
                        self.speed.convert_to_base())
                self.time.value = t.convert_to(self.time)
                return self.time
            else:
                raise CalcError(self.speed.value, self.time.value,
                                self.distance.value)
