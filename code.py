#!/usr/bin/env python
# coding: utf-8

# In[59]:


import numpy as np


# In[149]:


class Province:

    def __init__(self, name, is_sc = False, neighbours = [], unit = False):
        '''
        is_sc is true if the province is a supply center, land_neighbour_list is a list of provinces, coast_neighbours a dictionary with
        the name of the coast as key and as value a list of the provinces bordering that coast.
        '''
        # Why make coast_neighbours a dictionary and land_neighbour_list a list? Better to make all neighbour provinces 1 list?
        
        self.name = name
        self.neighbours = neighbours
        self.units = unit # defining units in dictionary gives errors for 'empty' objects
        self.sc = is_sc
        
        # simplified coast and land neighbours to a neighbours list
        
    def __repr__(self): # nice, kende __repr__ nog niet
        return self.name
    
    def is_sc(self):
        return self.sc
    
    def get_neighbours(self):
        return self.neighbours
    
#   def get_coast_neighbours(self,coast_name):
#       return self.coasts[coast_name] 
    
# Why introduce an add neighbour function? This should be given at initialisation.
#     def add_land_neighbours(self,province_list):
#        for province in province_list:
#            if province not in self.land_neighbours:
#                self.land_neighbours.append(province)
# See add_land_neighbours
#     def add_coast_neighbours(self,coast_name,province_list):
#        if coast_name not in self.coasts.keys():
#            self.coasts[coast_name] = []
#            self.units = dict.fromkeys(['land'] + list(self.coasts.keys()),False)  # Add the coast to the locations where units can be
#        for province in province_list:
#            if province not in self.coasts[coast_name]:
#                self.coasts[coast_name].append(province)
# location not defined in class
#     def add_unit(self,location):
#        self.units[location] = True
# location not defined in class
#     def remove_unit(self,location):
#         self.units[location] = False
    
#     def get_locations(self):
#         return list(self.units.keys())
    
#     def get_unit_location(self):
#         for location in self.units.keys():
#             if self.units[location]:
#                 return location
    def get_units(self):
        return self.units







# In[152]:


class Unit:
    def __init__(self,owner,province,unit_type):
        '''
        owner is the player that owns the unit, province is the province where the unit is.
        Where in the province the unit is, i.e. on land, north coast or south coast is stored in the Province! (maybe change this...)
        unit_type is 'A' for army or 'F' for fleet
        '''
        self.owner = owner
        self.province = province
        self.location = self.province.get_unit_location()
        self.unit_type = unit_type
        if unit_type == 'A':
            assert self.location == 'land'
        else:
            assert 'coast' in self.location
    
    def set_province(self,loc):
        self.province = loc
    
    def get_province(self):
        return self.province
    
    def get_location(self):
        return self.location
    
    def get_unit_type:
        return unit_type

    
bel.add_land_neighbours([ruh,hol])
hol.add_land_neighbours([kie,bel,ruh,kie,kie])
hol.add_coast_neighbours('coast',[hel,nth,hel])
print(hol.is_sc())
print(hol.get_land_neighbours())
print(hol.get_coast_neighbours('coast'))
print(hol.units)
hol.add_unit('land')
print(hol.get_locations())
print(hol.get_unit_location())


print(bel.get_unit_location())
        

army = Unit('France',hol,'A')
print(army.get_province())
print(army.get_location())



# In[ ]:


class Player:
    def __init__(self,starting_provinces,starting_scs):
        self.starting_scs = starting_scs
        self.owned_provinces = starting_provinces
        self.owned_scs = starting_scs
    
    def count_scs:
        pass



class Map:
    pass
    
    



# In[181]:


class Order:
    """
    unit is the unit that is given an order. Some methods are defined here because they must be able to be called on any order
    """
    
    def __init__(self,unit):
        self.unit = unit
        
    def is_valid_order(self):
        raise NotImplementedError 
    
    def execute_order(self):
        raise NotImplementedError 
    

class Holding_Order(Order):
    def __init__(self,unit):
        Order.__init__(self,unit)
    
    def is_valid_order(self):
        return True
    
    
        
class Moving_Order(Order):
    def __init__(self,unit,target,target_location = ''):
        """
        target is the province the unit is moving towards
        """
        Order.__init__(self,unit)
        self.target = target
        self.target_location = target_location
    
    def is_valid_order(self): 
        return True 
    
    def execute_order(self):
        if self.unit.unit_type == 'A':
            self.target.add_unit('land')
            self.unit.get_province().remove_unit(self.unit.get_location())
            
        elif len(self.target.units.keys())<3:  # This only triggers if there is one coast
            self.target.add_unit('coast')
            self.unit.get_province().remove_unit(self.unit.get_location())
        
        else:
            self.target.add_unit(self.target_location)
            self.unit.get_province().remove_unit(self.unit.get_location())            
    

class Support_Order(Order):
    def __init__(self,unit):
        Order.__init__(self,unit)
    
    def is_valid_order(self):
        pass #To implement
    


class Convoy_Order(Order):
    def __init__(self,unit):
        Order.__init__(self,unit)
    
    def is_valid_order(self):
        pass #To implement

    

        
hol = Province('hol')
bel = Province('bel')
kie = Province('kie')
ruh = Province('ruh')
hel = Province('hel')
nth = Province('nth')
        
        
bel.add_land_neighbours([ruh,hol])
hol.add_land_neighbours([kie,bel,ruh,kie,kie])
hol.add_coast_neighbours('coast',[hel,nth,hel])
ruh.add_unit('land')        
hol.add_unit('coast')

army1 = Unit('France',ruh,'A')
fleet1 = Unit('France',hol,'F')

ord1 = Moving_Order(army1,bel)
ord2 = Moving_Order(fleet1,bel)
ord1.execute_order()
ord2.execute_order()
print(ruh.units)
print(hol.units)
print(bel.units)


# In[182]:


class Season:
    """
    Here all the orders of a given season are collected and evaluated. Subclasses for different kinds of seasons
    """
    def update_board(self):
        pass
        # Get the orders
        # Do all the stuff here to update the board
        # print the new map and a list of order results 

class War_Season(Season):
    pass

class Winter(Season):
    pass

class Retreat(Season):
    pass


# In[ ]:



class Board:
    """
    This class is where the game will be played
    """
    def __init__(self):
        pass
        #add the state of the board at the start
    
