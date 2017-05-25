##Chris Allen

from API.MenuBar.Options.Preferences.CustomInterfaces.CustomInterfacesConst import CustomInterfacesConst
from API.Utility.Util import Util

class CustomInterfaces:
    def __init__(self):
        self.util = Util()
    
    @property
    def treeWidget(self):
        return findObject(CustomInterfacesConst.TREE)
    
    def interfaceDropdownFor(self, device):
        '''Iterate through the device tree until the device with a matching name is found
        return the combo box next to it'''
        for i in range(self.treeWidget.topLevelItemCount):
            currentObjectName = CustomInterfacesConst.TREE + '.item_' + str(i) + '/0'
            for j in range(len(object.children(findObject(currentObjectName)))):
                currentDeviceObjectName = currentObjectName + '.item_' + str(j) + '/0'
                if findObject(currentDeviceObjectName).text == device:
                    return findObject(currentDeviceObjectName[:-1]+'1')#Replace 0 with 1 at end
        raise ValueError('Could not find device named: ' + device)
    
    
    def selectInterfaceFor(self, device, interface):
        self.util.clickItem(self.interfaceDropdownFor(device), interface)