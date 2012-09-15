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

from lib.Units import UnitGroup, UnitDefinition


class SpeedUnitGroup(UnitGroup):

    def __init__(self):
        super(SpeedUnitGroup, self).__init__('velocity', 'v')
        self.definitions = [
            UnitDefinition('Meter/second', 'ms', 1.0),
            UnitDefinition('Kilometer/hour', 'kmh', 0.277777778),
            UnitDefinition('Mile/hour', 'mih', 0.44704),
            UnitDefinition('Knot', 'kn', 0.51477333),
            UnitDefinition('Mach', 'Mach', 295.0464)
        ]

SpeedUnits = SpeedUnitGroup()

ms = SpeedUnits.get_unit('ms')
kmh = SpeedUnits.get_unit('kmh')
mih = SpeedUnits.get_unit('mih')
knot = SpeedUnits.get_unit('kn')
mach = SpeedUnits.get_unit('Mach')
base_unit = SpeedUnits.base_unit()
