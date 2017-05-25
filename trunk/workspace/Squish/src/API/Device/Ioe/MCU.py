##Chris Allen

from API.Device.Ioe.IoeBase import IoeBase

class MCU(IoeBase):
	def __init__(self, p_model, p_x, p_y, p_displayName):
		super(MCU, self).__init__(p_model, p_x, p_y, p_displayName)
		None