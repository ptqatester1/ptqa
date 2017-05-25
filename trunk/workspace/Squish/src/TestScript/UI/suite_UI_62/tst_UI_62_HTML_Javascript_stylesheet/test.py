######################
#Author: Alex Leung ##
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.MenuBar.File.Open.Open import Open
from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server

import os
from API.functions import pathFromOS

#function initialization
util = Util()
openFile = Open()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 85, 155, "PC0")
se0 = Server(ComponentBoxConst.DeviceModel.SERVER, 270, 145, "Server0")

def main():
    util.init()
    maketop()
    functions()
    checkpoint()

def maketop():
    openFile.openSamples(pathFromOS("HTML/html_javascript_stylesheet.pkt"))
    util.speedUpConvergence()
    
def functions():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("http://1.1.1.1")

def checkpoint():
    pc0.desktop.webBrowser.textCheckPoint("Click Me for Inline Javascript Test", 1)
    pc0.desktop.webBrowser.textCheckPoint("HTML page with an external javascript file \(index2.html\)", 1)
    pc0.desktop.webBrowser.textCheckPoint("HTML page with an external stylesheet file \(index3.html\)", 1)
    pc0.desktop.webBrowser.textCheckPoint("HTML page with both external javascript and stylesheet files \(index4.html\)", 1)
    pc0.desktop.webBrowser.textCheckPoint("Image page\: Test for a previously saved file with the image file in the directory of the pkt file", 1)
    pc0.desktop.webBrowser.textCheckPoint("Image page\: Test for with the image file imported in the PT Server", 1)
