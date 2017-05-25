#********************************************************************************************
#@author: Pam Vinco
#@summary: ComplexPDUWindowConst contains the common constants used in the Complex PDU Window
#********************************************************************************************
class ComplexPDUWindowConst:
    COMPLEX_PDU_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU"
    
    #Source Settings
    OUTGOING_PORT_LIST = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_createPDUGroupBox.m_portsComboBox"
    AUTO_SELECT_PORT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_createPDUGroupBox.m_autoSelectPort"
    
    #PDU Settings
    APPLICATION_TYPE_LIST = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.m_appComboBox"
    
    DESTINATION_IP = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtIPAddress"
    SOURCE_IP= ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSrcIPAddress"
    TIME_TO_LIVE = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtTTL"
    TOS = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtTOSorDSCP"
    SEQUENCE_NUMBER = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSeqNum"
    SOURCE_PORT =  ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSrcPort"
    DESTINATION_PORT =  ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtDestPort"
    SIZE = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSize"

    #Simulation Settings
    ONE_SHOT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_simulationGroupBox.m_oneTimeRB"
    ONE_SHOT_TIME = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_simulationGroupBox.m_timeLE"
    PERIODIC = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_simulationGroupBox.m_periodicRB"
    PERIODIC_INTERVAL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_simulationGroupBox.m_intervalLE" 
    
    #Buttons
    CREATE_PDU = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_createPDUBtn"
    APPLY_CHANGES = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_editPDUBtn"

    #Error messages
    ERROR_INCORRECT_PDU_SIZE = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Packet Tracer"
    ERROR_INCORRECT_PDU_SIZE_LABEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Incorrect PDU Size -- Packet Tracer.qt_msgbox_label"
    ERROR_INCORRECT_PDU_SIZE_OK = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Incorrect PDU Size -- Packet Tracer.qt_msgbox_buttonbox.OK"
    
    INCORRECT_SEQ_ERROR_BUTT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Q3DockWindow1.create Custom PDU.CBaseCreateCustomPDU.Packet Tracer.qt_msgbox_buttonbox.OK"

    INCORRECT_TIME_POPUP = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Incorrect Time -- Packet Tracer"
    INCORRECT_TIME_POPUP_LABEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Incorrect Time -- Packet Tracer.qt_msgbox_label"
    INCORRECT_TIME_POPUP_OK = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.Incorrect Time -- Packet Tracer.qt_msgbox_buttonbox.OK" 
    
    #Application types
    DNS = "DNS"
    FINGER = "FINGER"
    FTP = "FTP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    IMAP = "IMAP"
    NETBIOS = "NETBIOS"
    PING ="PING"
    POP3 = "POP3"
    SFTP = "SFTP"
    SMTP = "SMTP"
    SNMP = "SNMP"
    SSH = "SSH"
    TELNET = "TELNET"
    TFTP = "TFTP"
    OTHER = "OTHER"
    
    #EDIT PDU SETTINGS (PING)
    EDIT_PDU_DESTINATION_IP = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtIPAddress"           
    EDIT_PDU_SOURCE_IP = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSrcIPAddress"
    EDIT_PDU_TIME_TO_LIVE = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtTTL"
    EDIT_PDU_TOS = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtTOSorDSCP"
    EDIT_PDU_SEQUENCE_NUMBER = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSeqNum"
    EDIT_PDU_SIZE = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.create Custom PDU.CBaseCreateCustomPDU.m_pduSettingsGroupBox.CGenericL3ConfigBase.m_txtSize"