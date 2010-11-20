#! /usr/bin/env python

from units import UnitGroup, UnitDefinition

class SpeedUnitGroup(UnitGroup):
    
    def __init__(self):
        super(DistanceUnitGroup,self).__init__('velocity', 'v')
        self.definitions = [
            UnitDefinition('meter per second', 'ms', 1.0),
            UnitDefinition('kilometer per hour', 'kmh', 0.277777778),
            UnitDefinition('mile per hour', 'mph', 0.44704)
        ]
        
SpeedUnits = SpeedUnitGroup()
