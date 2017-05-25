######################
#@author: Pamela Vinco
######################

from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Device.Hub.Hub import Hub
from API.Device.EndDevice.TV.TV import TV
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.VoIP.VoIP import VoIP
from API.Device.EndDevice.IPPhone.IPPhone import IPPhone
from API.Device.DeviceBase import DeviceBaseConst

util = Util()

#Device initialization
phone = IPPhone(ComponentBoxConst.DeviceModel.ANALOG_PHONE, 100, 100, "Analog Phone0")
tv = TV(ComponentBoxConst.DeviceModel.TV, 100, 200, "TV0")
tablet = PC(ComponentBoxConst.DeviceModel.TABLET_PC, 100, 300, "TabletPC0")
pda = PC(ComponentBoxConst.DeviceModel.PDA, 200, 100, "Pda0")
voip = VoIP(ComponentBoxConst.DeviceModel.VOIP, 200, 200, "Home VoIP0")
wired = PC(ComponentBoxConst.DeviceModel.WIRED_END_DEVICE, 200, 300, "Wired End Device0")
wireless = PC(ComponentBoxConst.DeviceModel.WIRELESS_END_DEVICE, 300, 100, "Wireless End Device0")
coaxial = Hub(ComponentBoxConst.DeviceModel.COAXIAL_SPLITTER_PT, 300, 200, "CoAxialSplitter0")

def main():       
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, phone.model, phone.x, phone.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, tv.model, tv.x, tv.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, tablet.model, tablet.x, tablet.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pda.model, pda.x, pda.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, voip.model, voip.x, voip.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, wired.model, wired.x, wired.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, wireless.model, wireless.x, wireless.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, coaxial.model, coaxial.x, coaxial.y)
    
def checkpoint():
    phone.exists()
    tv.exists()        
    tablet.exists()
    pda.exists()
    voip.exists()
    wired.exists()
    wireless.exists()       
    coaxial.exists()