'''
Created on 1 Sep 2012

@author: will
'''
from Tkinter import (Label, Frame, N, S, E, W, ACTIVE, Button, LEFT)
import tkFont
from tkSimpleDialog import Dialog

license_text = '''
GPL V3
======

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


class AboutDialog(Dialog):

    def body(self, master):
        self.hdgFont = tkFont.Font(family="Helvetica", size=14, weight='bold')
        self.monoFont = tkFont.Font(family='Monospace', size=10)
        Label(master, text="pyCycle", font=self.hdgFont).grid(row=0,
                                                            sticky=E + W)
        Label(master, text="V 0.1.0").grid(row=1, sticky=E + W)
        Label(master, text=u"\u00A9 2012 Will Bickerstaff").grid(row=2,
                                                                 sticky=E + W)
        Label(master, text="<will.bickerstaff@gmail.com>").grid(row=3,
                                                                sticky=E + W)
        lictxt = Label(master, text=license_text, anchor=W)
        lictxt.grid(row=4, column=0, sticky=N + S + E + W)

    def buttonbox(self):
        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)

        box.pack()
