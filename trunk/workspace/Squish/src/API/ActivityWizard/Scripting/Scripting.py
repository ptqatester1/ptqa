##Chris Allen

from API.MenuBar.Extensions.Scripting.ScriptingBase import ScriptingInterfaceBase

class Scripting(ScriptingInterfaceBase):
    def __init__(self):
        '''Call the super class constructor with the 'aw' parameter to tell it to use the Activity Wizard scripting constants'''
        super(Scripting, self).__init__('aw')