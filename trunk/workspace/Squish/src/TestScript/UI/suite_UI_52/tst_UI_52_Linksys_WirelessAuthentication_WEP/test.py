#Thi
#Bug 14790
from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Utility import UtilConst
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
Access_PointPT = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 119, 214, "Access PointPT")
PC_PT0 = PC(ComponentBoxConst.DeviceModel.PC, 49, 294, "PC_PT0")
PC_PT1 = PC(ComponentBoxConst.DeviceModel.PC, 152, 294, "PC_PT1")

Access_PointA = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_A, 403, 206, "Access PointA")
PC_A0 = PC(ComponentBoxConst.DeviceModel.PC, 368, 324, "PC_A0")
PC_A1 = PC(ComponentBoxConst.DeviceModel.PC, 422, 317, "PC_A1")

Access_PointN = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_N, 641, 24, "Access PointN")
PC_N0 = PC(ComponentBoxConst.DeviceModel.PC, 606, 133, "PC_N0")
PC_N1 = PC(ComponentBoxConst.DeviceModel.PC, 677, 136, "PC_N1")

server0  = Server(ComponentBoxConst.DeviceModel.SERVER, 535, 202, "Server0")
wirelessRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 639, 251, "Wireless Router2")
PC_Linksys0 = PC(ComponentBoxConst.DeviceModel.PC, 598, 345, "PC_Linksys0")
PC_Linksys1 = PC(ComponentBoxConst.DeviceModel.PC, 682, 344, "PC_Linksys1")

IP = "" 

def main():
    util.init()
    openFile()
    global IP
    IP = WEP(IP)
    WEP_encrypt(IP)

def openFile():
    util.open("UI20_WirelessAuthentication.pkt", UtilConst.UI_TEST)
    util.speedUpConvergence()
    util.speedUpConvergence()

def WEP(IP):
    PC_Linksys1.select()
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()
    
    wirelessRouter0.select()
    wirelessRouter0.clickConfigTab()
    wirelessRouter0.config.selectInterface("Wireless")
    wirelessRouter0.config.interface.wireless.wep()
    wirelessRouter0.config.interface.wireless.wepkey("123456789A")
    
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.applications.commandPrompt()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0") 
    PC_Linksys0.config.interface.wireless.wep()
    snooze(2)
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys0.config.interface.wireless.wepkey("123456789A")   

    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0")
    PC_Linksys1.config.interface.wireless.wep()
    snooze(2)
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys1.config.interface.wireless.wepkey("123456789A")  
    PC_Linksys1.close()

    PC_Linksys0.select()
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0")
    PC_Linksys0.config.interface.wireless.disabled()
    PC_Linksys0.config.interface.wireless.wep() #Bug 14790
    snooze(2)
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):

        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys0.config.interface.wireless.wepkey("123456789A")
    PC_Linksys0.close()
    util.speedUpConvergence()
    
    PC_Linksys1.select()
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()
    
    util.speedUpConvergence()
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.applications.commandPrompt()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)
    PC_Linksys0.close()
    return IP

def WEP_encrypt(IP):
    wirelessRouter0.select()
    wirelessRouter0.clickConfigTab()
    wirelessRouter0.config.selectInterface("Wireless")
    snooze(2)
    wirelessRouter0.config.interface.wireless.disabled()
    wirelessRouter0.config.interface.wireless.wep()
    wirelessRouter0.config.interface.wireless.wepkey("1234567891")  
    wirelessRouter0.config.interface.wireless.encryption("104/128-Bits (26 Hex digits)")
    while (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        if object.exists(UtilConst.ERROR_MESSAGE_OK2):
            util.clickButton(UtilConst.ERROR_MESSAGE_OK2)
        if object.exists(UtilConst.ERROR_MESSAGE_OK):
            util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    wirelessRouter0.config.interface.wireless.wepkey("1234567891234567891234567A")

    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.applications.commandPrompt()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0") 
    PC_Linksys0.config.interface.wireless.encryption("104/128-Bits (26 Hex digits)")
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    snooze(2)
    PC_Linksys0.config.interface.wireless.wepkey("1234567891234567891234567A")
    
    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0") 
    PC_Linksys1.config.interface.wireless.encryption("104/128-Bits (26 Hex digits)")
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys1.config.interface.wireless.wepkey("1234567891234567891234567A")
    util.speedUpConvergence()
    util.speedUpConvergence()
    
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    snooze(2)
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()
    
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)
    PC_Linksys0.close()