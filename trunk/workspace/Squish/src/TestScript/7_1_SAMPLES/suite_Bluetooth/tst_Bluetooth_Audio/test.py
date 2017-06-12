from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions

from API.Device.Ioe.MCU import MCU

portable_music_player = MCU('Music Player', 20, 190, 'IoE0')
bluetooth_speaker = MCU('Speaker', 280, 205, 'IoE1')

util = Util()

def main():
    open_sample()
    pair_with_speaker()
    check_music_palying()
    
def open_sample():
    util.init()
    Open().openSamples(functions.pathFromOS('7.1/Bluetooth/Bluetooth Audio.pkt'))
    for i in range(5):
        util.speedUpConvergence()

def pair_with_speaker():
    portable_music_player.select()
    portable_music_player.clickConfigTab()
    portable_music_player.config.selectInterface('Bluetooth')
    portable_music_player.config.interface.bluetooth.discoverButton()
    util.fastForwardTime() # Need to Fast Forward here or the table will show 0 elements in the next call
    portable_music_player.config.interface.bluetooth.pair(bluetooth_speaker.displayName)
    portable_music_player.close()

def check_music_palying():
    portable_music_player.deviceInteraction()
    bluetooth_speaker.select()
    bluetooth_speaker.clickProgrammingTab()
    util.fastForwardTime()
    portable_music_player.deviceInteraction()
    output = bluetooth_speaker.programming.getConsoleOutput()
    expected_text = 'Sounds/crickets.wav'
    result = expected_text in output
    msg = 'Expected %s to be in %s. Got %s' % (expected_text, output, result)
    functions.check(result, msg)

# Sample Instructions
'''
1. Go to the Bluetooth interface on Portable Music Player

2. Click Discover and Pair with the Bluetooth Speaker

3. ALT-click on the Portable Music Player to enable it
and to hear the white noise music playing wirelessly via Bluetooth
(turn up your computer volume)
'''