
class PopupWarningConst:
    RESET_ACTIVITY_DIALOG = ':CBaseInstructionDialog.Reset Activity? -- Packet Tracer'
    RESET_ACTIVITY_TEXT = ':CBaseInstructionDialog.Reset Activity? -- Packet Tracer.qt_msgbox_label'
    RESET_ACTIVITY_OK_BUTTON = ':CBaseInstructionDialog.Reset Activity? -- Packet Tracer.qt_msgbox_buttonbox.Ok'
    RESET_ACTIVITY_CANCEL_BUTTON = ':CBaseInstructionDialog.Reset Activity? -- Packet Tracer.qt_msgbox_buttonbox.Cancel'
    
class OverallFeedbackConst:
    WEBVIEW = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_overallFeedbackTab.QWebView1'
    FEEDBACK_TEXT = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_overallFeedbackTab.QWebView1.DOCUMENT.HTML1.BODY1'

class AssessmentItemsConst:
    EXPAND_COLLAPSE_ALL_BUTTON = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_assessmentItemsTab.m_btnExpColAll'
    ASSESSMENT_TREE = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_assessmentItemsTab.m_checkAnswerTree'
    SCORE_TEXT = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_assessmentItemsTab.m_pointsText'
    ITEM_COUNT_TEXT = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_assessmentItemsTab.m_compCompText'
    SCORE_BREAKDOWN_TEXT = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_assessmentItemsTab.m_compPointLbl'

class ConnectivityTestsConst:
    TABLE = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_stackedwidget.m_connectivityTestsTab.m_PDUTable'

class CheckResultsConst:
    overallFeedback = OverallFeedbackConst
    assessmentItems = AssessmentItemsConst
    connectivityTests = ConnectivityTestsConst
    CLOSE_BUTTON = ':CAppWindowBase.CBaseCheckAnswerPage.m_closeButton'
    TABBAR = ':CAppWindowBase.CBaseCheckAnswerPage.m_resultsTab.qt_tabwidget_tabbar'

class InstructionsDialogConst:
    popups = PopupWarningConst
    checkResults = CheckResultsConst
    INSTRUCTIONS_WEBVIEW = ':CBaseInstructionDialog.CWebView1'
    INSTRUCTIONS_TEXT = ':CBaseInstructionDialog.CWebView1.DOCUMENT.HTML1.BODY1'
    COMPLETION_TEXT = ':CBaseInstructionDialog.progressLbl'
    TOP_CHECKBOX = ':CBaseInstructionDialog.topCB'
    CHECK_RESULTS_BUTTON = ':CBaseInstructionDialog.checkAnswerBtn'
    RESET_ACTIVITY_BUTTON = ':CBaseInstructionDialog.resetBtn'
    PREVIOUS_PAGE_BUTTON = ':CBaseInstructionDialog.prevBtn'
    PAGE_LABEL = ':CBaseInstructionDialog.m_pageNum'
    NEXT_PAGE_BUTTON = ':CBaseInstructionDialog.nextBtn'
    DIALOG_WINDOW = ':CBaseInstructionDialog'
    None