#Lesley Tse
#This script tests the directory commands in PC's command prompt

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
    pc0.desktop.applications.commandPrompt()
   
    pc0.desktop.commandPrompt.setText("?")
    pc0.desktop.commandPrompt.setText("<Space>")
    pc0.desktop.commandPrompt.textCheckPoint("  cd           Displays the name of or changes the current directory.")
    pc0.desktop.commandPrompt.textCheckPoint("  delete       Deletes the specified file from C: directory.")
    pc0.desktop.commandPrompt.textCheckPoint("  dir          Displays the list of files  in C: directory.")
    pc0.desktop.commandPrompt.textCheckPoint("  mkdir        Creates a directory.")
    pc0.desktop.commandPrompt.textCheckPoint("  rmdir        Removes a directory.")
    
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.setText("delete sampleFile.txt")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.textCheckPoint("26        sampleFile.txt", 1)  #spacing is off in build 85, so might need to change this if fix comes out
    
    pc0.desktop.commandPrompt.setText("mkdir test")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.textCheckPoint("<DIR>              test", 1)
        
    pc0.desktop.commandPrompt.setText("cd test")
    pc0.desktop.commandPrompt.textCheckPoint("test>")
    
    pc0.desktop.commandPrompt.setText("cd ..")
    pc0.desktop.commandPrompt.setText("rmdir test")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.textCheckPoint("<DIR>              test", 1)  #DE1472
    
    pc0.desktop.commandPrompt.setText("mkdir test2/test3")
    pc0.desktop.commandPrompt.setText("cd test2")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.textCheckPoint("<DIR>              test3", 1)
    pc0.desktop.commandPrompt.setText("cd test3")
    pc0.desktop.commandPrompt.setText("mkdir test4")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.setText("rmdir test4")
    pc0.desktop.commandPrompt.setText("dir")
    pc0.desktop.commandPrompt.textCheckPoint("<DIR>              test4", 1)