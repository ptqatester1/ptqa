#************************************************************************************
#@author: Pam Vinco
#@summary: CommonToolsBarConst contains the common constants used in Common Tools Bar
#************************************************************************************
class CommonToolsBarConst:
    COMMON_TOOLS_BAR = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl"
    #Tools
    BUTTONS_BOX = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup"
    SELECT_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.SelectBtn"
    MOVE_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.MoveBtn" #Removed in PT 7 Build 40
    PLACENOTE_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.NoteBtn"
    DELETE_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.DeleteBtn"
    INSPECT_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.InspectBtn"
    DRAW_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.DrawPolyBtn"
    RESIZE_TOOL = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.ResizeBtn"
    ADD_SIMPLE_PDU = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.AddSimpleBtn"
    ADD_COMPLEX_PDU = ":CAppWindowBase.centralwidget.m_pPLToolBox.CPLToolBox_Impl.m_manipulateButtonGroup.AddComplexPDUBtn"
    
    #Place note
    PLACENOTE_TEXT_EDIT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.editframe.CNoteEdit1"
    PLACENOTE_TEXT_EDIT_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.editframe.CNoteEdit1"
    
    #Delete
    DELETE_CONFIRM_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete"
    DELETE_CONFIRM_DIALOG_LABEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_label"
    DELETE_CONFIRM_DIALOG_YES = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Yes"
    DELETE_CONFIRM_DIALOG_NO_PHYSICAL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete.qt_msgbox_buttonbox.No"
    DELETE_CONFIRM_DIALOG_YES_PHYSICAL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete.qt_msgbox_buttonbox.Yes"
    DELETE_CONFIRM_DIALOG_NO = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.No"
    DELETE_CONFIRM_DIALOG_CANCEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Cancel"
	
    DELETE_PHYSICAL_CONFIRM_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete"
    DELETE_PHYSICAL_CONFIRM_DIALOG_LABEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete.qt_msgbox_label"
    DELETE_PHYSICAL_CONFIRM_DIALOG_YES = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete -- Packet Tracer.qt_msgbox_buttonbox.Yes"
    DELETE_PHYSICAL_CONFIRM_DIALOG_NO = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete.qt_msgbox_buttonbox.No"
    DELETE_PHYSICAL_CONFIRM_DIALOG_CANCEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete -- Packet Tracer.qt_msgbox_buttonbox.Cancel"
    DELETE_PHYSICAL_CITY_CONFIRM_DIALOG_YES = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.Confirm Delete.qt_msgbox_buttonbox.Yes"
    
    DELETE_CONFIRM_DIALOG_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete"
    DELETE_CONFIRM_DIALOG_LABEL_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_label"
    DELETE_CONFIRM_DIALOG_YES_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Yes"
    DELETE_CONFIRM_DIALOG_NO_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.No"
    DELETE_CONFIRM_DIALOG_CANCEL_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Cancel"
    
    DELETE_CLUSTER_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete"
    DELETE_CLUSTER_DIALOG_LABEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_label"
    DELETE_CLUSTER_DIALOG_UNCLUSTER = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Uncluster"
    DELETE_CLUSTER_DIALOG_DELETE_CLUSTER = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Delete Cluster"
    DELETE_CLUSTER_DIALOG_CANCEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Cancel"
    
    DELETE_CLUSTER_DIALOG_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete"
    DELETE_CLUSTER_DIALOG_LABEL_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_label"
    DELETE_CLUSTER_DIALOG_UNCLUSTER_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Uncluster"
    DELETE_CLUSTER_DIALOG_DELETE_CLUSTER_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Delete Cluster"
    DELETE_CLUSTER_DIALOG_CANCEL_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.Confirm Delete.qt_msgbox_buttonbox.Cancel"

    #Inspect
    TABLE_TYPE_MENU = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.InspectMenu"
    TABLE_TYPE_MENU_PKA = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace4.CLogicalWorkspace1.InspectMenu"
    #Inspect Table Types
    ROUTING_TABLE = "Routing Table"
    IPV6_ROUTING_TABLE = "IPv6 Routing Table"
    ARP_TABLE = "ARP Table"
    NAT_TABLE = "NAT Table"
    QOS_QUEUES_TABLE = "QoS Queues"
    PORT_STATUS_SUMMARY_TABLE = "Port Status Summary Table"
    DNS_CACHE_TABLE = "DNS Cache Table"
    MAC_TABLE = "MAC Table"
    

    #Port Status Summary Dialog
    PORT_STATUS_SUMMARY_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Port Status Summary Table"
    PORT_STATUS_SUMMARY_TABLE_TEXT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Port Status Summary Table.PortStatusSummaryTableClass.textInfo"
    ROUTING_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Routing Table"
    
    IPV6_ROUTING_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.IPv6 Routing Table"
    
    ARP_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.ARP Table"
    
    NAT_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.NAT Table"
    DEVICE_TABLE_LIST = ".DeviceTable.CDeviceTblVW"

    #QOS Dialog			  
    QOS_QUEUES_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QoSTable.QoSTableClass.m_treeWidget"
    QOS_QUEUES_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QoSTable"
    
    
    DNS_CACHE_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.DNS Cache Table"
    
    MAC_TABLE_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.MAC Table"
    
    NO_FUNCTIONAL_PORTS_OK = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CBaseUserCreatedPDU.No Functional Ports -- Packet Tracer.qt_msgbox_buttonbox.OK"
    INCOMPATIBLE_DEVICE_OK = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CBaseUserCreatedPDU.Incompatible Device -- Packet Tracer.qt_msgbox_buttonbox.OK"
    

    
    DELETE_PHYSICAL_ERROR_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.Cannot Delete Device -- Packet Tracer"
    DELETE_PHYSICAL_ERROR_DIALOG_OK = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.Cannot Delete Device -- Packet Tracer.qt_msgbox_buttonbox.OK"

	
	##REDO FOR PKA WORKSPACE