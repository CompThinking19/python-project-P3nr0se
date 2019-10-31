#!/usr/bin/env python
# coding: utf-8

# In[3]:

Start! = open(IntroductoryText.txt)
#Attempting to create a resource system for the game
class Logistics:
    def class_method(resources):
        def __init__(fuel, materials, heat_resistant_materials, armour_materials, cold_resistant_materials):
            def fuelgauge(f):
                fuel = f
                if f < 0:
                    print "We can't go anywhere! Produce more fuel or the project is done."
            def materials_list(m):
                materials = m
                if m < 0:
                    print "We can't make anything without materials! Please mine more or we won't be going anywhere."
            def heat_resistant_materials_list(hrm):
                heat_resistant_materials = hrm
                if hrm < 0:
                    print "We can't make these ships without heat resistant materials!"
            def armour_materials_list(am):
                armour_materials = am
                if am < 0:
                    print "We can't make these ships without armour material!"
            def cold_resistant_materials_list(crm):
                cold_resistant_materials = crm
                if crm < 0:
                    print "We can't make these ships without cold resistant materials!"
