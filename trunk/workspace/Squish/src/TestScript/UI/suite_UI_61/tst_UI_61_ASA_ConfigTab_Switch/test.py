##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    create()
    checkAddVlan()
    checkRemoveVlan()

def create():
    a0.create()
    util.fastForwardTime()

def checkAddVlan():
    a0.select()
    a0.clickConfigTab()
    a0.config.selectInterface('VLAN Database')
    a0.config.vlan.addVlan('dmz', '3')
    a0.config.vlan.check.vlanTableRow('dmz', '3', 2)
    
def checkRemoveVlan():
    a0.config.vlan.removeVlanName('dmz')
    functions.check(a0.config.vlan.vlanTable.rowCount == 2)