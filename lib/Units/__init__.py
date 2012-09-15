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

from fractions import Fraction


class UnitGroup(object):

    def __init__(self, name=None, symbol=None):
        self.category_name = name
        self.category_symbol = symbol
        self.definitions = []

    def get_unit(self, required_unit):
        """ Return a unit object where the name or symbol matches
            Keyword Arguments:
            required_unit -- A string that represents the name or symbol of
                             the unit we are looking for
        """

        for key, val in enumerate(self.definitions):
            if val.name == required_unit or val.symbol == required_unit:
                return Unit(self.definitions[key])

    def base_unit(self):
        """ Returns the base unit, the base unit is whichever unit has a
            factor of 1.0.
        """

        for key, val in enumerate(self.definitions):
            if val.factor == 1.0:
                return Unit(self.definitions[key])


class UnitDefinition(object):

    def __init__(self, name, symbol, factor=1.0):
        self.factor = factor
        self.symbol = symbol
        self.name = name

    def is_base(self):
        """ Return a boolean that indicates if the unit is the base unit
            (has a factor of 1.0) or not.
        """
        if self.factor == 1.0:
            return True
        else:
            return False


class Unit(UnitDefinition):

    def __init__(self, unit_definition, value=0):
        self.value = value
        super(Unit, self).__init__(unit_definition.name,
                                  unit_definition.symbol,
                                  unit_definition.factor)

    def convert_to_base(self):
        """ Convert the unit value to the base value and return as a float """
        return self.value * self.factor

    def convert_to(self, new_unit_definition):
        """ Convert the unit to the given unit and return the value as a float

            Keyword Arguments:
            new_unit_definition -- A unit object that represents the target
                                   unit
        """
        return self.convert_to_base() / new_unit_definition.factor

    def to_string(self):
        """ return a string representation of the object """
        return "{0:f} {1:s} ({2:s})".format(self.value, self.symbol, self.name)

    def as_fraction(self):
        """ Return a string that represents the unit as a fraction """

        return_string = []
        if int(self.value) > 0:
            return_string.append(str(int(self.value)))
            return_string.append(' ')

        return_string.append(str(Fraction.from_float(self.value % 1). \
                        limit_denominator(1024)))

        return ''.join(return_string)
