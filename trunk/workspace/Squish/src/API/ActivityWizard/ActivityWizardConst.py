from API.ActivityWizard.VariableManager.VariableManagerConst import VariableManagerConst
from API.ActivityWizard.AnswerNetwork.AnswerNetworkConst import AnswerNetworkConst
from API.ActivityWizard.InitialNetwork.InitialNetworkConst import InitialNetworkConst
from API.ActivityWizard.InstructionDialog.InstructionDialogConst import InstructionsDialogConst
from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst

class ExitConst:
    EXIT = ":Activity_Wizard.m_navigationBtnGrpBox.ExitBtn"
    EXIT_SAVE_NO = ":CAppWindowBase.New -- Packet Tracer.qt_msgbox_buttonbox.No"
    EXIT_SAVE_YES = ":CAppWindowBase.New -- Packet Tracer.qt_msgbox_buttonbox.Yes"
    EXIT_SAVE_CANCEL = ":CAppWindowBase.New -- Packet Tracer.qt_msgbox_buttonbox.Cancel"
    EXIT_DIALOG_YES = ":Activity_Wizard.Exit? -- Packet Tracer.qt_msgbox_buttonbox.Yes"
    EXIT_DIALOG_NO = ":Activity_Wizard.Exit? -- Packet Tracer.qt_msgbox_buttonbox.No"
    EXIT_DIALOG_WINDOW = ":Activity_Wizard.Exit? -- Packet Tracer"

class InstructionsConst:
    INSTRUCTIONS = ":Activity_Wizard.m_navigationBtnGrpBox.InstructionsBtn"
    TAB_BAR = ":Activity_Wizard.m_contents.Instructions.m_instructionTabs.qt_tabwidget_tabbar"
    EDIT = "Edit"
    INSTRUCTIONS_TEXT_FIELD = ":Activity_Wizard.m_contents.Instructions.splitter.m_instructionTabs.qt_tabwidget_stackedwidget.m_editTab.m_txtInstruction"
    PAGE_NUMBER = ":Activity_Wizard.m_contents.Instructions.m_instPageNum"
    PREVIOUS_PAGE = ":Activity_Wizard.m_contents.Instructions.InstPrevBtn"
    NEXT_PAGE = ":Activity_Wizard.m_contents.Instructions.InstNextBtn"
    INSERT_PAGE = ":Activity_Wizard.m_contents.Instructions.InsertBtn"
    REMOVE_PAGE = ":Activity_Wizard.m_contents.Instructions.InstRemoveBtn"
    IMPORT_PAGE = ":Activity_Wizard.m_contents.Instructions.ImportBtn"
    IMPORT_PAGE_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    IMPORT_PAGE_DIALOG_OPEN = ":Activity_Wizard.QFileDialog.buttonBox.Open"
    IMPORT_PAGE_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    EXPORT_PAGE = ":Activity_Wizard.m_contents.Instructions.ExportBtn"
    EXPORT_PAGE_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    EXPORT_PAGE_DIALOG_SAVE = ":Activity_Wizard.QFileDialog.buttonBox.Save"
    EXPORT_PAGE_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    EXPORT_PAGE_DIALOG_OVERWRITE_YES = ":Activity_Wizard.QFileDialog.Export Instruction File.qt_msgbox_buttonbox.Yes"
    EXPORT_PAGE_DIALOG_OVERWRITE_NO = ":Activity_Wizard.QFileDialog.Export Instruction File.qt_msgbox_buttonbox.No"
    IMPORT_ALL = ":Activity_Wizard.m_contents.Instructions.ImportAllBtn"
    IMPORT_ALL_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    IMPORT_ALL_DIALOG_CHOOSE = ":Activity_Wizard.QFileDialog.buttonBox.Choose"
    IMPORT_ALL_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    EXPORT_ALL = ":Activity_Wizard.m_contents.Instructions.ExportAllBtn"
    EXPORT_ALL_DIALOG = ":Activity_Wizard.QFileDialog.fileNameEdit"
    EXPORT_ALL_DIALOG_CHOOSE = ":Activity_Wizard.QFileDialog.buttonBox.Choose"
    EXPORT_ALL_DIALOG_CANCEL = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    AUTO_LOAD_EXTERNAL_FILES = ":Activity_Wizard.m_contents.Instructions.AutoLoadCB"
    PREVIEW_AS_HTML = "Preview as HTML"
    PREVIEW_AS_HTML_TEXT = ":Activity_Wizard.m_contents.Instructions.m_instructionTabs.qt_tabwidget_stackedwidget.m_previewHTMLTab.CWebView1.DOCUMENT.HTML1.BODY1"
    
    VARIABLE_MANAGER_TABLE = ':Activity_Wizard.m_contents.Instructions.m_varInstruction'

class PasswordConst:
    PASSWORD = ":Activity_Wizard.m_navigationBtnGrpBox.PasswordBtn"
    PASSWORD_TEXTFIELD = ":Activity_Wizard.m_contents.Password.groupBox_20.m_passTF"
    CONFIRM_TEXTFIELD = ":Activity_Wizard.m_contents.Password.groupBox_20.m_passConfirmTF"
    ENABLE_PASSWORD = ":Activity_Wizard.m_contents.Password.groupBox_20.EnablePassBtn"
    DISABLE_PASSWORD = ":Activity_Wizard.m_contents.Password.groupBox_20.DisablePassBtn"
    ASK_AW_PASSWORD_TEXTFIELD = ":Password? -- Packet Tracer.QLineEdit1"
    ASK_AW_PASSWORD_OK = ":Password? -- Packet Tracer.QDialogButtonBox1.OK"
    ASK_AW_PASSWORD_CANCEL = ":Password? -- Packet Tracer.QDialogButtonBox1.Cancel"

class SaveConst:
    SAVE = ":Activity_Wizard.m_navigationBtnGrpBox.SaveBtn"
    SAVE_DIALOG = ":CAppWindowBase.QFileDialog.fileNameEdit"
    SAVE_DIALOG_OK = ":CAppWindowBase.QFileDialog.buttonBox.Save"
    SAVE_DIALOG_CANCEL = ":CAppWindowBase.QFileDialog.buttonBox.Cancel"
    OVERWRITE_FILE_PROMPT = ":Overwrite File?"
    OVERWRITE_FILE_PROMPT_LABEL = ":Overwrite File?.qt_msgbox_label"
    OVERWRITE_FILE_PROMPT_YES = ":Activity_Wizard.QFileDialog.Save File.qt_msgbox_buttonbox.Yes"
    OVERWRITE_FILE_PROMPT_NO = ":Activity_Wizard.QFileDialog.Save File.qt_msgbox_buttonbox.No"
    OVERWRITE_FILE_PROMPT2 = ":Overwrite File?"
    OVERWRITE_FILE_PROMPT2_YES = ":Overwrite File?.qt_msgbox_buttonbox.Yes"
    OVERWRITE_FILE_PROMPT2_NO = ":Overwrite File?.qt_msgbox_buttonbox.No"
    
    SAVE_FILE_NAME = ":CAppWindowBase.QFileDialog.fileNameEdit"
    CONFIRM_SAVE_FILE = ":CAppWindowBase.QFileDialog.buttonBox.Save"
    NO_SAVE_FILE = ":CAppWindowBase.QFileDialog.buttonBox.Cancel"
    CANCEL_SAVE_FILE = ":CAppWindowBase.QFileDialog.buttonBox.Cancel"
    SAVE_FILE_WINDOW = ":CAppWindowBase.QFileDialog"
    NO_WRITE_PERMISSION_PROMPT = ":No Write Permission"
    NO_WRITE_PERMISSION_PROMPT_OK = ":No Write Permission.qt_msgbox_buttonbox.OK"

class WelcomeConst:
    AUTHOR_INFO_CONTENT = ':Activity_Wizard.m_contents.Welcome.groupBox.m_authorInfo'
    
class ActivityWizardConst:
    answerNetwork = AnswerNetworkConst
    exit = ExitConst
    instructions = InstructionsConst
    password = PasswordConst
    save = SaveConst
    variableManager = VariableManagerConst
    initialNetwork = InitialNetworkConst
    welcome = WelcomeConst
    instructionsDialog = InstructionsDialogConst
    testActivity = TestActivityConst
    ACTIVITY_WIZARD_WINDOW = ":Activity_Wizard"
    ACTIVITY_WIZARD_NAVIGATION_GROUP = ":Activity_Wizard.m_navigationBtnGrpBox"
    WELCOME = ":Activity_Wizard.m_navigationBtnGrpBox.WelcomeBtn"
    VARIABLE_MANAGER = ":Activity_Wizard.m_navigationBtnGrpBox.VariableManagerBtn"
    INSTRUCTIONS = ":Activity_Wizard.m_navigationBtnGrpBox.InstructionsBtn"
    ANSWER_NETWORK = ":Activity_Wizard.m_navigationBtnGrpBox.AnswerNetworkBtn"
    SCRIPTING = ":Activity_Wizard.m_navigationBtnGrpBox.m_scriptingBtn"
    INITIAL_NETWORK = ":Activity_Wizard.m_navigationBtnGrpBox.InitialNetworkBtn"
    PASSWORD = ":Activity_Wizard.m_navigationBtnGrpBox.PasswordBtn"
    TEST_ACTIVITY = ":Activity_Wizard.m_navigationBtnGrpBox.TestActivityBtn"
    CHECK_ACTIVITY = ":Activity_Wizard.m_navigationBtnGrpBox.CheckActivityBtn"
    SAVE = ":Activity_Wizard.m_navigationBtnGrpBox.SaveBtn"
    SAVE_AS = ":Activity_Wizard.m_navigationBtnGrpBox.SaveAsBtn"
    SAVE_AS_PKZ = ":Activity_Wizard.m_navigationBtnGrpBox.SaveAsPkzBtn"
    SAVE_AS_CC = ":Activity_Wizard.m_navigationBtnGrpBox.SaveAsCCBtn"    
    EXIT = ":Activity_Wizard.m_navigationBtnGrpBox.ExitBtn"
    PASSWORD_PROMPT = ":Password? -- Packet Tracer.QLineEdit1"
    PASSWORD_PROMPT_OK = ":Password? -- Packet Tracer.QDialogButtonBox1.OK"
    USE_AS_ANSWER_NETWORK_YES = ":CAppWindowBase.Use as the Answer Network? -- Packet Tracer.qt_msgbox_buttonbox.Yes"
    USE_AS_ANSWER_NETWORK_NO = ":CAppWindowBase.Use as the Answer Network? -- Packet Tracer.qt_msgbox_buttonbox.No"
    USE_AS_ANSWER_NETWORK_DIALOG = ":CAppWindowBase.Use as the Answer Network? -- Packet Tracer"
    USE_AS_ANSWER_NETWORK_CANCEL = ":CAppWindowBase.Use as the Answer Network? -- Packet Tracer.qt_msgbox_buttonbox.Cancel"
    SAVE_DIALOG_LOOK_IN_LABEL = ":Activity_Wizard.QFileDialog.lookInLabel"
    TITLE = ':Activity_Wizard.m_activityWizardTitle'
    