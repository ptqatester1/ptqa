##Chris Allen

from API.Device.Ioe.IoeBase import IoeBase
from API.Device.DeviceBase.DesktopBase.DesktopBase import Desktop

class SBC(IoeBase):
	def __init__(self, p_model, p_x, p_y, p_displayName):
		super(SBC, self).__init__(p_model, p_x, p_y, p_displayName)
		self.desktop = Desktop(self)
	
	def updateName(self):
		super(SBC, self).updateName()
		self.desktop.updateName(self.squishName)
		None