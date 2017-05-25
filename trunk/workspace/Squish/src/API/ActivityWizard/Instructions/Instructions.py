from API.Utility.Util import Util
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API import functions

def err(msg = ''): raise NotImplementedError(msg)

class PopupWarnings:
    def __init__(self):
        self.util = Util()


class FileDialog:
    def __init__(self):
        self.util = Util()
    
    def filename(self, filename):
        self.util.typeText(ActivityWizardConst.instructions.IMPORT_PAGE_DIALOG, filename)
    
    def saveButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.EXPORT_ALL_DIALOG_CHOOSE)
    
    def openButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.IMPORT_PAGE_DIALOG_OPEN)
    
    def cancelButton(self):
        err()
    
    def chooseButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.IMPORT_ALL_DIALOG_CHOOSE)

    def importfile(self, filename):
        self.filename(filename)
        self.openButton()
    
    def importall(self, filename):
        self.filename(filename)
        self.chooseButton()
    
    def exporfile(self, filename):
        self.filename(filename)
        self.saveButton()

class Edit:
    def __init__(self):
        self.util = Util()
    
    def setText(self, text):
        self.util.setText(ActivityWizardConst.instructions.INSTRUCTIONS_TEXT_FIELD, text)

    def textCheckpoint(self, expected, occurrence = -1, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructions.INSTRUCTIONS_TEXT_FIELD, expected, occurrence, **kwargs)
        
class PreviewAsHtml:
    def __init__(self):
        self.util = Util()
    
    def textCheckpoint(self, expected, occurrence = -1, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructions.INSTRUCTIONS_TEXT_FIELD, epxected, occurrence, **kwargs)

class Tabs():
    def __init__(self):
        self.util = Util()
    
    def _clickTab(self, tab):
        self.util.clickTab(ActivityWizardConst.instructions.TAB_BAR, tab)

    def edit(self):
        self._clickTab('Edit')
    
    def previewAsHtml(self):
        self._clickTab('Preview as HTML')

class Instructions:
    def __init__(self):
        self.util = Util()
        self.edit = Edit()
        self.preview = PreviewAsHtml()
        self.tabs = Tabs()
        self.fileDialog = FileDialog()
    
    def select(self):
        self.util.clickButton(ActivityWizardConst.INSTRUCTIONS)
    
    @property
    def pageNumber(self):
        return str(findObject(ActivityWizardConst.instructions.PAGE_NUMBER).text)
    
    def previousButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.PREVIOUS_PAGE)
    
    def nextButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.NEXT_PAGE)
    
    def addButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.INSERT_PAGE)
    
    def removeButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.REMOVE_PAGE)
    
    def importPageButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.IMPORT_PAGE)
    
    def exportPageButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.EXPORT_PAGE)
    
    def importAllButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.IMPORT_ALL)
    
    def exportAllButton(self):
        self.util.clickButton(ActivityWizardConst.instructions.EXPORT_ALL)
    
    def autoLoadExternalFiles(self, checked = None):
        checkbox = findObject(ActivityWizardConst.instructions.AUTO_LOAD_EXTERNAL_FILES)
        self.util.checkbox(checkbox, checked)
    
    def importPage(self, filename):
        self.importPageButton()
        self.fileDialog.importfile(filename)
    
    def exportPage(self, filename):
        self.exportPageButton()
        self.fileDialog.exporfile(filename)
    
    def importAll(self, fileDir):
        self.importAllButton()
        self.fileDialog.importall(fileDir)
    
    def exportAll(self, fileDir):
        self.exportAllButton()
        self.fileDialog.exporfile(fileDir)
