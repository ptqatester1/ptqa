#**************************************************************************
#@author: Thi Nguyen
#@summary: HelpConst contains the common constants used in Help menu
#**************************************************************************
class MultiuserConst:
    MULTI_USER_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsMUAction"
    LISTEN = "Listen ..."
    PORT_VISIBILITY = "Port Visibility ..."
    SAVE_OFFLINE = "Save Offline Copy As ..."
    OPTION = "Options ..."    
    class Listen:
        PORT_NUM_EDIT = ":CAppWindowBase.CBaseMUListenDlg.m_editPortNumber"
        PASSWORD_EDIT = ":CAppWindowBase.CBaseMUListenDlg.m_editpasswd"
        ACCEPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_alwaysAccept"
        DENY_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_alwaysDeny"
        PROMPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_prompt"
        NEW_RN_ACCEPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysAcceptNewRN"
        NEW_RN_DENY_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysDenyNewRN"
        NEW_RN_PROMPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysPromptNewRN"
        STOP_LISTEN_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnStartListening"
        OK_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnOk"
        CANCEL_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnCancel"
    class Port_Visilbility:
        NETWORK_TREE_VIEW = ":CAppWindowBase.DevicePortTreeView.portTreeView"
        OK_BUTT = ":CAppWindowBase.DevicePortTreeView.btnOK"
        CANCEL_BUTT = ":CAppWindowBase.Dialog.btnCancel"
    class Options:
        REMOTE_SAVING_CHKBOX = ":Dialog.chkAllowRemoteSaving"
        DEPTH_EDIT = ":CBaseMUOptoinsDlg.m_editDepth"
        LISTEN_CHKBOX = ":CBaseMUOptoinsDlg.chkAlwaysListen"
        ALLOW_PEERS_CHKBOX = ":CBaseMUOptoinsDlg.chkAllowPeers"
        FWD_BROADCAST_CHKBOX = ":CBaseMUOptoinsDlg.chkAllowBroadcast"
        OK_BUTT = ":Dialog.m_btnOK"
        CANCEL_BUTT = ":Dialog.m_btnCancel"
    class Save_OffLine:
    	FILE_NAME_EDIT = ":CAppWindowBase.QFileDialog.fileNameEdit"
    	SAVE_BUTT = ":CAppWindowBase.QFileDialog.buttonBox.Save"
        CANCEL_BUTT = ":CAppWindowBase.QFileDialog.buttonBox.Cancel"