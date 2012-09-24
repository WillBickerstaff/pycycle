#! /usr/bin/env python

# Copyright 2011 Will Bickerstaff
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

import string

from lib.Bike.wheel import wheel
from lib.Units.speed_units import kmh
from lib.Units import Unit


class gear_ring(object):

    def __init__(self, num_teeth=12, man="", part_num=""):
        self.teeth = num_teeth
        self.manufacturer = man
        self.part_num = part_num

    def to_string(self):
        """ Return a string representation of the gear_ring object """

        s = []
        if self.manufacturer != "" or self.part_num != "":
            s.append(",")
        if self.manufacturer != "":
            s.append(self.manufacturer)
        if self.part_num != "":
            s.append(" {0:<s}".format(self.part_num))
        s.append('{0:d} teeth'.format(self.teeth))
        return ''.join(s)


class chain_ring(gear_ring):

    def __init__(self, **kwargs):
        num_teeth = 50
        pcd = 130
        mounts = 4
        man = ""
        pn = ""

        for k in kwargs:
            if k == "num_teeth" or k == "teeth":
                num_teeth = kwargs[k]
            if k == "bcd" or k == "pcd":
                pcd = kwargs[k]
            if k == "mounts" or k == "bolt":
                mounts = kwargs[k]
            if k == "man" or k == "manufacturer":
                man = kwargs[k]
            if k == "pn" or k == "part_num":
                pn = kwargs[k]

        gear_ring.__init__(self, num_teeth, man, pn)
        self.pcd = pcd
        self.mounts = mounts
        self.manufacturer = man
        self.part_num = pn

    def to_string(self):
        """ Return a string representation of the chain_ring object """
        return "{0:<s} - {1:d}pcd, {2:d} bolt".format(
                super(chain_ring, self).to_string(), self.pcd, self.mounts)


class cassette(object):

    def __init__(self, *args):
        self.manufacturer = ""
        self.part_num = ""
        self.rings = []

        for v in args:
            self.add_rings(v)

    def clear_rings(self):
        self.manufacturer = ""
        self.part_num = ""
        self.rings = []

    def add_rings(self, *rings):
        """ Add rings to the collection, rings can be supplied as int to
            represent the number of teeth on a ring or as complete
            gear_ring objects

            Arguments:
            rings -- Any number of gear_ring objects, or int representing
                     gear ring teeth

        """

        for new_ring in rings:
            if not isinstance(new_ring, gear_ring):
                new_ring = gear_ring(new_ring)

            # If a ring with the same number of teeth exists, then we will
            # replace it with the newly defined ring.
            ring_index = self.ring_exists(new_ring)
            if ring_index >= 0:
                self.rings[ring_index] = new_ring
            else:
                self.rings.append(new_ring)

        self.sort_ascending()

    def ring_exists(self, ring):
        """ Finds the index of the given ring and returns it. Returns -1 if
            the ring does not exist. Ring can be either a gear_ring object
            or an int representing the number of teeth.

            Keyword Arguments:
            ring -- A gear_ring object or an int representing the number of
                    teeth on the ring we are looking for

        """

        if isinstance(ring, gear_ring):
            ring = ring.teeth

        exists = -1

        for key, val in enumerate(self.rings):
            if val.teeth == ring:
                exists = key
                break

        return exists

    def sort_ascending(self):
        """ Sorts the rings into  ascending (by number of teeth) order. """

        num_gears = len(self.rings)

        for cur_ring in range(0, num_gears - 1):
            maxat = cur_ring
            maximum = self.rings[cur_ring].teeth

            for next_ring in range(cur_ring + 1, num_gears):
                if maximum < self.rings[next_ring].teeth:
                    maxat = next_ring
                    maximum = self.rings[next_ring].teeth

            temp = self.rings[cur_ring]
            self.rings[cur_ring] = self.rings[maxat]
            self.rings[maxat] = temp

    def sort_descending(self):
        """ Sorts the rings into  descending (by number of teeeth) order. """
        self.sort_ascending()
        self.rings.reverse()

    def list_rings(self):
        """Return a string representing all rings."""

        return_string = []
        for val in self.rings:
            return_string.append('{0:s}\n'.format(val.to_string()))

        return ''.join(return_string)

    def num_gears(self):
        """Returns an int representing the number of gear_rings on
            this cassette

        """

        return len(self.rings)

    def to_string(self):
        """ return a string representation of this cassette """
        return "{0:02d} speed {1:<s} {2:<s}\n\n{3:<s}".format(
        len(self.rings), self.manufacturer, self.part_num, self.list_rings())

    def change_ring_at_pos(self, position, new_ring):
        """ Swap a ring at the given position with the newly defined ring

            Keyword arguments:
            position -- The position of the ring we want to swap
            new_ring -- Either a gear_ring object representing the new
                        ring or an int representing the number of teeth
                        on the new ring

        """

        if not isinstance(new_ring, gear_ring):
            new_ring = gear_ring(new_ring)

        self.rings[position] = new_ring

    def swap_ring(self, old_ring, new_ring):
        """ Swap given ring with a  new one.

            rings can either be gear_ring objects, or an int representing the
            number of teeth on the ring. If two rings exist with the same
            number of teeth then the first one on the cassette is swapped

            Keyword Arguments:
            old_ring -- The representation ofthe ring to be swapped
            new_ring -- The representation of the ring that will take the
                        place of old_ring

        """

        pos = self.ring_exists(old_ring)
        if pos >= 0:
            self.change_ring_at_pos(pos, new_ring)


class chainset(cassette):

    def __init__(self, *args):

        cassette.__init__(self, *args)
        self._pcd = 130
        self._mounts = 5
        if len(args) > 0:
            for v in args:
                self.add_rings(v)

        self.pcd(self._pcd)
        self.mounts(self._mounts)

    def clear_rings(self):
        self._pcd = 130
        self._mounts = 5
        cassette.clear_rings()

    # Overrides the parent method because we want chain_rings instead of
    # gear_rings
    def add_rings(self, *rings):
        """ Add rings to the collection, rings can be supplied as int to
            represent the number of teeth on a ring or as complete
            gear_ring objects

            Arguments:
            rings -- Any number of gear_ring objects, or int representing
                     gear ring teeth

        """

        for ring in rings:
            new_ring = self._make_chain_ring(ring)
            ring_index = self.ring_exists(new_ring)
            if ring_index >= 0:
                self.rings[ring_index] = new_ring
            else:
                self.rings.append(new_ring)

        self.sort_descending()

    def _make_chain_ring(self, ring_from):
        """ Convert a gear_ring object or int representing the number of teeth
            to a chain_ring object.

            Keyword Arguments:
            ring_from -- Either the gear_ring to be converted or an int
                         representing the number of teeth

        """
        if isinstance(ring_from, gear_ring):
            new_ring = chain_ring(num_teeth=ring_from.teeth)
            new_ring.maufacturer = ring_from.manufacturer
            new_ring.part_num = ring_from.part_num
            if isinstance(ring_from, chain_ring):
                new_ring.pcd = ring_from.pcd
                self.pcd(new_ring.pcd)
                new_ring.mounts = ring_from.mounts
                self.mounts(new_ring.mounts)
            else:
                new_ring.pcd = self._pcd
                new_ring.mounts = self._mounts

        else:
            new_ring = chain_ring(num_teeth=ring_from, pcd=self.
                                 _pcd, mounts=self._mounts)

        return new_ring

    def pcd(self, pcd=None):
        """ Set the pcd of the chainset, doing so will alter the pcd of all
            chain_ring objects in the chainset.  Returns the current pcd as
            an int

            Keyword Arguments:
            pcd -- Optional argument to define a new pcd

        """

        if pcd != None:
            self._pcd = pcd
            for k in range(len(self.rings) - 1):
                self.rings[k].pcd = self._pcd

        return self._pcd

    def mounts(self, mounts=None):
        """ Set the number of mount bolts on the chainset, doing so will
            also alter the number of mount bolts on all chain_ring objects in
            the chainset.  Returns the current number of mounts as an int

            Keyword Arguments:
            mounts -- Optional argument to define a new number of mount bolts

        """
        if mounts != None:
            self._mounts = mounts
            for k in range(len(self.rings) - 1):
                self.rings[k].mounts = self._mounts

        return self._mounts

    def to_string(self):
        """ Return a string representation of the chainset object """

        d = super(chainset, self).to_string()
        return "{0:<s}\n{1:d} pcd {2:d} bolt".format(
                    d, self.pcd(), self.mounts())


class gear_assembly(object):

    def __init__(self):
        self.wheel = wheel()
        self.front_rings = chainset()
        self.rear_rings = cassette()

    def _build_ring(self, num_teeth, manufacturer="", part_num=""):
        """ Build a gear_ring ready for adding to either the cassette or
            chainset.  Returns a gear_ring object

            Keyword Arguments:
            num_teeth -- Either an int representing the number of teeth on the
                         ring or a gear_ring object
            manufacturer -- Optional string representing the manufacturers
                            name (default "")
            part_num -- Optional string representing the ring part number
                        (default "")
        """

        if isinstance(num_teeth, gear_ring):
            ring = num_teeth
        else:
            ring = gear_ring(int(num_teeth))
            ring.manufacturer = manufacturer
            ring.part_num = part_num
        return ring

    def add_front_ring(self, num_teeth, manufacturer="", part_num=""):
        """ Adds a ring to the chainset

            Keyword Arguments:
            num_teeth -- Either an int representing the number of teeth on the
                         ring or a gear_ring object
            manufacturer -- Optional string representing the manufacturers
                            name (default "")
            part_num -- Optional string representing the ring part number
                        (default "")
        """

        ring = self._build_ring(num_teeth, manufacturer, part_num)
        self.front_rings.add_rings(ring)
        self.front_rings.sort_descending()

    def add_rear_ring(self, num_teeth, manufacturer="", part_num=""):
        """ Adds a ring to the cassette

            Keyword Arguments:
            num_teeth -- Either an int representing the number of teeth on the
                         ring or a gear_ring object
            manufacturer -- Optional string representing the manufacturers
                            name (default "")
            part_num -- Optional string representing the ring part number
                        (default "")
        """

        ring = self._build_ring(num_teeth, manufacturer, part_num)
        self.rear_rings.add_rings(ring)

    def gear_inch(self, front_ring, rear_ring):
        front_ring = self._ring_teeth(front_ring)
        rear_ring = self._ring_teeth(rear_ring)

        return (float(front_ring) / rear_ring) * self.wheel.rim_size.value

    def rear_assembly(self, assembly):
        """ Add a complete gear assembly as the cassette

            Keyword Arguments:
            assembly -- A complete cassette object
        """
        if isinstance(assembly, cassette):
            self.rear_rings = assembly

    def front_assembly(self, assembly):
        """ Add a complete gear assembly as the chainset

            Keyword Arguments:
            assembly -- A complete chainset object
        """
        if isinstance(assembly, chainset):
            self.front_rings = assembly
            self.front_rings.rings.reverse()

    # This is only here so as we can loop through each assembly passing
    # the ring here to get its number of teeth.
    #
    # TODO: Check if this is really needed, can't we just grab it from the
    # rings teeth attribute
    def _ring_teeth(self, ring):
        """ Get the number of teeth on the given ring

            Keyword Arguments:
            ring -- the gear_ring or chain_ring object for which we want the
                    number of teeth
        """
        if isinstance(ring, gear_ring):
            return ring.teeth
        else:
            return ring

    # If the default is changed from kmh, make sure to import the correct unit
    def speed(self, front_ring, rear_ring, cadence=60, pref_unit=kmh):
        """ Returns a speed_unit representing the achievable speed with
            the given arguments.

            Keyword arguments:
            front_ring -- A gear_ring or chain_ring object
            rear_ring -- A gear_ring or chain_ring object
            cadence -- Optional cadence argument (default 60)
            pref_unit -- the preferred rseulting speed unit.  Must be a
                         speed_unit object as defined in speed_units
                         (default kmh)
        """
        front_ring = self._ring_teeth(front_ring)
        rear_ring = self._ring_teeth(rear_ring)
        rpm = (float(front_ring) / rear_ring) * cadence
        speed = self.wheel.act_speed(rpm)
        speed = Unit(pref_unit, speed.convert_to(pref_unit))
        return speed

    def num_gears(self):
        """ Returns an int representing the total number of gears """

        return self.rear_rings.num_gears() * self.front_rings.num_gears()

    # Everything below here is for formatting the object as a string
    # representation
    def __table_cadences(self, start_cadence, end_cadence=120,
                        required_cadence=0, qty=5):

        cadence_increase = ((end_cadence) - start_cadence) / (qty - 1.0)
        if required_cadence != 0:
            return start_cadence + (cadence_increase * required_cadence)
        else:
            cadences = []
            current_cadence = 0
            while current_cadence < qty:
                cadences.append(start_cadence +
                                (cadence_increase * current_cadence))
                current_cadence += 1
            return cadences

    def __table_head(self, cadences, speed_unit=kmh):
        head_string = []
        head_string.append("With {0:d}{1:<s} wheel.\n".format(
                    self.wheel.rim_size.value, self.wheel.rim_size.symbol))
        # Placeholder for the table top line, length needs calculating
        # after we've processed everything
        head_string.append("")
        cadence_heading = "{0:s} @ Cadence".format(speed_unit.symbol)
        head_string.append(
                    "\n|{0:>6}|{0:<10}|{0:>10}|{1:^8}|{2:^{3}}|\n".format(
                    '', 'Gear', cadence_heading, (len(cadences) * 7) - 1))
        head_string.append("|{0:^6}|{1:^10}|{2:^10}|{3:^8}|".format(
                        'Gear', 'Front', 'Rear', 'Inches'))

        for cadence_key in range(len(cadences) - 1):
            head_string.append("{0:^6d}|".format(int(cadences[cadence_key])))
        head_string.append('\n')
        # Now we can get the length of the top line
        head_string[1] = "-" * self.__table_width(head_string)

        return ''.join(head_string)

    def __html_table_head(self, cadences, speed_unit=kmh):
        head_string = []
        head_string.append("\n<table>\n\t<caption>Analysis with "
                           "{0:d}{1:<s} wheel.</caption>\n\n\t<tr>".format(
                    self.wheel.rim_size.value, self.wheel.rim_size.symbol))

        cadence_heading = "{0:s} @ Cadence".format(speed_unit.symbol)

        head_string.append(self.__td('Gear', 2, 0, True))
        head_string.append(self.__td('Front', 2, 0, True))
        head_string.append(self.__td('Rear', 2, 0, True))
        head_string.append(self.__td('Gear<br />Inches', 2, 0, True))
        head_string.append(self.__td(cadence_heading, 0, len(cadences), True))
        head_string.append('\n\t</tr>\n\t<tr>')
        for cadence_key in range(len(cadences) - 1):
            val = "{0:^3d}".format(int(cadences[cadence_key]))
            head_string.append(self.__td(val, 0, 0, True))
        head_string.append('\n\t</tr>')
        return ''.join(head_string)

    def __td(self, content, rowspan=0, colspan=0, head=False):
        if head:
            head = 'th'
        else:
            head = 'td'
        rs = ''
        cs = ''
        if rowspan > 0:
            rs = ' rowspan="{0:d}"'.format(rowspan)
        if colspan > 0:
            rs = ' colspan="{0:d}"'.format(colspan)
        return '\n\t\t<{0:s}{1:s}{2:s}>{3:s}</{0:s}>'.format(head, rs,
                                                             cs, content)

    def __table_separator(self, num_of_cadences):
        sep_string = []
        sep_string.append("|{0:-<6}+{0:-<10}+{0:-<10}+{0:-<8}".format(''))
        cadence_col = 0
        while cadence_col < num_of_cadences:
            sep_string.append("+{0:-<6}".format(''))
            cadence_col += 1
        sep_string.append("|\n".format(''))
        return ''.join(sep_string)

    def __table_speeds(self, front_ring, rear_ring, cadence, speed_unit):
        return "{0:3.1f}".format(self.speed(front_ring, rear_ring,
                                            cadence, speed_unit).value)

    def __table_width(self, table_string):
        table_string = ''.join(table_string)
        lines = string.split(table_string, '\n')
        max_length = 0
        for line in lines:
            if len(line) > max_length:
                max_length = len(line)
        return max_length

    def result_set(self, cadences, pref_speed=kmh):
        res = []
        gear = 0
        for i, front_ring in enumerate(self.front_rings.rings):
            for k, rear_ring in enumerate(self.rear_rings.rings):
                res.append({})
                speeds = {}
                for cadence in cadences:
                    speed = self.speed(front_ring, rear_ring, cadence,
                                       pref_speed)
                    speeds[cadence] = speed.value
                res[gear]['speeds'] = speeds
                res[gear]['front'] = tuple([i + 1, front_ring.teeth])
                res[gear]['rear'] = tuple([k + 1, rear_ring.teeth])
                gear_inch = self.gear_inch(front_ring, rear_ring)
                res[gear]['gear inch'] = gear_inch
                gear += 1
        return res

    def __table_data(self, cadences, pref_speed=kmh):
        data_string = []
        gear_num = 0
        # Populate the data
        for front_key, front_val in enumerate(self.front_rings.rings):
            data_string.append(self.__table_separator(len(cadences)))
            for rear_key, rear_val in enumerate(self.rear_rings.rings):
                speeds = []
                # Calculate all the speeds
                for cadence in cadences:
                    speeds.append(self.__table_speeds(front_val, rear_val,
                                                int(cadence), pref_speed))
                # pre-format gear values
                gear = " {0:02d}".format(gear_num + 1)
                front = " [{0:02d}] {1:02d}t".format(
                                front_key + 1, front_val.teeth)
                rear = " [{0:02d}] {1:02d}t".format(
                                rear_key + 1, rear_val.teeth)
                gear_inch = " {0:03d}".format(
                                int(self.gear_inch(front_val, rear_val)))
                # Add the gear values
                data_string.append("|{0:^6}|{1:^10}|{2:^10}|{3:^8}|".format(
                                    gear, front, rear, gear_inch))
                # Add the speeds
                for speed in speeds:
                    data_string.append("{0:^6}|".format(speed))

                data_string.append("\n")
                gear_num += 1
        return ''.join(data_string)

    def __html_table_data(self, cadences, pref_speed=kmh):
        data_string = []
        gear_num = 0
        # Populate the data
        for front_key, front_val in enumerate(self.front_rings.rings):
            class_str = ' class="ht"'
            for rear_key, rear_val in enumerate(self.rear_rings.rings):
                if rear_key != 0:
                    class_str = ''
                data_string.append('\n\n\t<tr{0:s}>'.format(class_str))
                speeds = []
                # Calculate all the speeds
                for cadence in cadences:
                    speeds.append(self.__table_speeds(front_val, rear_val,
                                                int(cadence), pref_speed))
                # pre-format gear values
                data_string.append(self.__td('{0:02d}'.format(gear_num + 1),
                                             0, 0, True))
                data_string.append(self.__td('[{0:02d}] {1:02d}t'.format(
                                front_key + 1, front_val.teeth)))
                data_string.append(self.__td('[{0:02d}] {1:02d}t'.format(
                                rear_key + 1, rear_val.teeth)))
                data_string.append(self.__td('{0:03d}'.format(
                                int(self.gear_inch(front_val, rear_val)))))
                # Add the speeds
                for speed in speeds:
                    data_string.append(self.__td(speed))

                data_string.append("\n\t</tr>")
                gear_num += 1
        return ''.join(data_string)

    def to_string(self, **kwargs):
        start_cadence = 60
        end_cadence = 120
        num_cadences = 5
        speed_unit = kmh
        format_html = False
        for k in kwargs:
            if k == "start_cadence":
                start_cadence = kwargs[k]
            if k == "end_cadence":
                end_cadence = kwargs[k]
            if k == "num_cadences":
                num_cadences = kwargs[k]
            if k == "speed_unit":
                speed_unit = kwargs[k]
            if k == "format":
                if kwargs[k] == 'html':
                    format_html = True
        """ Return a string representation of the gear_assembly object """
        # Cadence heading takes up space of 3 cadence values, so don't allow
        # anything less
        if num_cadences < 3:
            num_cadences = 3
        cadences = self.__table_cadences(start_cadence, end_cadence,
                                            0, num_cadences)
        table_string = []
        if format_html == True:
            table_string.append(self.__html_table_head(cadences, speed_unit))
            table_string.append(self.__html_table_data(cadences, speed_unit))
            table_string.append('\n</table>')
        else:
            table_string.append(self.__table_head(cadences, speed_unit))
            table_string.append(self.__table_data(cadences, speed_unit))
            table_string.append("-" * self.__table_width(table_string))
        return ''.join(table_string)
