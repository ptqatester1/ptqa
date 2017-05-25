#**************************************************************************
#@author: Chris Allen
#@summary: Holds methods related to the environment manager
#**************************************************************************

from API.MenuBar.Extensions.Environment.EnvironmentConst import EnvironmentConst
from API.SquishSyntax import SquishSyntax
from __builtin__ import int as toInt, int as integer
from __builtin__ import type as objectType
from squish import *
import object
import test
import re

squishSyntax = SquishSyntax()
class Environment:
    def __init__(self):
        self.squishName = ''
        #customInteractions is a function used to add waiting until the document is fully loaded to other functions
        def customInteractions(func):
            def waitForPage(*args, **kwargs):
                for i in range(20):
                    if waitForObject(EnvironmentConst.BASE).evalJS("document.readyState") == "complete":
                        return func(*args, **kwargs)
                    snooze(1)
            return waitForPage
        self.click = customInteractions(squishSyntax.click)
        self.setText = customInteractions(squishSyntax.setText)
        self.clickLink = customInteractions(squishSyntax.clickLink)
        self.clickButton = customInteractions(squishSyntax.clickButton)
    
    def waitForLoadComplete(func):
        def waitFunc(*args, **kwargs):
            for i in range(20):
                if waitForObject(EnvironmentConst.BASE).evalJS("document.readyState") == "complete":
                    squishSyntax.clearCache(':Environment.DOCUMENT.HTML1')
                    break
                snooze(1)
            return func(*args, **kwargs)
        return waitFunc
    
    @waitForLoadComplete
    def changeLocation(self, p_location = "Intercity"):
        '''Enter either the location name ("Intercity") or as a row number starting at 1. Name should be the preferred method but
        using and integer is available as well since not all names will be unique.'''
        if objectType(p_location) is integer:
            self.clickLink(EnvironmentConst.LOCATIONS_BASE + '.A' + str(p_location))
        else:
            baseObj = findObject(EnvironmentConst.LOCATIONS_BASE)
            children = object.children(baseObj)
            for child in children:
                properties = object.properties(child)
                try:
                    if properties['tagName'] == 'A':
                        if properties['innerText'] == p_location:
                            self.clickLink(child)
                            break
                except:
                    continue

    def toggleSyncWithPhysical(self):
        self.click(EnvironmentConst.SYNC_WITH_PHYSICAL)
    
    def addHour(self, p_hours = 1):
        for i in range(p_hours):
            self.clickButton(EnvironmentConst.TIME_PLUS_BUTTON)
            if p_hours > 1:
                snooze(1)
    
    def subtractHour(selfp_hours = 1):
        for i in range(p_hours):
            self.clickButton(EnvironmentConst.TIME_MINUS_BUTTON)
            if p_hours > 1:
                snooze(1)
                
    def setHour(self, p_hour, p_isAm = True):
        '''Take an integer or string as the hour argument and a bool or "am" or "pm" as the isAm argument'''
        p_hour = toInt(p_hour)
        if str(p_isAm).lower() == 'am':
            p_isAm = True
        elif str(p_isAm).lower() == 'pm':
            p_isAm = False
            
        for i in range(24):
            time = self.getTime()
            currentHour = toInt(time.split(':')[0])
            currentAmPm = time.split(' ')[1].lower() == 'am'
            if (not p_hour == currentHour) or (not p_isAm == currentAmPm):
                self.addHour()
                snooze(1)
            else:
                break
        
    @waitForLoadComplete    
    def getTime(self):
        return str(findObject(EnvironmentConst.CURRENT_TIME).innerText)
    
    def setTimeScale(self, p_scale):
        self.setText(EnvironmentConst.TIME_SCALE_EDIT, p_scale)
        self.clickButton(EnvironmentConst.TIME_SCALE_SET)
    
    @waitForLoadComplete    
    def getTimeScale(self):
        return str(findObject(EnvironmentConst.TIME_SCALE_EDIT).value)
    
    @waitForLoadComplete    
    def getVisibleSetOrKeyButton(self, p_setButton):
        '''Take the set button of the field being editted as an argument
        For example if the temperature field is being editted use the EnvironmentConst.TEMP_SET_BUTTON constant'''
        set = p_setButton
        minusKey = '.'.join(p_setButton.split('.')[0:-1]) + '.SPAN1.BUTTON1'
        plusKey = '.'.join(p_setButton.split('.')[0:-1]) + '.SPAN1.BUTTON2'
        if findObject(set).visible:
            return set
        elif findObject(minusKey).visible:
            return minusKey
        elif findObject(plusKey).visible:
            return plusKey
        else:
            raise Exception('No buttons visible')
    
    @waitForLoadComplete    
    def getEnvironmentalFactorDiv(self, p_environmentalFactor):
        '''Enter either the factor name ("temperature") or as a row number starting at 1. Name should be the preferred method but
        using and integer is available as well. This will return a dictionary with the keys mainDiv, editField, setButton, minusKey, plusKey'''
        if objectType(p_environmentalFactor) is integer:
            return EnvironmentConst.ENVIRONMENTAL_FACTORS_BASE + '.DIV' + str(p_environmentalFactor)
        else:
            baseObj = findObject(EnvironmentConst.ENVIRONMENTAL_FACTORS_BASE)
            children = object.children(baseObj)
            count = 0
            for i,child in enumerate(children):
                properties = object.properties(children[i])
                try:
                    if properties['tagName'] == 'DIV':
                        count += 1
                        if str(p_environmentalFactor).lower() in str(properties['innerText']).lower():
                            mainDiv = EnvironmentConst.ENVIRONMENTAL_FACTORS_BASE + '.DIV' + str(count) 
                            editField = mainDiv + '.INPUT1'
                            setButton = mainDiv + '.BUTTON1'
                            minusKey = mainDiv + '.SPAN1.BUTTON1'
                            plusKey = mainDiv + '.SPAN1.BUTTON2'
                            return {'mainDiv':mainDiv, 'editField':editField, 'setButton':setButton, 'minusKey':minusKey, 'plusKey':plusKey}
                            break
                except:
                    continue
    
    @waitForLoadComplete
    def setEnvironmentFactor(self, p_factor, p_value):
        div = self.getEnvironmentalFactorDiv(p_factor)
        self.setText(div['editField'], p_value)
        self.clickButton(self.getVisibleSetOrKeyButton(div['setButton']))
        
    def getEnvironmentFactorValue(self, p_factor):
        return str(findObject(self.getEnvironmentalFactorDiv(p_factor)['editField']).value)
    
    def getDaylight(self):
        snooze(1)
        return str(findObject(self.getEnvironmentalFactorDiv('daylight')['mainDiv']+'.SPAN1').innerText)
    
    def setTemperature(self, p_value):
        self.setEnvironmentFactor('temperature', p_value)
    
    def getTemperature(self):
        return self.getEnvironmentFactorValue('temperature')
    
    def setHumidity(self, p_value):
        self.setEnvironmentFactor('humidity', p_value)
    
    def getHumidity(self):
        return self.getEnvironmentFactorValue('humidity')
    
    def setWaterLevel(self, p_value):
        self.setEnvironmentFactor('water level', p_value)
    
    def getWaterLevel(self):
        return self.getEnvironmentFactorValue('water level')
    
    def setSmokeLevel(self, p_value):
        self.setEnvironmentFactor('smoke', p_value)
    
    def getSmokeLevel(self):
        return self.getEnvironmentFactorValue('smoke')
    
    def setC02Level(self, p_value):
        self.setEnvironmentFactor('carbon dioxide', p_value)
    
    def getC02Level(self):
        return self.getEnvironmentFactorValue('carbon dioxide')
    
    def setC0Level(self, p_value):
        self.setEnvironmentFactor('carbon monoxide', p_value)
    
    def getC0Level(self):
        return self.getEnvironmentFactorValue('carbon monoxide')
    
    def setWindSpeed(self, p_value):
        self.setEnvironmentFactor('wind speed', p_value)
    
    def getWindSpeed(self):
        return self.getEnvironmentFactorValue('wind speed')
    
    def setRainFall(self, p_value):
        self.setEnvironmentFactor('rain fall', p_value)
    
    def getRainFall(self):
        return self.getEnvironmentFactorValue('rain fall')
    
    def setMode(self, p_mode):
        mode = p_mode.lower()
        if mode == 'preset':
            self.clickButton(EnvironmentConst.MODE_PRESET)
        elif mode == 'manual':
            self.clickButton(EnvironmentConst.MODE_MANUAL)
        elif mode == 'key frames':
            self.clickButton(EnvironmentConst.MODE_KEY_FRAMES)
        else:
            raise Exception("Should be preset, manual or key frames")
    
    def setMeasurement(self, p_measure):
        measure = p_measure.lower()
        if measure == 'imperial':
            self.clickButton(EnvironmentConst.MEASURE_IMPERIAL)
        elif measure == 'metric':
            self.clickButton(EnvironmentConst.MEASURE_METRIC)
        else:
            raise Exception("Should be Imperial or Metric")
    
    