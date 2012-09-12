#! /usr/bin/env python

# Copyright 2010 Will Bickerstaff
# This file is part of PyCycle.
#
# PyCycle is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.read value
#
# PyCycle is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# PyCycle. If not, see http://www.gnu.org/licenses/
from Tkinter import Frame, Button, N, S, E, W, TOP
from lib.ui.ring import RingEntry, RingArrangement


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__input = Frame()
        self.__results = Frame()
        self.input_fields()

        self.__input.grid(row=0, column=0, sticky=W, in_=self)
        self.__results.grid(row=0, column=0, sticky=W, in_=self)

    def input_fields(self):
        self.cassette_input = Frame()
        self.chainset_input = Frame()
        self.wheel_input = Frame()

        self.create_cassette_input()
        self.create_chainset_input()

        self.chainset_input.grid(row=1, column=1, sticky=N + W,
                                 in_=self.__input)
        self.wheel_input.grid(row=0, column=0, columnspan=2,
                              in_=self.__input)

    def create_cassette_input(self):
        self.cassette_rings = RingArrangement([12, 14, 16, 18, 21, 24, 28],
                                              'Cassette')
        self.cassette_rings.grid(row=0, column=0, sticky=N)

    def create_chainset_input(self):
        self.chainset_rings = RingArrangement([34, 50], 'Chainset')
        self.chainset_rings.grid(row=0, column=1, sticky=N)