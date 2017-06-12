from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API.Workspace.Physical import Physical
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.SBC import SBC

import re
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

sbc0 = SBC('SBC-PT', 95, 190, 'SBC0')
sbc1 = SBC('SBC-PT', 255, 190, 'SBC1')

util = Util()

def main():
    open_sample('7.1/Bluetooth/paired connections.pkt')
    pair_device()
    util.clickOnPhysical()
    move_in_and_out_of_range()
    util.clickOnLogical()
    check_console_output()

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()

def pair_device():
    sbc0.select()
    sbc0.clickConfigTab()
    sbc0.config.selectInterface('Bluetooth')
    sbc0.config.interface.bluetooth.discoverButton()
    util.fastForwardTime()
    sbc0.config.interface.bluetooth.pair(sbc1.displayName)
    sbc0.close()

def move_in_and_out_of_range():
    Physical().goTo('Home City', 'Corporate Office')
    for i in range(10):
        sbc1_obj = Physical().getObject(sbc1.displayName)
        start_point = Point(sbc1_obj.x, sbc1_obj.y)
        new_point = Point(start_point.x + 300, start_point.y)
        util.dragAndDrop(util.currentWorkspace, start_point.x, start_point.y, util.currentWorkspace, new_point.x, new_point.y)
        util.fastForwardTime()
        util.dragAndDrop(util.currentWorkspace, new_point.x, new_point.y, util.currentWorkspace, start_point.x, start_point.y)

def check_console_output():
    for device in [sbc0, sbc1]:
        device.select()
        device.clickProgrammingTab()
        output = device.programming.getConsoleOutput()
        expected_text = ['connected', 'disconnected', 'hello']
        for text in expected_text:
            result = text in output
            msg = 'Expected %s to be in %s. Got %s' % (text, output, result)
            functions.check(result, msg)
        device.close()
        
# Sample Instructions
'''
This file demonstrates Bluetooth paired connections.

1. Go to SBC0's Config tab, Bluetooth interface.
2. Click on Discover, and click on
the first discovered device, and click Pair.
3. Once connected, go to both devices' Programming tab.
4. They are programmed to send messages to each other.
5. Go to Physical view and move them
in and out of range of each other,
and see the outputs.
'''