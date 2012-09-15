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
from Tkinter import LabelFrame, E, Button
from lib.ui.genericwidgets import LabeledSpin


class RingArrangement(LabelFrame):
    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        title = None if 'title' not in kwargs else kwargs['title']
        rings = [] if 'rings' not in kwargs else kwargs['rings']
        LabelFrame.__init__(self, master, text=title)
        self.config(padx=20, pady=5)
        self.rings = []
        self.addbut = Button(text='+', command=self.userAddRing)
        for ring in rings:
            self.addRing(ring)
        self.renderRings()

    def showAddBut(self):
        self.addbut.grid(in_=self, columnspan=2)

    def userAddRing(self):
        self.addRing()
        self.renderRings()

    def addRing(self, val=None):
        if val is None:
            if len(self.rings) > 0:
                val = self.rings[-1].val.get() + 2
            else:
                val = 10
        ring = RingEntry(pos=len(self.rings), master=self)
        ring.val.set(val)
        self.rings.append(ring)
        return ring

    def renderRing(self, ring):
        self.addbut.grid_forget()
        ring.render()
        ring.grid(in_=self)
        if len(self.rings) > 1:
            rmbut = Button(master=self, text='-', padx=3, pady=0,
                           command=lambda i=ring: self.removeRing(i))
            rmbut.grid(row=int(ring.grid_info()['row']), column=1, in_=self)
        self.showAddBut()

    def renderRings(self):
        for ring in self.rings:
            self.renderRing(ring)
        self.showAddBut()

    def removeRing(self, ring):
        if len(self.rings) == 1:
            return
        self.rings.pop(ring.pos())
        self.orderRings()
        for widget in self.children:
            self.children[widget].grid_remove()
        self.renderRings()

    def orderRings(self):
        for pos, ring in enumerate(self.rings):
            ring.pos(pos)

    def vals(self, ring=None):
        if ring is None:
            return tuple([int(x.Spin.get()) for x in self.rings])
        return int(self.rings[ring].Spin.get())


class RingEntry(LabeledSpin):
    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        pos = -1 if 'pos' not in kwargs else kwargs['pos']

        LabeledSpin.__init__(self, master=master)
        self.__ringpos = pos
        self.Spin.config(from_=10, to=60, width=2)
        self.render()

    def pos(self, pos=-1):
        if pos >= 0:
            self.__ringpos = pos
            self.render()
        return self.__ringpos

    def render(self):
        self.Spin.grid(row=0, column=1, in_=self)
        self.lbl.config(text='Ring %2d' % (self.__ringpos + 1))
        self.lbl.grid(row=0, column=0, sticky=E, in_=self)
