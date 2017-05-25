from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.SimulationPanel.EventList.EventList import EventList
from API.SimulationPanel.EventList.EventListConst import EventListConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControls import PlayControls
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 300, 100, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 200, "Router2")

def main():
    util.init()
    createTopology()
    util.clickOnSimulation()
    util.clickOnRealtime()
    configRouters()
    checkPoint()

def createTopology():
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(router1.x, router1.y, router2.x, router2.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(router2.x, router2.y, router0.x, router0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configRouters():
    for router in [router0, router1, router2]:
        router.select()
        router.clickCliTab()
        router.cli.startConsole()
        router.cli.setCliText("enable")
        router.cli.setCliText("configure terminal")
        router.cli.setCliText("interface fastethernet0/0")
        router.cli.setCliText("no shutdown")
        router.cli.setCliText("exit")
        router.cli.setCliText("interface fastethernet0/1")
        router.cli.setCliText("no shutdown")
        router.cli.setCliText("end")
        router.close()
        
def checkPoint():
    util.clickOnSimulation()
    
    eventListFilters.checkFilters('CDP', clearFilters=True)
    
    EventList().waitForEvent('Router1', 'Router2', 'CDP', 5)
    EventList().selectEvent('Router1', 'Router2', 'CDP')
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "The frame is a CDP frame. The CDP process processes it.")
    util.close(PDUConst.PDU_WINDOW)

    EventList().constantDelayCheckbox(False)

    PlayControls().captureForward(2)
    snooze(5)
    util.clickOnWorkspace(router1.x -10, router1.y + 15)
    snooze(5)

    if (object.exists(PDUConst.NO_PDU_INFO_POPUP_LABEL)):
        util.textCheckPoint(PDUConst.NO_PDU_INFO_POPUP_LABEL, "This PDU is in transit.")
    else:
        util.clickOnWorkspace(router0.x + 10, router0.y + 10)
        util.textCheckPoint(PDUConst.NO_PDU_INFO_POPUP_LABEL, "This PDU is in transit.")