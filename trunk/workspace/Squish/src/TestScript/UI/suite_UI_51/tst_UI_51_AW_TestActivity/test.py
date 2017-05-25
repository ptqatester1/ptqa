#Balaji

from API.Device.EndDevice.PC.PC import PC
from API.Device.Router.Router import Router
from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst
from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Utility import UtilConst


from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst

util = Util()

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 319, 106, "Border1")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 309, 194, "Border2")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 98, 106, "PC0")

def main():
    util.open("D3_5_1_5_2.pka", UtilConst.DISCOVERY3_TEST)
    step1()
    step2()
    reset()
    checkPoint()
def step1():
    
    r1.select()
    snooze(3)
    r1.clickCliTab()
    r1.cli.setCliText("\r") 
    r1.cli.setCliText("enable")
    r1.cli.setCliText("sh ip route")
    r1.cli.textCheckPoint("Gateway of last resort is not set")
    r1.cli.setCliText("config t")
    r1.cli.setCliText("ip route 0.0.0.0 0.0.0.0 172.16.2.1")
    r1.cli.setCliText("end")
    r1.cli.setCliText("copy running-config startup-config")
    r1.cli.setCliText("\r")
    


    r2.select()
    snooze(3)
    r2.clickCliTab()
    r2.cli.setCliText("\r") 
    r2.cli.setCliText("enable")
    r2.cli.setCliText("sh ip route")
    r2.cli.textCheckPoint("Gateway of last resort is not set")
    r2.cli.setCliText("config t")
    r2.cli.setCliText("ip route 0.0.0.0 0.0.0.0 s0/1/1")
    r2.cli.setCliText("end")
    r2.cli.setCliText("copy running-config startup-config")
    r2.cli.setCliText("\r")
    
    
def step2():
    r1.select()
    snooze(3)
    r1.clickCliTab()
    r1.cli.setCliText("\r") 
    r1.cli.setCliText("sh ip route")
    r1.cli.textCheckPoint("172.16.2.1")
    
    r2.select()
    snooze(3)
    r2.clickCliTab()
    r2.cli.setCliText("\r") 
    r2.cli.setCliText("sh ip route")
    r2.cli.textCheckPoint("0.0.0.0")
    
    util.speedUpConvergence()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()     
    pc0.desktop.commandPrompt.setText("ping 10.10.10.250")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Reply from 10.10.10.250")


def reset():
    util.clickButton(TestActivityConst.RESET_ACTIVITY)
    util.clickButton(TestActivityConst.RESET_ACTIVITY_DIALOG_OK)
def checkPoint():
    snooze(15)
    util.textCheckPoint(TestActivityConst.INSTRUCTION_BOX_PROGRESS_LABEL, "Completion: 0%")

