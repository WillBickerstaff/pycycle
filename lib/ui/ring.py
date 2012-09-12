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
from Tkinter import Frame, Label, Spinbox, E, Button, IntVar


class RingArrangement(Frame):
    def __init__(self, rings=[], master=None):
        Frame.__init__(self, master)
        self.rings = []
        self.addbut = Button(text='+', command=self.userAddRing)
        for ring in rings:
            self.addRing(ring)
        self.renderRings()

    def showAddBut(self):
        self.addbut.grid(in_=self, columnspan=2)

    def userAddRing(self):
        self.renderRing(self.addRing())

    def addRing(self, val=None):
        if val is None:
            if len(self.rings) > 0:
                val = self.rings[-1].val.get()
            else:
                val = 10
        ring = RingEntry(len(self.rings), self)
        ring.val.set(val)
        self.rings.append(ring)
        print self.vals()
        return ring

    def renderRing(self, ring):
        self.addbut.grid_forget()
        ring.render()
        ring.grid(in_=self)
        rmbut = Button(master=self, text='-',
                       command=lambda i=ring: self.removeRing(i))
        rmbut.grid(row=int(ring.grid_info()['row']), column=1, in_=self)
        self.showAddBut()

    def renderRings(self):
        for ring in self.rings:
            self.renderRing(ring)
        self.showAddBut()

    def removeRing(self, ring):
        self.rings.pop(ring.pos())
        self.orderRings()
        print self.children
        for widget in self.children:
            self.children[widget].grid_remove()
        self.renderRings()
        print self.vals()

    def orderRings(self):
        for pos, ring in enumerate(self.rings):
            ring.pos(pos)

    def vals(self, ring=None):
        if ring is None:
            return [int(x.val.get()) for x in self.rings]
        return int(self.ringss[ring].val.get())


class RingEntry(Frame):
    def __init__(self, ringpos=0, master=None):
        Frame.__init__(self, master)
        self.val = IntVar()
        self.__ringpos = ringpos
        self.lbl = Label()
        self.Spin = Spinbox(from_=10, to=60, width=2, textvariable=self.val)
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
