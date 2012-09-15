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


class VolumeUnitGroup(UnitGroup):

    def __init__(self):
        super(VolumeUnitGroup, self).__init__('mass', 'm')
        self.definitions = [
            UnitDefinition('Cubic meter', 'm3', 1.0),
            UnitDefinition('Liter', 'l', 0.001),
            UnitDefinition('milliliter', 'ml', 1e-06),
            UnitDefinition('fluid ounce (UK)', 'floz', 2.84130625e-06),
            UnitDefinition('gallon (UK)', 'gal', 0.00454609),
            UnitDefinition('pint (UK)', 'pt', 0.000568261)
        ]

VolumeUnits = VolumeUnitGroup()
m3 = VolumeUnits.get_unit('m3')
liter = VolumeUnits.get_unit('l')
ml = VolumeUnits.get_unit('ml')
floz = VolumeUnits.get_unit('floz')
gal = VolumeUnits.get_unit('gal')
gallon = gal
pt = VolumeUnits.get_unit('pt')
pint = pt
base_unit = VolumeUnits.base_unit()
