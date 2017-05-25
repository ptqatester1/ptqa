######################
#@author: Pamela Vinco
######################
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Ioe.SBC import SBC
from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.IoeBase import IoeBase
from API.Device.Ioe.MCUConst import MCUConst
from API.Toolbar.MainToolBar.CustomDeviceWindow import CustomDeviceWindow
from API.Toolbar.MainToolBar.CustomDeviceWindowConst import CustomDeviceWindowConst
import os
from API.functions import check

util = Util()

env = os.environ['PT7HOME']
templatePath = env + os.sep + 'templates'
dirContents = os.listdir(templatePath)
nonIoeTemplates = ['2811 NM-ESW-161 (2) WIC-2T', '2621XM NM-2FE2W (2) WIC-2T', '1841 WIC-2T', 'Wireless PC']

itemsNotToInclude = ['1841_WIC_2T', '2621XM_NM_2FE2W_2_WIC_2T', '2811_NM_ESW_161_2_WIC_2T', 'environments', 'Wireless_PC']
ioeTemplates = []
for f in dirContents:
    if not f in itemsNotToInclude:
        ioeTemplates.append(f.split('.')[0])
devNameList = []
devList = []

    
def main():
    util.maximizePT()
    CustomDeviceWindow().goToTemplateManager()
    devNameList = [dev for dev in CustomDeviceWindow().deviceList if not dev in nonIoeTemplates]
    CustomDeviceWindow().close()
    xpos = 100
    ypos = 100
    for i, deviceName in enumerate(devNameList):
        #devList.append(MCU(deviceName, xpos, ypos, deviceName))
        dev = IoeBase(deviceName, xpos, ypos, 'IoE' + str(i))
        devList.append(dev)
    for dev in devList: 
        test.log('tesing ' + dev.deviceModel)
        dev.create()
        dev.select()
        try:
            findObject(dev.squishName + MCUConst.specifications.MAIN_WEBVIEW)
        except LookupError, e:
            continue
        except Exception, e:
            raise
        
        if dev.deviceModel in ('Sound Sensor', 'Membrane Potentiometer'):
            webviewText = MCUConst.specifications.MAIN_WEBVIEW + '.DOCUMENT.HTML1.BODY1.DIV1.FONT1'
        elif dev.deviceModel in ('Servo', 'LCD'):
            webviewText = MCUConst.specifications.MAIN_WEBVIEW + '.DOCUMENT.HTML1.BODY1.SPAN1'
        elif dev.deviceModel in ('Push Button Toggle Switch', 'Furnace', 'Fire Sensor', 'Door',
                                 'CO2 Detector', 'CO Detector', 'Appliance', 'AC'):
            webviewText = MCUConst.specifications.MAIN_WEBVIEW + '.DOCUMENT.HTML1.BODY1'
        elif dev.deviceModel == 'Fire Monitor':
            webviewText = MCUConst.specifications.MAIN_WEBVIEW + '.DOCUMENT.HTML1.BODY1.DIV1.DIV1.FONT1'
        else:
            webviewText = MCUConst.specifications.MAIN_WEBVIEW + ".DOCUMENT.HTML1.BODY1.FONT1"
        #For items that have different names on the page than their model names
        if dev.deviceModel == 'CO Detector':
            dev.deviceModel = 'Carbon Monoxide Detector'
        if dev.deviceModel == 'CO2 Detector':
            dev.deviceModel = 'Carbon Dioxide Detector'
        if dev.deviceModel == 'Atm Pressure Monitor':
            dev.deviceModel = 'Pressure Sensor'
        if dev.deviceModel == 'Rocker Switch':
            dev.deviceModel = 'Switch'
        if dev.deviceModel == 'Push Button Toggle Switch':
            dev.deviceModel = 'Push Button'
        if dev.deviceModel == 'Air Cooler':
            dev.deviceModel = 'Chiller'
        if dev.deviceModel == 'AC':
            dev.deviceModel = 'Air Conditioner (AC)'
        
        windowText = str(findObject(dev.squishName + webviewText).innerText)
        windowText = windowText.replace('\xa0', ' ')
        
        check(dev.deviceModel in windowText, 'name:' + dev.deviceModel + ' : windowText:' + windowText)
        dev.close()
        snooze(1)
        dev.delete()
    check(len(devList) - len(nonIoeTemplates) == len(ioeTemplates))
    None