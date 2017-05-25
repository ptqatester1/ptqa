#**************************************************************************
#@author: Thi Nguyen
#@summary: IPC 
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.Utility.Util import Util
from API.IPC.IPCConst import IPCConst
from squish import *

class IPC(SquishSyntax):
   
    #@summary: set port for IPCTest
    def setPort(self, p_port):
        self.setText(IPCConst.PORT_TEXTFIELD, p_port)

        
    #@summary: set application id for IPCTest
    def setAppID(self, p_app_id):
        self.setText(IPCConst.APP_ID_TEXTFIELD, p_port)

      
    #@summary: set key for IPCTest  
    def setKey(self, p_key):
        self.setText(IPCConst.KEY_TEXTFIELD, p_port)

     
    #@summary: press the connect button to connect to PT
    def connectToPT(self, p_port = "39000", p_app_id = "net.netacad.cisco.ipctest" , p_key = "cisco"):
        self.setText(IPCConst.PORT_TEXTFIELD, p_port)
        print p_port
        self.setText(IPCConst.APP_ID_TEXTFIELD, p_app_id)
        self.setText(IPCConst.KEY_TEXTFIELD, p_key)
        self.clickButton(IPCConst.CONNECT_BUTT)
        snooze(7)
        self.clickButton(IPCConst.CONNECT_OK_BUTT)
        
    #@summary: set IpcCall for IPCTest
    def sendIpcCall(self, p_ipc_call):
        self.setText(IPCConst.IPC_CALL_TEXTFIELD, p_ipc_call)
        self.clickButton(IPCConst.SEND_BUTT)
        
    #@summary: check output of IPC call
    def checkpointHistory(self, p_check_string, p_occurrenceNum = -1):
        snooze(2)
        consoleText = str(findObject(IPCConst.HISTORY_TEXTFIELD).plainText)
        self.textCheckPoint(consoleText, p_check_string, p_occurrenceNum)

        