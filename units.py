#! /usr/bin/env python

from fractions import Fraction


class UnitGroup(object):
    
    def __init__(self, name=None, symbol=None):
        self.category_name = name
        self.category_symbol = symbol
        self.definitions = []
        
    def get_unit(self, required_unit):
        for k, v in enumerate(self.definitions):
            if v.name == required_unit or v.symbol == required_unit:
                return Unit(self.definitions[k])
                                

class UnitDefinition(object):

    def __init__(self, name, symbol, factor=1.0):
        self.factor = factor
        self.symbol = symbol
        self.name = name
            
    def is_base(self):
        if factor == 1.0:
            return True
        else:
           return False


class Unit(UnitDefinition):
    
    def __init__(self, unit_definition, value=0):
        self.value = value
        super(Unit,self).__init__(unit_definition.name,
                                  unit_definition.symbol,
                                  unit_definition.factor)
        
            
    def convert_to_base(self):
        return self.value * self.factor
        
    def convert_to(self, new_unit_definition):
        return self.convert_to_base() / new_unit_definition.factor
        
    def as_fraction(self):
        rStr = []
        if int(self.value) > 0:
            rStr.append(str(int(self.value)))
            rStr.append(' ')
            
        rStr.append(str(Fraction.from_float(self.value % 1). \
                        limit_denominator(1024)))
                
        return ''.join(rStr)
