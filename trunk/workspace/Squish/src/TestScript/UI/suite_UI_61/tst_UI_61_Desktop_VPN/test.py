##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server

from API.ComponentBox import ComponentBoxConst

util = Util()

p0 = PC(ComponentBoxConst.DeviceModel.PC, 560, 190, 'PC0')

def main():
    util.init()
    openfile()
    checkVpn()
    
def openfile():
    util.open('Desktop_VPN.pkt', UtilConst.UI_TEST)
    util.speedUpConvergence()
    
def checkVpn():
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.vpn()
    p0.desktop.vpn.connectVpn('ciscogroup', 'ciscogroup', '10.3.0.1', 'user', 'pass')
    util.fastForwardTime()
    snooze(2)
    p0.desktop.vpn.popups.vpnIsConnectedOkButton()
    p0.desktop.vpn.disconnectButton()
    util.fastForwardTime()
    test.passes('All buttons working')