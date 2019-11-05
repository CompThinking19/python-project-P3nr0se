#!/usr/bin/env python
# coding: utf-8

# In[3]:

Start! = open(IntroductoryText.txt)
#Attempting to create a resource system for the game
class Logistics:
    def class_method(resources):
        def __init__(fuel, materials, heat_resistant_materials, armour_materials, cold_resistant_materials):
            #Fuelgauge is meant to define the resource used to get from place to place.
            def fuelgauge(f):
                fuel = f
                if f < 0:
                    print "We can't go anywhere! Produce more fuel or the project is done."
            #materials_list is meant to define the base material used to construct ships or buildings
            def materials_list(m):
                materials = m
                if m < 0:
                    print "We can't make anything without materials! Please mine more or we won't be going anywhere."
            #heat_resistant materials refer to materials needed to build ships that can go to venus and mercury
            def heat_resistant_materials_list(hrm):
                heat_resistant_materials = hrm
                if hrm < 0:
                    print "We can't make these ships without heat resistant materials!"
            #armour_materials are supposed to be used for ships that need to travel through the asteroid belt.
            def armour_materials_list(am):
                armour_materials = am
                if am < 0:
                    print "We can't make these ships without armour material!"
            #cold_resistant_materials are meant to be used for ships that travel past Jupiter
            def cold_resistant_materials_list(crm):
                cold_resistant_materials = crm
                if crm < 0:
                    print "We can't make these ships without cold resistant materials!"
