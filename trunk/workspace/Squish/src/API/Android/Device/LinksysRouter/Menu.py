from API.Android.Device.DeviceBase import DeviceMenuBase
class Menu(DeviceMenuBase):
    def __init__(self):
        self.squishName = ""
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
		super(LinksysRouter, self).updateName(self.squishName)