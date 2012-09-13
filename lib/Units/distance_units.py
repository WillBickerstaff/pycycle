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


class DistanceUnitGroup(UnitGroup):

    def __init__(self):
        super(DistanceUnitGroup, self).__init__('distance', 'd')
        self.definitions = [
            UnitDefinition('meter', 'm', 1.0),
            UnitDefinition('kilometer', 'km', 1000.0),
            UnitDefinition('millimeter', 'mm', 0.001),
            UnitDefinition('centimeter', 'cm', 0.01),
            UnitDefinition('mile', 'mi', 1609.344),
            UnitDefinition('thou', 'mil', 0.0000254),
            UnitDefinition('feet', 'ft', 0.3048),
            UnitDefinition('inch', 'in', 0.0254)
        ]

DistanceUnits = DistanceUnitGroup()

meter = DistanceUnits.get_unit('m')
kilometer = DistanceUnits.get_unit('km')
km = kilometer
millimeter = DistanceUnits.get_unit('mm')
mm = millimeter
centimeter = DistanceUnits.get_unit('cm')
cm = centimeter
mile = DistanceUnits.get_unit('mi')
mi = mile
thou = DistanceUnits.get_unit('mil')
mil = thou
feet = DistanceUnits.get_unit('ft')
ft = feet
inch = DistanceUnits.get_unit('in')
base_unit = DistanceUnits.base_unit()
