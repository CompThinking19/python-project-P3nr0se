#!/usr/bin/env python
# coding: utf-8

# In[3]:

Start = open(IntroductoryText.txt)
#Attempting to create a resource system for the game
class Logistics:
    numrockets = 0
    def __init__(self, fuel, materials, hrm, armour_materials, cold_resistant_materials):
        #Fueltank is meant to define the resource used to get from place to place.
        fueltank = fuel
    #materials_list is meant to define the base material used to construct ships or buildings
        materialslog = materials
    #heat_resistant materials refer to materials needed to build ships that can go to venus and mercury
        heat_resistant_materials = hrm
    #armour_materials are supposed to be used for ships that need to travel through the asteroid belt.
        am = armour_materials
    #cold_resistant_materials are meant to be used for ships that travel past Jupiter
        crm = cold_resistant_materials
    #This is meant to be the user's method of interfacing with the resources that they have access to
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
    #Used to construct a basic rocket.
    def BuildRocket(self):
        materialslog -= 10
        numrockets += 1
    #Used to Launch a Rocket to the moon
    def EarthtoLuna(self):
        if numrockets > 0 and fueltank >= 15:
            numrockets -= 1
            fueltank -= 15
            #trying to add a condition that recognizes human presence on the moon
            MoonLand == yes
            open(MoonTouchdown.txt)
        else:
            if numrockets == 0:
                print "We need a rocket to get to the moon!"
            else:
                print "We need more fuel!"
    #Used to launch a rocket to Mars
    def EarthtoMars(self):
        if numrockets > 0 and fueltank >= 25:
            numrockets -= 1
            fueltank -= 25
            #trying to add a condition that recognizes human presence on Mars
            MarsLand == yes
            open(MarsTouchdown.txt)
        else:
            if numrockets == 0:
                print "We need a rocket to get to mars!"
            else:
                print "We need more fuel!"
