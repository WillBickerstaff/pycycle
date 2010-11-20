#! /usr/bin/env python

from distance_units import DistanceUnit
from speed_units import SpeedUnit
from time_units import TimeUnit


class SpeedTimeDistanceCalc(object):


    def __init__(self):
        self.base_vals{'speed' : SpeedUnit.get_unit('ms'),
                       'time' : TimeUnit.get_unit('s'),
                       'distance' : DistanceUnit.get_unit('m')
                      }

        self.vals{'speed' : SpeedUnit.get_unit('ms'),
                  'time' : TimeUnit.get_unit('s'),
                  'distance' : DistanceUnit.get_unit('m')
                  }

    def calc(self):
        for k, v in self.vals.items():
            self.base_vals[k].value = v.as_base

        if self.base_vals['distance'].value == 0:
            self.__calc_distance()
        if self.base_vals['speed'].value == 0:
            self.__calc_speed()
        if self.base_vals['time'].value == 0:
            self.__calc_time

    def __calc_distance(self):
        self.base_vals['distance'].value = \
            self.base_vals['time'] * self.base_vals['speed'].value

        self.__set_target('distance')

    def __calc_speed(self):
        self.base_vals['speed'].value = \
            self.base_vals['distance'] / self.base_vals['time'].value

        self.__set_target('speed')

    def __calc_time(self):
        self.base_vals['time'].value = \
            self.base_vals['distance'] / self.base_vals['speed'].value

        self.__set_target('time')
        

    def __set_target(self, target):
        self.vals[target].value = \
            self.base_vals[target].convert_to(self.vals[target])

                              
    def format_time(self):
        ftime = {}
        s = self.baseVals['time']
        ftime['h'] = int(s/3600)
        s = s-(ftime['h']*3600)
        ftime['m'] = int(s/60)
        ftime['s'] = s-(ftime['m']*60)

        return ':'.join(ftime)
        
                                                 

        
