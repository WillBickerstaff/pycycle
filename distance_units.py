#! /usr/bin/env python

from units import UnitGroup, UnitDefinition

class DistanceUnitGroup(UnitGroup):
    
    def __init__(self):
        super(DistanceUnitGroup,self).__init__('distance', 'd')
        
        self.definitions = [
            UnitDefinition('meter', 'm', 1.0),
            UnitDefinition('kilometer', 'km', 1000.0),
            UnitDefinition('millimeter', 'mm', 0.001),
            UnitDefinition('centimeter', 'cm', 0.01),
            UnitDefinition('mile', 'mi', 1609.344),
            UnitDefinition('thou', 'mil', 0.0000254),
            UnitDefinition('feet', 'ft', 0.3048),
            UnitDefinition('inch', 'in', 0.0254)
        ]

DistanceUnits = DistanceUnitGroup()
