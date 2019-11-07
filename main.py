#!/usr/bin/env python
# coding: utf-8

# In[3]:

Start = open(IntroductoryText.txt)
#Attempting to create a resource system for the game
class Logistics:
    def __init__(self, fuel, materials, hrm, armour_materials, cold_resistant_materials):
        #Fueltank is meant to define the resource used to get from place to place.
        fueltank = fuel
        if fueltank < 1:
            print "We can't go anywhere! Produce more fuel or the project can no longer continue."
        if fueltank > 0:
            print fueltank
    #materials_list is meant to define the base material used to construct ships or buildings
        materialslog = materials
        if materialslog < 1:
            print "We can't make anything without materials! Please mine more or we won't be going anywhere."
        if materialslog > 0:
            print materialslog
    #heat_resistant materials refer to materials needed to build ships that can go to venus and mercury
        heat_resistant_materials = hrm
        if heat_resistant_materials < 1:
            print "We can't make these ships without heat resistant materials!"
        if heat_resistant_materials > 0:
            print  heat_resistant_materials
    #armour_materials are supposed to be used for ships that need to travel through the asteroid belt.
        am = armour_materials
        if am < 1:
            print "We can't make these ships without armour material!"
        if am > 0:
            print am
    #cold_resistant_materials are meant to be used for ships that travel past Jupiter
        crm = cold_resistant_materials
        if crm < 0:
            print "We can't make these ships without cold resistant materials!"
        if crm > 0:
            print crm
    def getfuel(self):
        return fueltank
    def getmats(self):
        return materialslog
    def gethotmats(self):
        return heat_resistant_materials
    def getarmour(self):
        return am
    def getcoldmats(self):
        return crm
    def initialresources():
        stuff = [fueltank, materialslog, heat_resistant, am, crm]
        fueltank = 10
        materialslog = 50
        heat_resistant = 0
        am = 0
        crm = 0
        return stuff
    def resources(self):
        print ["Fuel", fueltank, "Materials", materialslog, "Heat Resistant Materials", heat_resistant_materials, "Armour Materials", am, "Cold Resistant Materials", crm]

class Building:
    def __init__(self, Construct)
    import Logistics
        Construct = build
        def build(rocket):
            for rocket in build:
                clear():
