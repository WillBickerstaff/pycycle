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

from Units import UnitGroup, UnitDefinition


class MassUnitGroup(UnitGroup):

    def __init__(self):
        super(MassUnitGroup, self).__init__('mass', 'm')
        self.definitions = [
            UnitDefinition('kilogram', 'kg', 1.0),
            UnitDefinition('gram', 'g', 0.001),
            UnitDefinition('ounce', 'oz', 0.0283495231),
            UnitDefinition('pound', 'lb', 0.45359237),
            UnitDefinition('tonne', 't', 1000.0)
        ]

MassUnits = MassUnitGroup()
kg = MassUnits.get_unit('kg')
gram = MassUnits.get_unit('g')
oz = MassUnits.get_unit('oz')
ounce = oz
lb = MassUnits.get_unit('lb')
ton = MassUnits.get_unit('t')
base_unit = MassUnits.base_unit()
