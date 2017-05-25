########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

import os

#function initialization
util = Util()

pc = PC(ComponentBoxConst.DeviceModel.PC, 71, 108, "pc")    

def main():
    util.init()
    maketop()
    checkpoint()    

def maketop():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc.model, pc.x, pc.y)
        
def checkpoint():    
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.clickDesktopTab()
    pc.desktop.applications.commandPrompt()
    pc.desktop.commandPrompt.setText("mkdir test1/test2")
    pc.desktop.commandPrompt.setText("dir")
    pc.desktop.commandPrompt.textCheckPoint('''C:\\\\>dir
\s
 Volume in drive C has no label\.
 Volume Serial Number is [\dA-F]+-[\dA-F]+
 Directory of C:\\\\

\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{1,2} (AM|PM) \s+26 \s+sampleFile.txt      
\d{1,2}/\d{1,2}/\d{4}\s+\d{1,2}:\d{1,2} (AM|PM) \s+<DIR> \s+test1               
\s+90 bytes \s+2 File\(s\)''')
    pc.desktop.commandPrompt.setText("cd test1/test2")
    pc.desktop.commandPrompt.textCheckPoint("C:\\\\test1\\\\test2>")
    pc.desktop.commandPrompt.setText("cd ..")
    pc.desktop.commandPrompt.textCheckPoint("C:\\\\test1>")
    pc.desktop.commandPrompt.setText("dir")
    pc.desktop.commandPrompt.textCheckPoint('''C:\\\\test1>dir
\s
\sVolume in drive C has no label.
\sVolume Serial Number is [\dA-F]{1,4}-[\dA-F]{1,4}
\sDirectory of C:\\\\test1

\d{1,2}/\d{1,2}/\d{4} \s+\d{1,2}:\d{1,2} (AM|PM)\s*<DIR>\s*test2\s*
\s*0 bytes\s*1 File\(s\)''')
    pc.desktop.commandPrompt.setText("cd ..\..")
    pc.desktop.commandPrompt.textCheckPoint("C:\\\\test1>cd \.\.\\\\\.\.")
    pc.desktop.commandPrompt.setText("rmdir test1/test2")
    pc.desktop.commandPrompt.setText("cd test1/test2")    
    pc.desktop.commandPrompt.textCheckPoint("The system cannot find the path specified.") 
    pc.close()