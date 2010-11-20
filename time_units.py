#! /usr/bin/env python

from units import UnitGroup, UnitDefinition

class TimeUnitGroup(UnitGroup):
    
    def __init__(self):
        super(DistanceUnitGroup,self).__init__('time', 't')   
        self.definitions = [
            UnitDefinition('second', 's', 1.0),
            UnitDefinition('minute', 'm', 60.0),
            UnitDefinition('hour', 'h', 3600.0),
            UnitDefinition('day', 'd', 86400.0)
        ]

TimeUnits = TimeUnitGroup()
