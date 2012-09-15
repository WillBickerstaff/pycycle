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
from Tkinter import LabelFrame, OptionMenu, StringVar
from lib.ui.genericwidgets import LabeledSpin
import lib.Units.distance_units as dist


class WheelEntry(LabelFrame):
    DIA_UNITS = [dist.mm, dist.cm, dist.inch]

    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        LabelFrame.__init__(self, master, text='Wheel')
        self.unitopts = ['%s (%s)' % (x.name, x.symbol)
                         for x in WheelEntry.DIA_UNITS]
        self.__val = WheelEntry.DIA_UNITS[0]
        self.createSpin()
        self.create_unit_opts()

    def create_unit_opts(self):
        self.unitoptselected = StringVar()
        self.unitoptselected.set(self.unitopts[2])
        self.unitopt = OptionMenu(self, self.unitoptselected, *self.unitopts)
        self.unitopt.grid(row=1, column=1, in_=self)
        self.val()

    def val(self, val=None):
        if val is not None:
            self.__val.value = val
        else:
            sel = self.unitoptselected.get().split()[0]
            for u in WheelEntry.DIA_UNITS:
                if sel in u.name:
                    self.__val = u
                    self.__val.value = int(self.Spin.val.get())
        return self.__val

    def createSpin(self):
        self.Spin = LabeledSpin(title='Dia')
        self.Spin.val.set(27)
        self.Spin.Spin.config(from_=10, to=1000, width=4)
        self.Spin.grid(row=1, column=0, in_=self)
