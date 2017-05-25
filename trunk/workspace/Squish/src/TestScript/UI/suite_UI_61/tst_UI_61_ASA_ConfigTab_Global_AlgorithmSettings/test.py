##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.ComponentBox import ComponentBoxConst

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    create()
    checkDefaults()
    checkChangedValues()
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.SECURITY, a0.model, a0.x, a0.y)
    util.fastForwardTime()
    
def checkDefaults():
    util.clickOnWorkspace(a0.x, a0.y)
    a0.updateName()
    a0.clickConfigTab()
    a0.config.selectInterface('Algorithm Settings')
    a0.config.algorithmSettings.check.globalSettings(True)
    a0.config.algorithmSettings.check.halfOpenSessionMultiplier('1')
    a0.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=False)
    a0.config.algorithmSettings.check.maxConnections('100')
    a0.config.algorithmSettings.check.maxConnections(None, property='enabled', value=False)
    a0.config.algorithmSettings.check.maxRetransmission('1000')
    a0.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=False)
    
def checkChangedValues():
    a0.config.algorithmSettings.globalSettings(False)
    a0.config.algorithmSettings.halfOpenSessionMultiplier('10')
    a0.config.algorithmSettings.maxConnections('10')
    a0.config.algorithmSettings.maxRetransmission('10')
    
    
    a0.config.algorithmSettings.check.globalSettings(False)
    a0.config.algorithmSettings.check.halfOpenSessionMultiplier('10')
    a0.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=True)
    a0.config.algorithmSettings.check.maxConnections('10')
    a0.config.algorithmSettings.check.maxConnections(None, property='enabled', value=True)
    a0.config.algorithmSettings.check.maxRetransmission('10')
    a0.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=True)