#*********************************************************************************
#@author: Tuan Hoang
#@summary: AnswerNetworkConst contains the common constants used in Answer Network
#********************************************************************************* 
class AnswerNetworkConst:
    ANSWER_NETWORK = ":Activity_Wizard.m_navigationBtnGrpBox.AnswerNetworkBtn"
    TAB_BAR = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_tabbar"
    
    #Tabs
    ASSESSMENT_TREE = "Assessment Tree"
    CONNECTIVITY_TEST = "Connectivity Test"
    SCORING_MODEL = "Scoring Model"
    OVERALL_FEEDBACK = "Overall Feedback"
    SETTINGS = "Settings"
    
    SHOW_ANSWER_NETWORK = ":Activity_Wizard.m_contents.Answer_Network.groupBox_11.ShowAnsNetBtn"
    ACTIVITY_WIZARD_ICON = ":CAppWindowBase.Activity Wizard Icon"
    IMPORT_FILE_TO_ANSWER_NETWORK = ":Activity_Wizard.m_contents.Answer_Network.groupBox_12.ImportAnsNetBtn"
    IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG_OK = ":Activity_Wizard.QFileDialog.buttonBox.Open"
    IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    EXPORT_ANSWER_NETWORK_TO_FILE = ":Activity_Wizard.m_contents.Answer_Network.groupBox_12.ExportAnsNetBtn"
    EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG_OK = ":Activity_Wizard.QFileDialog.buttonBox.Save"
    EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    REPLACE_FILE_DIALOG = ':Activity_Wizard.QFileDialog.Save File'
    REPLACE_FILE_YES_BUTTON = ':Activity_Wizard.QFileDialog.Save File.qt_msgbox_buttonbox.Yes'
    REPLACE_FILE_NO_BUTTON = ':Activity_Wizard.QFileDialog.Save File.qt_msgbox_buttonbox.No'
    OVERWRITE_DIALOG = ':Overwrite File?'
    OVERWRITE_YES_BUTTON = ':Overwrite File?.qt_msgbox_buttonbox.Yes'
    OVERWRITE_NO_BUTTON = ':Overwrite File?.qt_msgbox_buttonbox.No'

    ASSESSMENT_ITEMS_TREE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.splitter_2.m_comparatorTreeLV"
    ASSESSMENT_ITEMS_TREE_NETWORK = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.splitter_2.m_comparatorTreeLV.item_0/0"
    ASSESSMENT_ITEMS_TREE_HEADER = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.splitter_2.m_comparatorTreeLV.QHeaderView1"
    ASSESSMENT_ITEMS_TREE_RENAME_BOX = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.splitter_2.m_comparatorTreeLV.qt_scrollarea_viewport.QExpandingLineEdit1"
    IP = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_IPCBox"
    ROUTING = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_routingCBox"
    ACL = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_ACLCBox"
    PHYSICAL = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_physicalCBox"
    SWITCHING = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_switchingCBox"
    NAT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_NATCBox"
    VARIABLES = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_variablesCBox"
    VIEW_HIDE_ALL = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_viewFilterGrpBox.m_viewAllCBox"

    CONNECTIVITY_TABLE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_connectivityTab.m_PDUTable"
    CONNECTIVITY_VIEWPORT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_connectivityTab.m_PDUTable.qt_viewport"
    CONNECTIVITY_COMBO_BOX = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_connectivityTab.m_PDUTable.qt_scrollarea_viewport.QComboBox1"
    CONNECTIVITY_LINE_EDIT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_connectivityTab.m_PDUTable.qt_scrollarea_viewport.QExpandingLineEdit1"
    CONNECTIVITY_LINE_EDIT_COMBO = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_connectivityTab.m_PDUTable.qt_viewport.qt_clipped_viewport.qt_editor_cb.in-combo"
    COMPLETED_FEEDBACK_TEXTFIELD = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_feedbackTab.groupBox_15.m_completedFeedbackTF"
    INCOMPLETE_FEEDBACK_TEXTFIELD = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_feedbackTab.groupBox_16.m_incompletedFeedbackTF"
    COMPLETED_FEEDBACK_V_SCROLL = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_feedbackTab.groupBox_15.m_completedFeedbackTF.qt_scrollarea_vcontainer.QScrollBar1"
    
    #Settings Tab - Time Settings
    TIME_SETTINGS_LABEL = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.textLabel7_3"
    TIME_ELAPSED = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_timeElapsedRB"
    COUNTDOWN = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_countDownRB"
    NONE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_noneRB"
    
    COUNTDOWN_HOURS = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_hrSpin.qt_spinbox_lineedit"
    COUNTDOWN_MINUTES = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_minSpin.qt_spinbox_lineedit"
    COUNTDOWN_SECONDS = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_secSpin.qt_spinbox_lineedit"

    #Settings Tab - Feedback Settings
    NO_DYNAMIC_PERCENTAGE_FEEDBACK = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_18.m_checkNoDyChk"
    SHOW_SCORE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_18.m_checkDyChkShCntScore"
    SHOW_ITEM_COUNT_PERCENTAGE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_18.m_checkDyChkShPctPoints"
    SHOW_ITEM_COUNT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_18.m_checkDyChkShCntPoint"
    SHOW_SCORE_PERCENTAGE = "Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_18.m_checkDyChkShPctScore"
    
    #Settings Tab - User profile settings
    USER_PROFILE_LOCKING = ':Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.m_userProfileLockCB' 
    NO_GUEST_PROFILE = ':Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.m_userProfileNoGuestCB'

    TIME_TO_FORWARD_ANSWER_NETWORK = ':Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.m_ansNetForwardSimTimeTE'

    #Assessment Tree Tab Items
    SHOW_CHECKED_ONLY_CHBOX = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.groupBox_17.m_checkedOnlyCB"
    KEYWORD_TEXTFIELD = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.groupBox_17.m_keywordTF"
    FILTER_BUTTON = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.groupBox_17.m_filterBtn"
    EXPAND_COLLAPSE_ALL_BUTTON = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.groupBox_17.m_btnExpCollapseAllAns"
    
    WORKPRODUCT_LIST = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_evidenceModelTable"
    WORKPRODUCT_ROWS = WORKPRODUCT_LIST + ".QHeaderView1.HeaderViewItem"
    WORKPRODUCT_ADD = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_addEvdBtn"
    WORKPRODUCT_DELETE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_remEvdBtn"
    WORKPRODUCT_EDIT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_editEvdBtn"
    WORKPRODUCT_UP = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_upEvdBtn"
    WORKPRODUCT_DOWN = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_13.m_downEvdBtn"
    WORKPRODUCT_WINDOW = ":Activity_Wizard.BaseWorkProductFeaturePopup"
    WORKPRODUCT_NAME = ":Activity_Wizard.BaseWorkProductFeaturePopup.evidenceGB.m_nameLE"
    WORKPRODUCT_DESCRIPTION = ":Activity_Wizard.BaseWorkProductFeaturePopup.evidenceGB.m_descTE"
    WORKPRODUCT_LIMIT_CHECKBOX = ":Activity_Wizard.BaseWorkProductFeaturePopup.evidenceGB.m_limitExprCB"
    WORKPRODUCT_EXPRESSION = ":Activity_Wizard.BaseWorkProductFeaturePopup.evidenceGB.m_expressionTE"
    WORKPRODUCT_HELP = ":Activity_Wizard.BaseWorkProductFeaturePopup.evidenceGB.m_helpTE"
    WORKPRODUCT_OK = ":Activity_Wizard.BaseWorkProductFeaturePopup.m_okBtn"
    WORKPRODUCT_CANCEL = ":Activity_Wizard.BaseWorkProductFeaturePopup.m_cancelBtn"
    
    SCORING_MODEL_DIALOG = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel"
    SCORING_RULE_LIST_TITLE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14"
    SCORING_RULE_TEXT_LABEL = "Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.textLabel1_6"
    SCORING_RULE_LIST = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_profiencyModelTable"
    SCORING_RULE_ROWS = SCORING_RULE_LIST + ".QHeaderView1.HeaderViewItem"
    SCORING_RULE_ADD = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_addObsBtn"
    SCORING_RULE_DELETE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_remObsBtn"
    SCORING_RULE_EDIT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_editObsBtn"
    SCORING_RULE_UP = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_upObsBtn"
    SCORING_RULE_DOWN = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.ScoringModel.groupBox_14.m_downObsBtn"
    
    SCORING_RULE_WINDOW = ":Activity_Wizard.BaseProficiencyModelPopup"
    SCORING_RULE_TYPE_DROPDOWN = ":Activity_Wizard.BaseProficiencyModelPopup.proficiencymodelGB.m_typeCB"
    PRIMARY_OBSERVABLE = "Primary Observable"
    COMPOUND_OBSERVABLE = "Compound Observable"
    PROFICIENCY_ESTIMATE = "Proficiency Estimate" 
    REPORTING_VARIABLE = "Reporting Variable"
    SCORING_RULE_NAME = ":Activity_Wizard.BaseProficiencyModelPopup.proficiencymodelGB.m_nameLE"
    SCORING_RULE_DESCRIPTION = ":Activity_Wizard.BaseProficiencyModelPopup.proficiencymodelGB.m_descTE"
    SCORING_RULE_EXPRESSION = ":Activity_Wizard.BaseProficiencyModelPopup.proficiencymodelGB.m_expressionTE"
    SCORING_RULE_HELP = ":Activity_Wizard.BaseProficiencyModelPopup.proficiencymodelGB.m_helpTE"
    SCORING_RULE_OK = ":Activity_Wizard.BaseProficiencyModelPopup.m_okBtn"
    SCORING_RULE_CANCEL = ":Activity_Wizard.BaseProficiencyModelPopup.m_cancelBtn"
    
    SETTINGS_TIME_TEXT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.textLabel7_3"
    SETTINGS_NONE_LBL_TXT = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_timeTab.groupBox_19.m_noneRB"
    
    VAR_ASSESSMENT_TREE = ":Activity_Wizard.m_contents.Answer_Network.m_answerNetTabs.qt_tabwidget_stackedwidget.m_assessOptTab.m_varAssessmentTree"
    
    ##This is a list of the used answer network items. Add new Items as needed.
    class AssessmentItems:
        NETWORK = "Network"
        ROUTER_0 = "Network.Router 0"
        ROUTER_0_DEVICE_MODEL = "Network.Router0.Device Model: 1841"
        PEER_0 = "Network.Peer0"
        PEER_0_ADDRESS_IF_NOT_CONNECTED = "Network.Peer0.Peer Address: :0"
        PEER_0_NETWORK_IF_NOT_CONNECTED = "Network.Peer0.Peer Network Name: "
        PEER_0_PASSWORD_IF_NOT_CONNECTED = "Network.Peer0.Password: "
        PEER_0_CONNECTED_IF_NOT_CONNECTED = "Network.Peer0.Connected: 0"
        ROUTER_0_STATIC_ROUTES = "Network.Router0.Routes.(deprecated) Static Routes"
        ROUTER_0_STATIC_ROUTES_ROUTE0 = "Network.Router0.Routes.(deprecated) Static Routes.(deprecated) Route0: {{RegEx:172\.16\.1\.0-24-FastEthernet0/0-0\\n}}"
        ROUTER_0_STATIC_ROUTES_ROUTE1 = "Network.Router0.Routes.(deprecated) Static Routes.(deprecated) Route1: {{RegEx:172\.16\.2\.0-24-FastEthernet0/0-0\\n}}"
        ROUTER_0_FIREWALL_AUDIT_TRAIL = "Network.Router0.Firewall.Global Audit Trail: 1"
        ROUTER_0_PORT_FA_CRYPTO_MAP = "Network.Router0.Ports.FastEthernet0/0.Crypto Map: mymap"
        ROUTER_1_ROUTES = "Network.Router1.Routes"
        ROUTER_1_ROUTES_STATIC = "Network.Router1.Routes.(deprecated) Static Routes"
        ROUTER_1_ROUTES_STATIC_ROUTE_0 = "Network.Router1.Routes.(deprecated) Static Routes.(deprecated) Route0: 1\.0\.0\.0-8-3\.3\.3\.2-0"
        ROUTER_0_RADIUS_CLIENT_RADIUS_SERVER_KEY = "Network.Router0.RADIUS Client.RADIUS server key: radiuspa55"
        ROUTER_0_LOGIN_ON_FAILURE = "Network.Router0.Login Options.Login On Failure: 1"
        ASA_0 = "Network.ASA0"
        ASA_0_AAA = "Network.ASA0.AAA"
        ASA_0_AAA_AUTHENTICATION = "Network.ASA0.AAA.Authentication"
        ASA_0_AAA_AUTHENTICATION_SSH_1 = "Network.ASA0.AAA.Authentication.Authentication SSH: 1"
        ASA_0_AAA_AUTHENTICATION_TELNET_2 = "Network.ASA0.AAA.Authentication.Authentication Telnet: 2"
        ASA_0_PORTS = "Network.ASA0.Ports"
        ASA_0_PORTA_ETHERNET_0_2_ACCESS_VLAN_3 ="Network.ASA0.Ports.Ethernet0/2.Access VLAN: 3"
        
        
        