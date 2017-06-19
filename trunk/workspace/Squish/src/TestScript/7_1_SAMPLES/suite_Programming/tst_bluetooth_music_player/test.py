from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions
from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC
from API.Device.Ioe.MCU import MCU

util = Util()

smartphone = PC(ComponentBoxConst.DeviceModel.PDA, 40, 80, 'Smartphone0')
speaker = MCU('Speaker', 85, 260, 'IoE0')

def main():
    open_sample('7.1/Programming/bluetooth music player.pkt')
    turn_on_bluetooth()
    pair_with_speaker()
    play()
    stop()
    check_sound_played()

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()

def turn_on_bluetooth():
    smartphone.select()
    smartphone.clickConfigTab()
    smartphone.config.selectInterface('Bluetooth')
    smartphone.config.interface.bluetooth.portStatus()
    util.speedUpConvergence()
    
def pair_with_speaker():
    smartphone.config.interface.bluetooth.discoverButton()
    snooze(1)
    smartphone.config.interface.bluetooth.pair('IoE0')
    snooze(1)
    util.speedUpConvergence()
    
def play():
    smartphone.clickDesktopTab()
    util.clickButton(smartphone.squishName + '.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.m_desktopFrame.GUI Example_btn')
    util.click(get_play_button())
    snooze(1)
    util.speedUpConvergence()
    
def stop():
    util.click(get_play_button())
    smartphone.close()

def check_sound_played():
    speaker.select()
    speaker.clickProgrammingTab()
    output = speaker.programming.getConsoleOutput()
    expected_text = '/Sounds/crickets.wav'
    condition = expected_text in output
    msg = 'Expected %s to be in %s. Got %s' % (expected_text, output, condition)
    functions.check(condition, msg)
    
def get_play_button():
    webview = smartphone.squishName + '.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1.CBaseWorkstationCustomApp.m_customWebView.DOCUMENT.HTML1.BODY1'
    return functions.WebviewTagFind2().findTagWithProperties(webview, 'BUTTON', {'innerText':'Play/Stop'})