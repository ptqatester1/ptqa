##Chris Allen

from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst

class GuiConst:
	NUMBER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_btn"
	PICKUP = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_labelBG"
	HANG_UP = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.labelHandSet"
	STATUS_LABEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.labelInput"
	MI_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_btnMi"
	DO_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_btnDo"
	RE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_btnRe"
	DO_RE_ME_INDICATION = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.m_labelIndicator"
	NUMBER_LABEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.lblNumber"
	FROM_NUMBER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.lblNumber4Digits"
	ANALOG_PHONE_NUMBER_LABEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseAnalogPhoneGUI.labelLineNumber"
	DATE_TIME_LABEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseIPPhoneGUI.lblDateTime"
	PLAYING_MI_LABEL = ":m_guiTab.Playing 'Mi'..._QLabel"
	SCROLLBAR = ".c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_hcontainer.QScrollBar1"

class PhoneConst:
	physical = PhysicalConst
	config = ConfigConst
	gui = GuiConst