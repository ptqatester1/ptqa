from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    pc0.create()

def checkpoint():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.textCheckPoint("")
    pc0.desktop.webBrowser.browse("127.0.0.1")
    util.speedUpConvergence()
    util.speedUpConvergence()
    pc0.desktop.webBrowser.textCheckPoint("Request Timeout")
    pc0.desktop.webBrowser.browse("www.test.com")
    util.speedUpConvergence()
    util.speedUpConvergence()
    pc0.desktop.webBrowser.textCheckPoint("Host Name Unresolved")
    pc0.desktop.webBrowser.back()
    pc0.desktop.webBrowser.check.url("127.0.0.1")
    pc0.desktop.webBrowser.forward()
    pc0.desktop.webBrowser.check.url("www.test.com")