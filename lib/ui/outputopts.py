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
from Tkinter import (LabelFrame, Label, OptionMenu, StringVar, Spinbox,
                     Frame, END, Button, W)
import lib.Units.speed_units as speeds


class OutOptions(LabelFrame):

    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        LabelFrame.__init__(self, master, text='Output Options')
        self.config(padx=20, pady=5)
        self.cadences = CadenceEntry()
        self.cadences.grid(row=0, column=0, sticky=W, in_=self)
        self.velocity = VelocitySelect()
        self.velocity.grid(row=1, column=0, sticky=W, in_=self)

    def speedUnits(self):
        return self.velocity.val()

    def cadenceVals(self):
        return self.cadences.vals()


class VelocitySelect(Frame):
    VELOCITIES = [speeds.kmh, speeds.mih, speeds.ms]

    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        Frame.__init__(self, master)
        Label(text='Output Velocity').grid(row=0, column=0, sticky=W,
                                           in_=self)
        self.vel = VelocitySelect.VELOCITIES[0]
        self.vel_selected = StringVar()
        vel_opts = ['%s (%s)' % (sp.name, sp.symbol)
                    for sp in VelocitySelect.VELOCITIES]
        self.velopt = OptionMenu(self, self.vel_selected, *vel_opts)
        self.vel_selected.set('%s (%s)' % (self.vel.name, self.vel.symbol))
        self.velopt.grid(row=0, column=1, sticky=W)

    def val(self, val=None):
        if val is not None:
            self.vel.value = val
        else:
            sel = self.unitoptselected.get().split()[0]
            for v in VelocitySelect.VELOCITIES:
                if sel in v.name:
                    self.vel = v
                    self.vel.value = int(self.Spin.get())
        return self.vel


class CadenceEntry(Frame):
    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        title = 'Cadence' if 'title' not in kwargs else kwargs['title']
        cadences = [] if 'cadence' not in kwargs else kwargs['cadence']
        Frame.__init__(self, master=master)
        self.title = Label(text=title, master=self)
        self.cadences = []
        self.addbut = Button(text='+', command=self.userAddCadence)
        if len(cadences) == 0:
            for c in range(40, 100, 10):
                self.create_entry(c)
        self.render()

    def create_entry(self, cadence=None):
        if cadence is None:
            if len(self.cadences) > 0:
                cadence = int(self.cadences[-1].get()) + 10
            else:
                cadence = 40
        cadenceent = Spinbox(from_=10, to=180, width=3, master=self)
        cadenceent.delete(0, END)
        cadenceent.insert(0, cadence)
        self.cadences.append(cadenceent)

    def userAddCadence(self):
        self.create_entry()
        self.render()

    def render(self):
        for widget in self.children:
            self.children[widget].grid_remove()
        self.title.grid(row=0, column=0, columnspan=5, sticky=W, in_=self)
        col = 0
        for spin in self.cadences:
            spin.grid(row=1, column=col, sticky=W, in_=self)
            if len(self.cadences) > 1:
                rmbut = Button(master=self, text='-',
                               command=lambda i=col: self.rmCadence(i))
                rmbut.grid(row=2, column=col, in_=self)
            col += 1
        self.addbut.grid(row=1, column=col, sticky=W, in_=self)

    def rmCadence(self, col):
        if len(self.cadences) == 1:
            return
        self.cadences[col].grid_remove()
        self.cadences.pop(col)
        self.render()

    def vals(self, cadence=None):
        if cadence is None:
            return tuple([int(x.get()) for x in self.cadences])
        return int(self.cadences[cadence].get())
