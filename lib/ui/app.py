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
from Tkinter import Frame, Button, N, S, E, W
from lib.ui.ring import RingArrangement
from lib.ui.wheel import WheelEntry
from lib.ui.outputopts import OutOptions
from lib.Bike import bike
from lib.ui.output import OutputPane


class Application(Frame):

    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        Frame.__init__(self, master)
        self.__input = Frame(padx=10, pady=10)
        self.__output = Frame(padx=10, pady=10)
        self.__results = Frame()
        self.input_fields()
        self.__input.grid(row=0, column=0, sticky=W)
        self.__results.grid(row=0, column=1, sticky=W, in_=self)

    def input_fields(self):
        self.cassette_input = Frame()
        self.chainset_input = Frame()
        self.wheel_input = Frame()
        self.output_opts = Frame()

        self.create_cassette_input()
        self.create_chainset_input()
        self.create_wheel_input()
        self.create_output_opts()

    def create_cassette_input(self):
        self.cassette_rings = RingArrangement(
                rings=[28, 24, 21, 18, 16, 14, 12], title='Cassette')
        self.cassette_rings.grid(row=0, column=0, rowspan=2,
                                 sticky=N + S + E + W, in_=self.__input)

    def create_chainset_input(self):
        self.chainset_rings = RingArrangement(rings=[34, 50], title='Chainset')
        self.chainset_rings.grid(row=0, column=1, sticky=N + S + E + W,
                                 in_=self.__input)

    def create_wheel_input(self):
        self.wheel_input = WheelEntry()
        self.wheel_input.grid(row=1, column=1, sticky=N + S + E + W,
                              in_=self.__input)

    def create_output_opts(self):
        self.output_opts = OutOptions()
        self.output_opts.grid(row=2, column=0, columnspan=2,
                              sticky=N + S + E + W, in_=self.__input)
        Button(text="Calculate", command=self.calc).grid(row=3, column=1,
                                                         sticky=E,
                                                         in_=self.__input)

    def calc(self):
        cycle = bike()
        cycle.wheel_size(self.wheel_input.val())
        for w in self.__output.children:
            self.__output.children[w].grid_remove()
        for ring in self.cassette_rings.vals():
            cycle.gearing.add_rear_ring(ring)
        for ring in self.chainset_rings.vals():
            cycle.gearing.add_front_ring(ring)
        data = cycle.gearing.result_set(self.output_opts.cadenceVals(),
                                        self.output_opts.speedUnits())
        op = OutputPane(master=self.__output, data=data,
                        velsym=self.output_opts.speedUnits().symbol)
        op.grid(in_=self.__output, row=0, column=0)
        self.__output.grid(row=0, column=1, sticky=N + S + E + W)
