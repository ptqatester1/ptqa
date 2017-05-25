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
    IP = get(IP)
    IP = WPA_PSK(IP)
    IP = WPA_PSK_encrypt(IP)
    IP = WPA2_PSK(IP)
    WPA2_PSK_encrypt(IP)

def openFile():
    util.open("UI20_WirelessAuthentication-2.pkt", UtilConst.UI_TEST)
    util.speedUpConvergence()
    util.speedUpConvergence()

def get(IP):
    
    util.clickOnWorkspace(PC_Linksys1.x, PC_Linksys1.y)
    PC_Linksys1.select()
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()
    return IP
    
    
def WPA_PSK(IP):
    wirelessRouter0.select()
    wirelessRouter0.clickConfigTab()
    wirelessRouter0.config.selectInterface("Wireless")
    wirelessRouter0.config.interface.wireless.wpapsk()
    wirelessRouter0.config.interface.wireless.pskPassPhrase("evilevil")
    
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.applications.commandPrompt()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0")
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0") 
    PC_Linksys0.config.interface.wireless.wpapsk()
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys0.config.interface.wireless.pskPassPhrase("evilevil")
    PC_Linksys0.config.interface.wireless.encryption("AES")
    
    
    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0") 
    PC_Linksys1.config.interface.wireless.wpapsk()
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys1.config.interface.wireless.pskPassPhrase("evilevil")
    PC_Linksys1.config.interface.wireless.encryption("AES")
    util.speedUpConvergence()
    util.speedUpConvergence()
    
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()    

    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)
    return IP
    

def WPA_PSK_encrypt(IP):   
    wirelessRouter0.select()
    wirelessRouter0.config.interface.wireless.encryption("TKIP")

    PC_Linksys0.select()
    
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0")
    PC_Linksys0.config.interface.wireless.encryption("TKIP")

    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0")
    PC_Linksys1.config.interface.wireless.encryption("TKIP")
    util.speedUpConvergence()
    util.speedUpConvergence()
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()    

    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)
    PC_Linksys0.close()
    return IP

def WPA2_PSK(IP):
    wirelessRouter0.select()
    wirelessRouter0.config.interface.wireless.wpa2psk()
    wirelessRouter0.config.interface.wireless.pskPassPhrase("evilevil")

    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.applications.commandPrompt()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 3)
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0") 
    PC_Linksys0.config.interface.wireless.wpa2psk()
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys0.config.interface.wireless.pskPassPhrase("evilevil")
    PC_Linksys0.config.interface.wireless.encryption("TKIP")

    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0") 
    PC_Linksys1.config.interface.wireless.wpa2psk()
    while (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    PC_Linksys1.config.interface.wireless.pskPassPhrase("evilevil")
    PC_Linksys1.config.interface.wireless.encryption("TKIP")
    util.speedUpConvergence()
    util.speedUpConvergence()
    
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()    
    
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 3)
    return IP

def WPA2_PSK_encrypt(IP):   
    wirelessRouter0.select()
    wirelessRouter0.config.interface.wireless.encryption("AES")

    PC_Linksys0.select()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 4)
    PC_Linksys0.clickConfigTab()
    PC_Linksys0.config.selectInterface("Wireless0")
    PC_Linksys0.config.interface.wireless.encryption("AES")

    PC_Linksys1.select()
    PC_Linksys1.clickConfigTab()
    PC_Linksys1.config.selectInterface("Wireless0")
    PC_Linksys1.config.interface.wireless.encryption("AES")
    util.speedUpConvergence()
    util.speedUpConvergence()
    PC_Linksys1.clickDesktopTab()
    PC_Linksys1.desktop.applications.ipConfiguration()
    IP = PC_Linksys1.desktop.ipConfiguration.getIp()
    PC_Linksys1.close()    
    
    PC_Linksys0.select()
    PC_Linksys0.clickDesktopTab()
    PC_Linksys0.desktop.commandPrompt.setText("ping "+ IP)
    util.speedUpConvergence()
    PC_Linksys0.desktop.commandPrompt.textCheckPoint("Received = 0", 4)
    PC_Linksys0.close()