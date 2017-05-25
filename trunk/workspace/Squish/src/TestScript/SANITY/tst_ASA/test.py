##Chris Allen
##Adding ASA to API

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Device.Security.Asa import Asa

from API.Device.Switch import Switch




util = Util()

asa = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, "Asa0")

def main():
    util.createDevice(ComponentBoxConst.DeviceType.SECURITY, asa.model, asa.x, asa.y)
    checkCLI()
    checkConfigSettings()
    #checkAlgorithmSettings()
    checkVlanDatabase()
    checkEthernet()
        
    
def checkCLI():
    util.clickOnWorkspace(asa.x, asa.y)
    asa.updateName()
    asa.clickCliTab()
    snooze(10)
    asa.cli.startConsole()
    asa.cli.setCliText("enable")
    asa.cli.setCliText("")
    asa.cli.setCliText("configure terminal")
    
def checkConfigSettings():
    asa.clickConfigTab()
    asa.config.selectInterface("Settings")
    asa.config.settings.displayName(asa.displayName)
    asa.config.settings.hostname(asa.displayName)
    asa.config.exportStartUpConfig(util.getFilePath("AsaConfig.txt", UtilConst.SANITY_TEST), AsaConst.Config.Settings.STARTUP_CONF_EXPORT_OK)
    asa.config.saveNVRam()
    asa.config.eraseNVRam()
    asa.config.loadStartUpConfig(util.getFilePath("AsaConfig.txt", UtilConst.SANITY_TEST), AsaConst.Config.Settings.STARTUP_CONF_LOAD_OK)
    asa.config.mergeRunningConfig(util.getFilePath("AsaConfig.txt", UtilConst.SANITY_TEST), AsaConst.Config.Settings.RUNNING_CONF_MERGE_CANCEL)
    asa.config.exportRunningConfig(util.getFilePath("AsaConfig.txt", UtilConst.SANITY_TEST), AsaConst.Config.Settings.RUNNING_CONF_EXPORT_CANCEL)
    
def checkAlgorithmSettings():
    asa.config.selectInterface("Algorithm Settings")
    snooze(5)
    asa.clickButton(AsaConst.Config.AlgorithmSettings.GLOBAL_SETTINGS_CHECKBOX)
    asa.config.setHalfOpenSessionMult("5")
    asa.config.setMaxNumConnections("100")
    asa.config.setMaxNumOpenedSessions("1000")
    asa.config.setMaxRetransmission("1000")
    
def checkVlanDatabase():
    asa.config.selectInterface("VLAN Database")
    asa.config.addVlan("NewVlan", "99")
    asa.config.removeVlan("99", "NewVlan")
    asa.config.addVlan("Vlan3", "3")
    
def checkEthernet():
    asa.config.selectInterface("Ethernet0/0")
    asa.config.selectTrunk()
    asa.config.selectInterface("Ethernet0/1")
    asa.config.selectAccess()
    