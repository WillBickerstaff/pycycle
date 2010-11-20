#! /usr/bin/env python

from units import UnitGroup, UnitDefinition

class DistanceUnitGroup(UnitGroup):
    
    def __init__(self):
        super(DistanceUnitGroup,self).__init__('mass', 'm')
        self.definitions = [
            UnitDefinition('kilogram', 'kg', 1.0),
            UnitDefinition('gram', 'g', 0.001),
            UnitDefinition('ounce', 'oz', 0.0283495231),
            UnitDefinition('pound', 'lb', 0.45359237),
            UnitDefinition('tonne', 't', 1000.0)
        ]

DistanceUnits = DistanceUnitGroup()
