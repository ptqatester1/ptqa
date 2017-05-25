from API.Device.DeviceBase.WirelessGuiBase.Gui import GuiBase

class Gui(GuiBase):
	def __init__(self, parent):
		super(Gui, self).__init__(parent, isRouter=False)
	