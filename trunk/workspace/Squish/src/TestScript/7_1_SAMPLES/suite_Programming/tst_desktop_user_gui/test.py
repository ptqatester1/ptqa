from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions
from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')

def main():
    open_sample('7.1/Programming/desktop user gui.pkt')
    select_gui_example()
    increment_clicks()
    check_click_counter()
    enter_cli_command()
    check_response()

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()

def select_gui_example():
    pc0.select()
    pc0.clickDesktopTab()
    gui_example_button = '%s.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.m_desktopFrame.GUI Example_btn' % (pc0.squishName)
    util.clickButton(gui_example_button)

def increment_clicks():
    snooze(1)
    util.click(get_click_button())
    snooze(1)
    
def check_click_counter():
    util.textCheckPoint(get_webview(), 'count 2')

def enter_cli_command():
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText('example_cmd 1 2 3')

def check_response():
    pc0.desktop.commandPrompt.textCheckPoint('cliEvent: invoked,["example_cmd","1","2","3"]', escape=True)

def get_webview():
    return pc0.squishName + '.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1.CBaseWorkstationCustomApp.m_customWebView.DOCUMENT.HTML1.BODY1'

def get_click_button():
    return functions.WebviewTagFind2().findTagWithProperties(get_webview(), 'BUTTON', {'innerText':'Click'})