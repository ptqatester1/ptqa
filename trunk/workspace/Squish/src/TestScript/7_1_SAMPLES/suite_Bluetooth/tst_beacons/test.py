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

beacon0 = MCU('Beacon', 120, 80, 'Beacon0')
beacon1 = MCU('Beacon', 325, 85, 'Beacon1')
sbc = SBC('SBC-PT', 230, 245, 'SBC0')

util = Util()

def main():
    open_sample('7.1/Bluetooth/beacons.pkt')
    util.clickOnPhysical()
    move_beacons_in_range()
    util.clickOnLogical()
    check_beacon_receives_data()

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()

def move_beacons_in_range():
    Physical().goTo('Home City', 'Corporate Office')
    beacon0_obj = Physical().getObject('Beacon0')
    beacon1_obj = Physical().getObject('Beacon1')
    sbc_obj = Physical().getObject('SBC0')
    new_sbc_loc = Point(350, 200)
    left_of_sbc_loc = Point(325, 200)
    right_of_sbc_loc = Point(375, 200)
    util.dragAndDrop(util.currentWorkspace, sbc_obj.x, sbc_obj.y, util.currentWorkspace, new_sbc_loc.x, new_sbc_loc.y)
    util.dragAndDrop(util.currentWorkspace, beacon0_obj.x, beacon0_obj.y, util.currentWorkspace, left_of_sbc_loc.x, left_of_sbc_loc.y)
    util.dragAndDrop(util.currentWorkspace, beacon1_obj.x, beacon1_obj.y, util.currentWorkspace, right_of_sbc_loc.x, right_of_sbc_loc.y)

def check_beacon_receives_data():
    for i in range(5):
        util.speedUpConvergence() # Give the beacons plenty of time to send signals
    sbc.select()
    sbc.clickProgrammingTab()
    output = sbc.programming.getConsoleOutput()
    matches_set = set(re.findall('received beacon from [\dA-F]{4}\.[\dA-F]{4}\.[\dA-F]{4}', output))
    unique_matches = len(matches_set)
    msg = 'Expected two unique matchs. Got %s' % (unique_matches)
    functions.check(unique_matches == 2, msg)

# Sample instructions
'''
This network demonstrates Bluetooth
beacons broadcasting and monitoring.

1. Go to Physical view and
move the SBC around to be
in range of the beacons.
2. Go back to Logical view
and see the Bluetooth broadcast
link between the beacons
and the SBC.
3. Open the SBC's Programming tab
and see it receiving beacon data.
'''