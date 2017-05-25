##Chris Allen

class IncomingConst:  
    CONNECTION_TYPE_DROPDOWN = ":CBaseMUConnectDlg.cmbMUConnType"
    CONNECTION_TYPE_COMBOBOX = ":CBaseMUConnectDlg.cmbMUConnType.QComboBoxPrivateContainer1.QComboBoxListView1"
    USE_GLOBAL_MULTIUSER_PASSWORD_CHECKBOX = ":CBaseMUConnectDlg.chkGlobalPasswd"
    PASS_EDIT = ":CBaseMUConnectDlg.m_editPasswd"
    OK_BUTT = ":CBaseMUConnectDlg.m_btnConnect"
    CANCEL_BUTT = ":CBaseMUConnectDlg.m_btnCancel"

class OutgoingConst:
    CONNECTION_TYPE_DROPDOWN = ":CBaseMUConnectDlg.cmbMUConnType"
    MULTIUSER_CONNECTION_TYPE = ":CBaseMUConnectDlg.cmbMUConnType"
    CONNECTION_TYPE_COMBOBOX = ":CBaseMUConnectDlg.cmbMUConnType.QComboBoxPrivateContainer1.QComboBoxListView1"
    PEER_ADDRESS_EDIT = ":CBaseMUConnectDlg.cmbPeerAddress.QLineEdit1"
    PEER_PORT_EDIT = ":CBaseMUConnectDlg.m_editPortNum"

    PEER_NETWORK_NAME_EDIT = ":CBaseMUConnectDlg.m_editID"
    PASSWORD_EDIT = ":CBaseMUConnectDlg.m_editPasswd"
    CONNECT_BUTT = ":CBaseMUConnectDlg.m_btnConnect"
    CANCEL_BUTT = ":CBaseMUConnectDlg.m_btnCancel"
    
    CONNECT_DIALOG_WINDOW = ":CBaseMUConnectDlg.Connect"
    CONNECT_DIALOG_LABEL = ":CBaseMUConnectDlg.Connect.qt_msgbox_label"
    CONNECT_DIALOG_OK = ":CBaseMUConnectDlg.Connect.qt_msgbox_buttonbox.OK"

class PopupConst:
    MU_INCOMMING_PROMPT_YES = "CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Incoming Peer Connection.qt_msgbox_buttonbox.Yes"
    MU_INCOMMING_PROMPT_NO = "CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Incoming Peer Connection.qt_msgbox_buttonbox.No"
    
    CONNECTION_ERROR_DIALOG = ':CBaseMUConnectDlg.Connect'
    CONNECTION_ERROR_OK_BUTTON = ':CBaseMUConnectDlg.Connect.qt_msgbox_buttonbox.OK'
    CONNECTION_ERROR_TEXT = ':CBaseMUConnectDlg.Connect.qt_msgbox_label'
    
class ExtensionConst:
    incoming = IncomingConst
    outgoing = OutgoingConst
    popup = PopupConst
    INCOMING_TYPE = "Incoming"
    OUTGOING_TYPE = "Outgoing"
    MESSAGE_OK_BUTT = ":CBaseMUConnectDlg.Packet Tracer.qt_msgbox_buttonbox.OK"
    MULTIUSER_CONNECT_DIALOG = ":CBaseMUConnectDlg"
    CONNECTION_TYPE = ":CBaseMUConnectDlg.cmbMUConnType"
    MAIN_DIALOG = ':CBaseMUConnectDlg'
    
    