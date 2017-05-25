########################
##Author: AbbasH
########################

from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Device.Router.Router import Router
from API.Device.Switch.Switch import Switch
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.ActivityWizard.InitialNetwork.InitialNetworkConst import InitialNetworkConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst

util = Util()

r = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 30, 182, "Router0")
s = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 130, 182, "Switch0")

def main():
    util.init()
    maketop()
    checkpoint()

    
def maketop():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r.model, r.x, r.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s.model, s.x, s.y)
    util.speedUpConvergence()

def checkpoint():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    snooze(1)
    util.clickButton(MainToolbarConst.USE_AS_ANSWER_NETWORK_YES)    
    util.clickButton(ActivityWizardConst.INITIAL_NETWORK)
    util.clickButton(InitialNetworkConst.COPY_FROM_ANSWER_NETWORK)
    util.clickButton(InitialNetworkConst.COPY_FROM_ANSWER_NETWORK_DIALOG_YES)
    util.clickItem(InitialNetworkConst.LOCKING_ITEMS_TREE, "Locking.Topology.Existing Devices.Router0.Use CLI Tab")
    util.clickItem(InitialNetworkConst.LOCKING_ITEMS_TREE, "Locking.Topology.Existing Devices.Router0.Use Config Tab")
    util.clickItem(InitialNetworkConst.LOCKING_ITEMS_TREE, "Locking.Topology.Existing Devices.Switch0.Use CLI Tab")
    util.clickItem(InitialNetworkConst.LOCKING_ITEMS_TREE, "Locking.Topology.Existing Devices.Switch0.Use Config Tab")

