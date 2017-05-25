from API.Toolbar.CommonToolsBar.ComplexPDUWindow import ComplexPDUWindow 
from API.Toolbar.CommonToolsBar.ComplexPDUWindowConst import ComplexPDUWindowConst 
from API.Device.EndDevice.PC.PC import PC 
 
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar 
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst 
from API.Utility.Util import Util 
from API.ComponentBox import ComponentBoxConst 
from API.UserCreatedPacketWindow.UserCreatedPDUListConst import UserCreatedPDUListConst

#Function initialization
complexPDUWindow = ComplexPDUWindow() 
util = Util() 
common = CommonToolsBar() 

#Device initialization
Host1 = PC(ComponentBoxConst.DeviceModel.PC, 124, 93, "PC0") 
Host2 = PC(ComponentBoxConst.DeviceModel.PC, 568, 104, "PC1") 
 
def main(): 
    util.init() 
    createTopology() 
    configPCs() 
    checkPoint1() 
    checkPoint2() 
    checkPoint3() 
    checkPoint4() 
    checkPoint5() 
    createComplexPing() 
    checkPoint6() 
 
def createTopology(): 
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,Host1.model,Host1.x,Host1.y) 
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,Host2.model,Host2.x,Host2.y) 
    util.connect(Host1.x, Host1.y, Host2.x, Host2.y, ComponentBoxConst.Connection.CONN_AUTO,"" , "") 
 
def configPCs(): 
    Host1.select() 
    Host1.updateName() 
    Host1.clickDesktopTab() 
    Host1.desktop.applications.ipConfiguration() 
    Host1.desktop.ipConfiguration.setIPConfiguration("192.168.1.1", "255.255.255.0", "" , "") 
    Host1.desktop.ipConfiguration.close() 
    Host1.close() 
 
    util.clickOnWorkspace(Host2.x, Host2.y) 
    Host2.updateName() 
    Host2.clickDesktopTab()  
    Host2.desktop.applications.ipConfiguration()  
    Host2.desktop.ipConfiguration.setIPConfiguration("192.168.1.2", "255.255.255.0","" , "")  
    Host2.desktop.ipConfiguration.close()  
    Host2.close()  
  
def checkPoint1():  
    util.clickButton(CommonToolsBarConst.ADD_COMPLEX_PDU)  
    Host1.select()  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.TIME_TO_LIVE, "32")
  
def checkPoint2():  
    snooze(1)  
    test.compare(findObject(ComplexPDUWindowConst.OUTGOING_PORT_LIST).count, 1)  
  
def checkPoint3():  
    snooze(1)  
    test.compare(findObject(ComplexPDUWindowConst.APPLICATION_TYPE_LIST).count, 16)  
  
def checkPoint4():  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.DNS)  
    snooze(3)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "53") 

def checkPoint5():  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.FINGER)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "79")

    complexPDUWindow.selectAppType(ComplexPDUWindowConst.FTP)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "21")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.HTTP)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "80")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.HTTPS)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "443")  
     
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.IMAP)  
    snooze(1)  
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "143")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.NETBIOS)  
    snooze(1)  
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "137")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.POP3)  
    snooze(1)  
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "110")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.SFTP)  
    snooze(1)  
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "115")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.SMTP)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "25")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.SNMP)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "161")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.SSH)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "22")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.TELNET)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "23")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.TFTP)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "69")
  
    complexPDUWindow.selectAppType(ComplexPDUWindowConst.OTHER)  
    snooze(1)
    util.textCheckPoint(ComplexPDUWindowConst.DESTINATION_PORT, "")
    
    util.close(ComplexPDUWindowConst.COMPLEX_PDU_WINDOW)
    
def createComplexPing():  
    util.clickButton(CommonToolsBarConst.ADD_COMPLEX_PDU)  
    Host1.select()  
    snooze(1)
    util.setText(ComplexPDUWindowConst.DESTINATION_IP, "192.168.1.1")
    util.setText(ComplexPDUWindowConst.TIME_TO_LIVE, "32")
    util.setText(ComplexPDUWindowConst.SEQUENCE_NUMBER, "1")
    util.setText(ComplexPDUWindowConst.SIZE, "1")
    util.clickButton(ComplexPDUWindowConst.PERIODIC)
    util.setText(ComplexPDUWindowConst.PERIODIC_INTERVAL, "5")
    util.clickButton(ComplexPDUWindowConst.CREATE_PDU)
    
def checkPoint6():  
    snooze(1)  
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST).topLevelItemCount, 1)