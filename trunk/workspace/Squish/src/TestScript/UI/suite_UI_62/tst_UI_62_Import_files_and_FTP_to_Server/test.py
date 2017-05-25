######################
#Author: Alex Leung ##
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.MenuBar.File.Open.Open import Open
from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst
from API.functions import pathFromOS
import os

#function initialization
util = Util()
openFile = Open()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 95, 190, "PC0")
PATH = pathFromOS("HTML/import files and ftp to server.pkt")
INSTALL_PATH = os.environ['PT7HOME']
def main():
    util.init()
    maketop()
    step1()
    step2()
    step345()
    step6()

def maketop():
    openFile.openSamples(PATH)
    util.speedUpConvergence()
    
def step1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("2.0.0.3")
    util.fastForwardTime()
    snooze(3)
    pc0.desktop.webBrowser.textCheckPoint("Cisco Packet Tracer\nWelcome to Cisco Packet Tracer. Opening doors to new opportunities. Mind Wide Open.\nQuick Links: \nA small page \nCopyrights \nImage page \nImage")
    pc0.close()
    
def step2():
    pc0.select()
    pc0.desktop.applications.textEditor()
    pc0.desktop.textEditor.importFile(INSTALL_PATH + pathFromOS("/saves/HTML/index.html"))
    pc0.desktop.textEditor.importFile(INSTALL_PATH + pathFromOS("/saves/HTML/styles.css"))
    pc0.desktop.textEditor.importFile(INSTALL_PATH + pathFromOS("/saves/HTML/myjs.js"))
    pc0.close()
    
def step345():
    pc0.select()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ftp 2.0.0.3")
    util.fastForwardTime()
    pc0.desktop.commandPrompt.setText("cisco")
    pc0.desktop.commandPrompt.setText("cisco")
    pc0.desktop.commandPrompt.setText("cd /http")
    pc0.desktop.commandPrompt.setText("put index.html")
    util.fastForwardTime()
    pc0.desktop.commandPrompt.setText("put styles.css")
    util.fastForwardTime()
    pc0.desktop.commandPrompt.setText("put myjs.js")
    util.fastForwardTime()
    pc0.desktop.commandPrompt.close()
    snooze(1)
    
def step6():
    pc0.select()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("2.0.0.3")
    util.fastForwardTime()
    #checkpoint
    pc0.desktop.webBrowser.textCheckPoint("Cisco Packet Tracer\nWelcome to Cisco Packet Tracer. Opening doors to new opportunities. Mind Wide Open.\nQuick Links: \nA small page \nCopyrights \nImage page \nImage \nClick Me!")
    pc0.close()
