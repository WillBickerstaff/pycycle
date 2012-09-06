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

from Units import Unit, UnitGroup, UnitDefinition
import re


class TimeUnitGroup(UnitGroup):

    def __init__(self):
        super(TimeUnitGroup, self).__init__('time', 't')
        self.definitions = [
            UnitDefinition('millisecond', 'ms', 0.001),
            UnitDefinition('second', 's', 1.0),
            UnitDefinition('minute', 'm', 60.0),
            UnitDefinition('hour', 'h', 3600.0),
            UnitDefinition('day', 'd', 86400.0)
        ]

TimeUnits = TimeUnitGroup()

millisecond = TimeUnits.get_unit('ms')
ms = millisecond
second = TimeUnits.get_unit('s')
sec = second
minute = TimeUnits.get_unit('m')
hour = TimeUnits.get_unit('h')
hr = hour
day = TimeUnits.get_unit('d')
base_unit = TimeUnits.base_unit()


class FormattedTime(TimeUnitGroup):

    def __init__(self, time_string=None):
        super(FormattedTime, self).__init__()
        self.__vals = []
        self._formattedTime = time_string
        for v in self.definitions:
            self.__vals.append(Unit(v, 0))
        if time_string != None:
            self.set_time(time_string)

    def set_time(self, new_time):
        """ Try and set a time based on what is passed. Tried to make this
            fairly loose on it's requirement, we can pass an int representing
            a number of second or a string with any non-digit as the separator.

            Any string pass will need to include all values, so:
            0,2,3,4 will be understood as 0 days, 2 hours, 3 minutes and
            4 seconds.  2,3,4 would be 2 days, 3 hours 4 minutes.

            The safest way to call this method is to pass an int representing
            the number of seconds required.

            Keyword Arguments:
            new_time -- The new representation of the time
        """
        # deal with times passed as int,
        # we assume these represent total seconds
        try:
            prob_sec = int(new_time)
            self.__vals.reverse()
            for segment in self.__vals:
                if prob_sec > 0:
                    segment.value = int(prob_sec / segment.factor)
                    prob_sec -= (segment.value * segment.factor)
            self.__vals.reverse()

        # otherwise we'll try and make sense of the string.
        # TODO: Make the regex smarter at pulling
        # out seperator characters and identifying what they mean
        except ValueError:
            # This regex just looks for any non digit and seperates there
            # we assume that the greatest is given first (d,h,m,s,ms)
            notdigit = re.compile(r'\D*')
            time_pattern = notdigit.split(new_time)
            time_pattern.reverse()
            for key, val in enumerate(time_pattern):
                if key <= len(self.definitions):
                    self.__vals[key].value = int(val)

    def to_string(self):
        """ Return a string representation of the time """
        time_string = []
        self.__vals.reverse()
        for key, segment in enumerate(self.__vals):
            if key != len(self.__vals) and key != 0:
                time_string.append(' ')

            if segment.symbol == 'ms':
                time_string.append("{0:03d}{1:s}".format(
                                    segment.value, segment.symbol))
            else:
                time_string.append("{0:02d}{1:s}".
                                    format(segment.value, segment.symbol))
        time_string = ''.join(time_string)

        self.__vals.reverse()
        return time_string
