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

from Tkinter import Frame, Label, N, S, E, W, SUNKEN, RIDGE


class OutputPane(Frame):
    def __init__(self, **kwargs):
        master = None if 'master' not in kwargs else kwargs['master']
        self.data = None if 'data' not in kwargs else kwargs['data']
        velsym = 'Unknown' if 'velsym' not in kwargs else kwargs['velsym']
        Frame.__init__(self, master=master)
        self.canvas = Frame(master, relief=SUNKEN, bg='#ffffff', borderwidth=2,
                            width=200, height=200)
        self.create_header(velsym)
        for gear, res in enumerate(self.data):
            self.make_res(gear + 1, res)
        Label(text="Result:").grid(row=0, column=0, in_=self, sticky=W)
        self.canvas.grid(row=1, column=0, in_=self, sticky=N + S + E + W)

    def make_res(self, gear, data):
        row = 3 + gear
        self.res_text('%02d' % gear, row, 0)
        self.res_text('[%d] %dt' % (data['front'][0], data['front'][1]),
                                    row, 1)
        self.res_text('[%d] %dt' % (data['rear'][0], data['rear'][1]),
                                    row, 2)
        self.res_text('%d' % data['gear inch'], row, 3)
        col = 4
        for vel in sorted(self.data[0]['speeds']):
            self.res_text('%.2f' % data['speeds'][vel], row, col)
            col += 1

    def res_text(self, text, row, col):
        lbl = Label(text=text, relief=RIDGE, borderwidth=1, bg='#ffffff',
                    fg='#000000', padx=5, anchor=W)
        lbl.grid(row=row, column=col, in_=self.canvas, sticky=N + S + E + W)

    def create_header(self, velsym='Unknown'):
        self.header_text('Gear', col=0, rowspan=2)
        self.header_text('Chainset', col=1, rowspan=2)
        self.header_text('Cassette', col=2, rowspan=2)
        self.header_text('Gear\nInches', col=3, rowspan=2)
        self.header_text('Velocity (%s) @ Cadence' % velsym, col=4, row=0,
                         colspan=len(self.data[0]['speeds']))
        col = 4
        for cadence in sorted(self.data[0]['speeds']):
            self.header_text(cadence, col=col, row=1)
            col += 1

    def header_text(self, text, **kwargs):
        rowspan = 1 if 'rowspan' not in kwargs else kwargs['rowspan']
        colspan = 1 if 'colspan' not in kwargs else kwargs['colspan']
        row = 0 if 'row' not in kwargs else kwargs['row']
        col = kwargs['col']
        lbl = Label(text=text, relief=RIDGE, borderwidth=1, bg='#000000',
                    fg='#ffffff', padx=5, anchor=S)
        lbl.grid(row=row, column=col, rowspan=rowspan, in_=self.canvas,
                 columnspan=colspan, sticky=N + S + E + W)
