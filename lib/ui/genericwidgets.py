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

from Tkinter import Frame, Label, Spinbox, W, IntVar


class LabeledSpin(Frame):
    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        title = '' if 'title' not in kwargs else kwargs['title']
        Frame.__init__(self, master)
        self.val = IntVar()
        self.lbl = Label(text=title)
        self.lbl.grid(row=0, column=0, sticky=W, in_=self)
        self.Spin = Spinbox(textvariable=self.val)
        self.Spin.grid(row=0, column=1, sticky=W, in_=self)
