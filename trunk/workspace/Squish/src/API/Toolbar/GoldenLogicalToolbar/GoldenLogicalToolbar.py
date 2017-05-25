#**************************************************************************
#@author: Tuan Hoang
#@summary: GoldenPhysicalToolbar handles golden toolbar in Physical Mode
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.Utility.Util import Util
import object

class BackgroundInputs:
    def __init__(self):
        self.clickButton = SquishSyntax().clickButton
        self.setText = SquishSyntax().setText
        
    def setTiledBackground(self):
        self.clickButton(GoldenLogicalToolbarConst.SET_TILED_BACKGROUND)
        
    def useOriginalImage(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_ORIGINAL_IMAGE_RADIO)
    
    def displayTiledBackgroundImage(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_TILED_CHECKBOX)
    
    def reset(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_RESET)
    
    def apply(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_APPLY)
    
    def browse(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_BROWSE)
    
    def filename(self, filename):
        self.setText(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_FILE_NAME_EDIT, filename)
    
    def open(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_FILE_OPEN)
    
    def cancel(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_FILE_CANCEL)

    def closeBackgroundDialog(self):
        self.close(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_DIALOG)
    
    @property
    def mainDialog(self):
        return GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_DIALOG
        
class Background:
    def __init__(self):
        self.sq = SquishSyntax()
        self.inputs = BackgroundInputs()
    
    def setBackground(self, filename):
        if not object.exists(self.inputs.mainDialog):
            self.inputs.setTiledBackground()
        self.inputs.browse()
        self.inputs.filename(filename)
        self.inputs.open()
        Util().snooze(5)
        self.inputs.apply()
        #self.inputs.closeBackgroundDialog()
    
class GoldenLogicalToolbar(SquishSyntax):
    bg = Background()
    #@summary: Sets background image p_imagePath in backgrounds sub directory p_imageLocation
    #@param p_imagePath: Path to the image
    #@param p_imageLocation: Logical, Intercity, City, or Building
    def setBackgroundImage(self, p_imageLocation):
        self.clickItem(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_LIST, p_imageLocation)
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_APPLY)
        
    def browseBackgroundImage(self,p_imagePath):
        self.goToBackgroundSelector()
        self.browseButton()
        self.filenameEdit(p_imagePath)
        self.openfileButton()
        self.closeBackgroundDialog()
        
    def goToBackgroundSelector(self):
        self.clickButton(GoldenLogicalToolbarConst.SET_TILED_BACKGROUND)
    
    def browseButton(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_BROWSE)
        
    def filenameEdit(self, p_imagePath):
        self.typeText(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_FILE_NAME_EDIT, p_imagePath)
    
    def openfileButton(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_FILE_OPEN)
    
    def closeBackgroundDialog(self):
        self.close(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_DIALOG)
    
    def useOriginalImage(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_ORIGINAL_IMAGE_RADIO)
    
    def displayTiledBackgroundImage(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_TILED_CHECKBOX)
    
    def resetButton(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_RESET)
    
    def applyButton(self):
        self.clickButton(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_APPLY)
    
    def newClusterButton(self):
        self.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    
    def backButton(self):
        self.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)