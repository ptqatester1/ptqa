from API.Device.DeviceBase.DeviceBase import SquishObjectName

class ConstantsHelper(SquishObjectName):
    def __init__(self):
        SquishObjectName.__init__(self)
    
    def replace_string_in_obj_name(self, string, string_to_replace, replacement_string):
        return string.replace(string_to_replace, replacement_string)
        
    def objName(self, obj):
        if self.isRouter:
            return SquishObjectName.objName(self, obj)
        else:
            original_obj_name = '.m_guiTab.'
            replacement_obj_name = '.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.CDesktopApplet1.CWorkstationWebBrowserBase.'
            object_name = SquishObjectName.objName(self, obj)
            return self.replace_string_in_obj_name(object_name, original_obj_name, replacement_obj_name)