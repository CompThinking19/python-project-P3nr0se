#!/usr/bin/env python
# coding: utf-8

# In[3]:
import re
Start = open("IntroductoryText.txt")
Intro = Start.read()
print Intro
#Attempting to create a resource system for the game
class Logistics:
    # Defined initial values of resources.
    numrockets = 0
    fueltank = 30
    materialslog = 25
    heat_resistant_materials = 0
    am = 0
    crm = 0
    #Initial checks to tell the player that they are not on any of these planets.
    MarsLand = False
    MarsBase = False
    MarsMine = False
    MarsFuel = False
    MoonLand = False
    MoonBase = False
    MoonMine = False
    MoonFuel = False
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
    #This is meant to be the user's method of interfacing with the resources that they have access to.
    def getrockets(self):
        return numrockets
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
    def getrequirements(self):
        print "The basic rocket requires 10 basic materials and the 'BuildRocket' command."
        if MoonLand != True:
            print "Traveling to the moon requires fifteen fuel and the 'EarthtoLuna' command"
        if MarsLand != True:
            print "Traveling to mars requires twenty-five fuel."
        print "More resources are gained by constructing bases on the surface of the planet, which will be explained upon touchdown"
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
            MoonLand == True
            moontext = open(MoonTouchdown.txt)
            moonopen = moontext.read()
            print moonopen
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
            MarsLand == True
            marstext = open(MarsTouchdown.txt)
            marsopen = marstext.read()
            print marsopen
        else:
            if numrockets == 0:
                print "We need a rocket to get to mars!"
            else:
                print "We need more fuel!"
    def BuildMars(self):
        if MarsLand != True:
            return "We aren't on Mars Commander!"
        if materials_list != 10:
            return "We don't have the Materials to Construct anything Commander!"
        if MarsLand == True and materials_list == 10:
            print "We may construct a based on Mars! Yes or No Commander?"
            if imput == True:
                materials_list -= 10
                MarsBase == True
                print "Type in 'MarsBase' to acess its functions Commander!"
    def MarsBase(self):
        if MarsBase == True:
            print "The Mars Base has a variety of construction options. Please type '.MarsMine' to generate materials. Otherwise please type 'MarsFuel' to generate fuel!"
    def MarsMine(self):
        if MarsBase != True or MarsMine == True:
            return "Something's not right here! We aren't on mars or we have already mined Mars!"
        if MarsBase == True and MarsMine != True:
            am = 15
            materials_list += 25
            return "Orders confirmed, commander! Minerals being stockpiled! (+15 Armour Materials, + 25 Materials)"
    def MarsFuel(self):
        if MarsBase != True or MarsFuel == True:
            return "Something's not right here! We aren't on mars or we have already extracted fuel from Mars!"
        if MarsBase == True and MarsFuel != True:
            print "Orders confirmed, commander! Fuel being stockpiled! (+25 Fuel)"
            fueltank += 25
            return MarsFuel == True
    def BuildMoon(self):
        if MoonLand != True:
            return "We aren't on the Moon Commander!"
        if materials_list != 10:
            return "We don't have the Materials to Construct anything Commander!"
        if MoonLand == True and materials_list == 10:
            print "We may construct a based on Moon! True or No Commander?"
            if imput == True:
                materials_list -= 10
                MoonBase == True
                print "Type in 'MoonBase' to acess its functions Commander!"
    def MoonBase(self):
        if MoonBase == True:
            print "The Moon Base has a variety of construction options. Please type 'MoonMine' to generate materials. Otherwise please type 'MoonFuel' to generate fuel!"
    def MoonMine(self):
        if MoonBase != True or MoonMine == True:
            return "Something's not right here! We aren't on mars or we have already mined the Moon!"
        if MoonBase == True and MoonMine != True:
            print "Orders confirmed, commander! Minerals being stockpiled! (+15 Materials. + 25 Cold Resistant Materials)"
            materials_list += 15
            crm += 25
            return MoonMine == True
    def MoonFuel(self):
        if MoonBase != True or MoonFuel == True:
            return "Something's not right here! We aren't on mars or we have already extracted fuel from the Moon!"
        if MoonBase == True and MoonFuel != True:
            print "Orders confirmed, commander! Fuel being stockpiled! (+50 Fuel)"
            fueltank += 50
            return MoonFuel == True
