import sys
from API.Utility.Util import Util
from API.SquishSyntax import SquishSyntax
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.functions import WebviewTagFind2 as TF
from API.functions import NotFoundException
from API.functions import getType
from squish import *
import test
import os

util = Util()

ENV_WEBVIEW = ':Environments.m_environmentWebView.DOCUMENT.HTML1.BODY1'
ENV_WEBVIEW_BODY = ':CAppWindowBase.CEnvironmentDialog1.m_environmentWebView.DOCUMENT.HTML1.BODY1'

ALERT_CONTAINER = '__SM_ALERT_BOX_CONTAINER__'
ALERT_BOX = '__SM_ALERT_BOX_CONTAINER___box'
ALERT_MSG = '__SM_ALERT_BOX_CONTAINER___msg'
ALERT_BTN = '__SM_ALERT_BOX_CONTAINER___btn'

#ENVIRONMENT_WINDOW = ':CAppWindowBase.CEnvironmentDialog1'
ENVIRONMENT_WINDOW = ':Environments'

def err():
    raise(Exception('Not implemented yet'), None, sys.exc_info()[2])

def customInteractions(func):
    def waitForPage(*args, **kwargs):
        Util().clearCache(ENV_WEBVIEW)
        '''for i in range(20):
            if waitForObject(ENV_WEBVIEW).evalJS("document.readyState") == "complete":
                Util().clearCache(ENV_WEBVIEW)
                return func(*args, **kwargs)
            snooze(1)
    return waitForPage'''


class ObjectFinder:
    def __init__(self):
        None
    
    @customInteractions
    def location(self):
        label = TF().findTagWithProperties(ENV_WEBVIEW, 'H2', {'innerText':'Location'})
        return label.firstChild()
    
    @customInteractions
    def locationCombo(self):
        combo = TF().findTagWithID(ENV_WEBVIEW, 'locationCombo')
        return combo
    
    def currentTime(self):
        label = TF().findTagWithProperties(ENV_WEBVIEW, 'TIME', {'simplifiedInnerText':'\d+:\d+:\d+'})
        return label
    
    @customInteractions
    def pauseButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'type':'submit', 'simplifiedInnerText':'Pause', 'id':'toggle_time'})
        return button
    
    @customInteractions
    def startButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'type':'submit', 'simplifiedInnerText':'Start', 'id':'toggle_time'})
        return button
    
    @customInteractions
    def timeScaleRealLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'realTime')
        return lineEdit
    
    @customInteractions
    def timeScaleHmsRealComboBox(self):
        combo = TF().findTagWithID(ENV_WEBVIEW, 'realSecondsCombo')
        return combo
    
    @customInteractions
    def timeScaleSimulationLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'simTime')
        return lineEdit
    
    @customInteractions
    def timeScaleHmsSimulationComboBox(self):
        combo = TF().findTagWithID(ENV_WEBVIEW, 'simSecondsCombo')
        return combo
    
    @customInteractions
    def timelineLineEdit(self):
        lineInput = TF().findTagWithID(ENV_WEBVIEW, 'timeLineTime')
        return lineInput
    
    @customInteractions
    def timelineIncrementButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'innerText':'\+', 'type':'submit'})
        return button
    
    @customInteractions
    def timelineDecrementButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'innerText':'-', 'type':'submit'})
        return button
    
    @customInteractions
    def timeIncrementComboBox(self):
        combo = TF().findTagWithProperties(ENV_WEBVIEW, 'SELECT', {'id':'increments', 'type':'select-one', 'selectedOption':'\d+\s\w*'})
        return combo
    
    @customInteractions
    def previousKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'prevKeyframeBtn'})
        return button
    
    @customInteractions
    def totalKeyframeLaebl(self):
        return self.previousKeyframeButton().previousSibling()
    
    @customInteractions
    def currentKeyframeLabel(self):
        return self.totalKeyframeLaebl().previousSibling()
    
    @customInteractions
    def nextKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'nextKeyframeBtn'})
        return button
    
    @customInteractions
    def addKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'setAddKeyframeBtn'})
        return button
    
    @customInteractions
    def removeKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'removeKeyframeBtn'})
        return button
    
    @customInteractions
    def exportKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'exportKeyframes'})
        return button
    
    @customInteractions
    def importKeyframeButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'importKeyframeFromFile'})
        return button

    @customInteractions
    def keyframeDropdown(self):
        dropdown = TF().findTagWithID(ENV_WEBVIEW, 'keyframeTemplates')
        return dropdown

    @customInteractions
    def noteTextEdit(self):
        sibling = TF().findTagWithProperties(ENV_WEBVIEW, 'LABEL', {'simplifiedInnerText':'Show Notes in View Mode'})
        parent = object.parent(sibling)
        textarea = TF().findTagWithProperties(parent, 'TEXTAREA', {'type':'textarea'})
        return textarea
    
    @customInteractions
    def showNotesCheckbox(self):
        parent = TF().findTagWithProperties(ENV_WEBVIEW, 'LABEL', {'simplifiedInnerText':'Show Notes in View Mode'})
        checkbox = TF().findTagWithProperties(parent, 'INPUT', {'type':'checkbox'})
        return checkbox
    
    @customInteractions
    def viewOnlyButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'viewBtn'})
        return button
    
    @customInteractions
    def viewOnlyEditButton(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'editBtn')
        return button
    
    @customInteractions
    def createCustomEnvironmentButton(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'customCreateBtn')
        return button

    @customInteractions
    def createCustomEnvironmentCategoryComboBox(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'CustomEnvironmentCategories')
        return button
    
    @customInteractions
    def createCustomEnvironmentEnvironmentIDLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'enviromentID')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentEnvironmentDisplayNameLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'enviromentName')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentMetricUnitLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'metricUnit')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentImperialUnitLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'imperialUnit')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentMetricToImperialFormulaLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'imperialFormula')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentImperialToMetricFormulaLineEdit(self):
        lineEdit = TF().findTagWithID(ENV_WEBVIEW, 'metricFormula')
        return lineEdit
    
    @customInteractions
    def createCustomEnvironmentCreateButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'simplifiedInnerText':'Create', 'type':'button'})
        return button
    
    @customInteractions
    def createCustomEnvironmentCancel(self):
        sibling = self.createCustomEnvironmentCreateButton()
        parent = object.parent(sibling)
        button = TF().findTagWithProperties(parent, 'BUTTON', {'simplifiedInnerText':'Cancel', 'type':'button'})
        return button
    
    @customInteractions
    def removeCustomEnvironmentButton(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'removeCustomBtn')
        return button
    
    @customInteractions
    def debugButton(self):
        button = TF().findTagWithProperties(ENV_WEBVIEW, 'BUTTON', {'id':'debugBtn'})
        return button
    
    @customInteractions
    def errorMessageButton(self):
        button = TF().findTagWithID(ENV_WEBVIEW, ALERT_BTN)
        return button
    
    @customInteractions
    def advancedTabButton(self):
        parent = TF().findTagWithID(ENV_WEBVIEW, 'tabs')
        button = TF().findTagWithProperties(parent, 'A', {'innerText':'Advanced'})
        return button
    
    @customInteractions
    def alertButton(self):
        parent = TF().findTagWithProperties(ENV_WEBVIEW, 'DIV', {'simplifiedInnerText':'Alert Close'})
        button = TF().findTagWithProperties(parent, 'BUTTON', {'simplifiedInnerText':'Ok'})
        return button
    
def setText(obj, text):
    obj.focus()
    nativeType('<Ctrl+a>')
    nativeType('<Del>')
    nativeType(text)
    #ObjectFinder().timeScaleRealLineEdit().focus()
    #ObjectFinder().timeScaleSimulationLineEdit().focus()
    nativeType('<Tab>')
    None
    
class TimeScaleObjects:
    real_edit = ObjectFinder().timeScaleRealLineEdit
    simulation_edit = ObjectFinder().timeScaleSimulationLineEdit
    hms_real_combo = ObjectFinder().timeScaleHmsRealComboBox
    hms_simulation_combo = ObjectFinder().timeScaleHmsSimulationComboBox

class TimelineObjects:
    edit = ObjectFinder().timelineLineEdit
    increment = ObjectFinder().timelineIncrementButton
    decrement = ObjectFinder().timelineDecrementButton
    combo = ObjectFinder().timeIncrementComboBox
    
class KeyframeObjects:
    current_frame_label = ObjectFinder().currentKeyframeLabel
    total_frame_label = ObjectFinder().totalKeyframeLaebl
    previous_button = ObjectFinder().previousKeyframeButton
    next_button = ObjectFinder().nextKeyframeButton
    add_button = ObjectFinder().addKeyframeButton
    remove_button = ObjectFinder().removeKeyframeButton
    export_button = ObjectFinder().exportKeyframeButton
    import_button = ObjectFinder().importKeyframeButton
    keyframe_dropdown = ObjectFinder().keyframeDropdown

class CustomEnvironmentObjects:
    create_custom_environment_button = ObjectFinder().createCustomEnvironmentButton
    category_combo = ObjectFinder().createCustomEnvironmentCategoryComboBox
    id_edit = ObjectFinder().createCustomEnvironmentEnvironmentIDLineEdit
    display_name_edit = ObjectFinder().createCustomEnvironmentEnvironmentDisplayNameLineEdit
    metric_unit = ObjectFinder().createCustomEnvironmentMetricUnitLineEdit
    imperial_unit = ObjectFinder().createCustomEnvironmentImperialUnitLineEdit
    metric_to_imperial_formula_edit = ObjectFinder().createCustomEnvironmentMetricToImperialFormulaLineEdit
    imperial_to_metric_formula_edit = ObjectFinder().createCustomEnvironmentImperialToMetricFormulaLineEdit
    create_button = ObjectFinder().createCustomEnvironmentCreateButton
    cancel_button = ObjectFinder().createCustomEnvironmentCancel

class ViewOnlyObjects:
    def __init__(self):
        self.editButton = ObjectFinder().viewOnlyEditButton
    
    @customInteractions
    def getNoteArea(self):
        noteArea = TF().findTagWithProperties(ENV_WEBVIEW, 'NOTES', {'tagName':'NOTES'})
        return noteArea
    
    @customInteractions
    def getViewOnlyTree(self):
        tree = TF().findTagWithID(ENV_WEBVIEW, 'viewTree')
        return tree
    
    @customInteractions
    def getPropertyObject(self, p_propertyName):
        tree = self.getViewOnlyTree()
        itemChildSpan = TF().findTagWithProperties(tree, 'SPAN', {'innerText':p_propertyName})
        item = object.parent(itemChildSpan)
        return item
    
    @customInteractions
    def getPropertyExpander(self, p_propertyName):
        tree = self.getViewOnlyTree()
        itemSpan = TF().findTagWithProperties(tree, 'SPAN', {'simplifiedInnerText':p_propertyName})
        expander = TF().findTagWithProperties(itemSpan, 'SPAN', {'domClassName':'fancytree-expander'})
        return expander
    
    @customInteractions
    def getSubPropertyObject(self, p_subPropertyName, p_parentPropertyName):
        parent = self.getPropertyObject(p_parentPropertyName)
        children = object.children(parent)
        if len(children) == 2:
            searchParent = children[1]
        else:
            raise(Exception('While writing this I am under the impression that there will alway be 2 children.\
            If this is not the case let me know so that I can fix this. -Chris'))
        subPropertyListItem = TF().findTagWithProperties(searchParent, 'LI', {'innerText':subpropertyName})
        return subPropertyListItem
    
    @customInteractions
    def getSubPropertyValueObj(self, p_subPropertyExactName):
        valueObj = TF().findTagWithID(ENV_WEBVIEW, 'value_' + p_subPropertyExactName)
        return valueObj
    
    @customInteractions
    def getSubPropertyDebugObj(self, p_subPropertyExactName):
        valueObj = TF().findTagWithID(ENV_WEBVIEW, 'debug_value_' + p_subPropertyExactName)
        return  valueObj
    
class PropertiesObjects:
    def __init__(self):
        None
    @customInteractions
    def getPropertyTree(self):
        tree = TF().findTagWithID(ENV_WEBVIEW, 'tree')
        return tree
    
    @customInteractions
    def getPropertyObject(self, p_propertyName):
        '''Returns the LI object of the span. This is the parent of all items in the property'''
        tree = self.getPropertyTree()
        itemChildSpan = TF().findTagWithProperties(tree, 'SPAN', {'simplifiedInnerText':p_propertyName})
        item = object.parent(itemChildSpan)
        return item
    
    @customInteractions
    def getPropertyCheckbox(self, p_propertyName):
        tree = self.getPropertyTree()
        itemSpan = TF().findTagWithProperties(tree, 'SPAN', {'simplifiedInnerText':p_propertyName})
        checkbox = TF().findTagWithProperties(itemSpan, 'SPAN', {'domClassName':'fancytree-checkbox'})
        return checkbox
    
    @customInteractions
    def getPropertyExpander(self, p_propertyName):
        tree = self.getPropertyTree()
        itemSpan = TF().findTagWithProperties(tree, 'SPAN', {'simplifiedInnerText':p_propertyName})
        expander = TF().findTagWithProperties(itemSpan, 'SPAN', {'domClassName':'fancytree-expander'})
        return expander
    
    @customInteractions
    def getSubPropertyObject(self, subpropertyName, parentPropertyName):
        parent = self.getPropertyObject(parentPropertyName)
        children = object.children(parent)
        if len(children) >= 2:
            searchParent = children[1]
        else:
            raise(Exception('While writing this I am under the impression that there will alway be 2 children.\
            If this is not the case let me know so that I can fix this. -Chris'))
        subPropertyListItem = TF().findTagWithProperties(searchParent, 'LI', {'innerText':subpropertyName})
        return subPropertyListItem
    
    @customInteractions
    def getSubPropertyCheckbox(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        checkbox = TF().findTagWithProperties(listItem, 'SPAN', {'domClassName':'fancytree-checkbox'})
        return checkbox
    
    @customInteractions
    def getSubPropertyInitValueEdit(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        sibling = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Init Value:'})
        lineEdit = sibling.nextSibling()
        return lineEdit
    
    @customInteractions
    def getSubPropertyMinValueEdit(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        sibling = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Min Value:'})
        lineEdit = sibling.nextSibling()
        return lineEdit
    
    @customInteractions
    def getSubPropertyMaxValueEdit(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        sibling = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Max Value:'})
        lineEdit = sibling.nextSibling()
        return lineEdit
    
    @customInteractions
    def getSubPropertyTransferenceValueEdit(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        sibling = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Transference:'})
        lineEdit = sibling.nextSibling()
        return lineEdit
    
    @customInteractions
    def getSubPropertyInterpolateCheckbox(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        label = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Interpolate'})
        checkbox = label.firstChild()
        return checkbox
    
    @customInteractions
    def getSubPropertyShowCheckbox(self, subpropertyName, parentPropertyName):
        listItem = self.getSubPropertyObject(subpropertyName, parentPropertyName)
        label = TF().findTagWithProperties(listItem, 'LABEL', {'innerText':'Show'})
        checkbox = label.firstChild()
        return checkbox
    
    @customInteractions
    def getAdvancedSettingsCheckbox(self):
        checkbox = TF().findTagWithID(ENV_WEBVIEW, 'advancedSettings')
        return checkbox
    
class Objects:
    timescale = TimeScaleObjects()
    timeline = TimelineObjects()
    keyframe = KeyframeObjects()
    properties = PropertiesObjects()
    customenvironment = CustomEnvironmentObjects()
    viewOnly = ViewOnlyObjects()
    advanced_tab_button = ObjectFinder().advancedTabButton
    current_location_label = ObjectFinder().location
    current_time_label = ObjectFinder().currentTime
    pause_button = ObjectFinder().pauseButton
    start_button = ObjectFinder().startButton
    note_textedit = ObjectFinder().noteTextEdit
    edit_button = ObjectFinder().viewOnlyEditButton
    show_notes_checkbox = ObjectFinder().showNotesCheckbox
    view_only_button = ObjectFinder().viewOnlyButton
    create_custom_environment_button = ObjectFinder().createCustomEnvironmentButton
    remove_custom_environment_button = ObjectFinder().removeCustomEnvironmentButton
    debug_button = ObjectFinder().debugButton
    error_ok_button = ObjectFinder().errorMessageButton
    alert_ok_button = ObjectFinder().alertButton
    location_combo = ObjectFinder().locationCombo

class TimeScale:
    def __init__(self):
        self.objects = Objects()
    def setSimulationTimeScale(self, p_real, p_simulated, p_hmsReal = 'S', p_hmsSimulated = 'S'):
        self.setReal(p_real)
        self.setSimulated(p_simulated)
        self.setHmsReal(p_hmsReal)
        self.setHmsSimulated(p_hmsSimulated)
    
    def setReal(self, p_real):
        Objects().timescale.real_edit().value = str(p_real)
        
    def setSimulated(self, p_simulated):
        Objects().timescale.simulation_edit().value = str(p_simulated)
    
    def setHmsReal(self, p_hmsReal):
        '''S[econds], M[inutes], H[ours]'''
        combo = Objects().timescale.hms_real_combo()
        option = p_hmsReal.upper()[0]
        for i in range(combo.numChildren):
            if str(combo.optionAt(i).innerText).startswith(option):
                combo.setSelectedOption(combo.optionAt(i).innerText)
                return
        raise Exception('Option not found. Check the given parameters')
        
    def setHmsSimulated(self, p_hmsSimulated):
        '''S[econds], M[inutes], H[ours]'''
        combo = Objects().timescale.hms_simulation_combo()
        option = p_hmsSimulated.upper()[0]
        for i in range(combo.numChildren):
            if str(combo.optionAt(i).innerText).startswith(option):
                combo.setSelectedOption(combo.optionAt(i).innerText)
                return
        raise Exception('Option not found. Check the given parameters')
        
class Timeline:
    def __init__(self):
        self.objects = Objects()
        self.click = Util().click
        self.setText = setText
        
    def setTime(self, p_time):
        '''Time in hh:mm:ss(AM|PM) format'''
        self.setText(Objects().timeline.edit(), p_time)
        #self.click(ENVIRONMENT_WINDOW)
        
    def increment(self):
        self.click(Objects().timeline.increment())
    
    def decrement(self):
        self.click(Objects().timeline.decrement())
    
    def setIncrement(self, option):
        combo = Objects().timeline.combo()
        for i in range(combo.numChildren):
            if option.lower() in str(combo.optionAt(i).innerText).lower():
                combo.setSelectedOption(combo.optionAt(i).innerText)
                return
        raise Exception('Option not found. Check the given parameters')
        
    
class Keyframes:
    def __init__(self):
        self.objects = Objects()
        self.click = Util().click
        
    def getCurrentKeyframe(self):
        currKeyframe = Objects().keyframe.current_frame_label()
        return currKeyframe.innerText

    def getTotalKeyframe(self):
        totalKeyframe = Objects().keyframe.total_frame_label()
        return totalKeyframe.innerText
    
    def previous(self):
        self.click(Objects().keyframe.previous_button())
    
    def next(self):
        self.click(Objects().keyframe.next_button())
        
    def add(self):
        self.click(Objects().keyframe.add_button())
    
    def remove(self):
        self.click(Objects().keyframe.remove_button())
    
    def exportBtn(self):
        self.click(Objects().keyframe.export_button())
    
    def keyframeDropdownSelect(self, p_dropdownItem):
        combo = Objects().keyframe.keyframe_dropdown()
        option = p_dropdownItem
        for i in range(combo.numChildren):
            if str(combo.optionAt(i).innerText) == option:
                combo.setSelectedOption(combo.optionAt(i).innerText)
                return
        raise Exception('Option not found. Check the given parameters')
    
    def importBtn(self):
        self.click(Objects().keyframe.import_button())
    
    def fileCancelBtn(self):
        cancelButton = findObject(':CAppWindowBase.QFileDialog.buttonBox.Cancel')
        Util().click(cancelButton)
    
    def fileSaveBtn(self):
        saveButton = findObject(':CAppWindowBase.QFileDialog.buttonBox.Save')
        Util().click(saveButton)
    
    def fileOpenBtn(self):
        openButton = findObject(':CAppWindowBase.QFileDialog.buttonBox.Open')
        Util().click(openButton)
    
    def fileNameEdit(self, p_filename):    
        snooze(1)
        lineEdit = waitForObject(':CAppWindowBase.QFileDialog.fileNameEdit')
        snooze(1)
        util.setText(lineEdit, p_filename)
        None
    
    def fileOverwrite(self, overwrite = True):
        overwriteDialog = ':CAppWindowBase.QFileDialog.Save File'
        if object.exists(overwriteDialog):
            if overwrite:
                yesButton = findObject(':CAppWindowBase.QFileDialog.Save File.qt_msgbox_buttonbox.Yes')
                Util().click(yesButton)
            else:
                noButton = findObject(':CAppWindowBase.QFileDialog.Save File.qt_msgbox_buttonbox.No')
                Util().click(noButton)
    
    
    def exportFile(self, p_filename, overwrite = True, cancel = False):
        self.exportBtn()
        self.fileNameEdit(p_filename)
        if cancel:
            self.fileCancelBtn()
        else:
            self.fileSaveBtn()
        self.fileOverwrite(overwrite)
    
    def importFile(self, p_filename, cancel = False):
        self.importBtn()
        self.fileNameEdit(p_filename)
        if cancel:
            self.fileCancelBtn()
        else:
            self.fileOpenBtn()
        
        
        
        
class Properties:
    def __init__(self):
        self.objects = Objects()
        self.click = Util().click
        self.setText = setText
    
    def expandProperty(self, p_propertyName):
        '''Expands a property based on the property searched for. This
        property name must be unique. For example searching for Radiation
        will match Electromagnetic Radiation under Light rather than the
        intended Radiation. This means instead you should search for
        ^Radiation$ using regex to make sure it is unique'''
        self.click(Objects().properties.getPropertyExpander(p_propertyName))
        snooze(1)
    
    def checkProperty(self, p_propertyName):
        self.click(Objects().properties.getPropertyCheckbox(p_propertyName))
    
    def checkSubPropertyToggle(self, p_subPropertyName, p_parentPropertyName):
        self.click(Objects().properties.getSubPropertyCheckbox(p_subPropertyName, p_parentPropertyName))
    
    def setSubPropertyInitValue(self, p_value, subpropertyName, parentPropertyName):
        initValue = Objects().properties.getSubPropertyInitValueEdit(subpropertyName, parentPropertyName)
        self.setText(initValue, p_value)
        None
        
    def setSubPropertyMinValue(self, p_minValue, subpropertyName, parentPropertyName):
        minValEdit = Objects().properties.getSubPropertyMinValueEdit(subpropertyName, parentPropertyName)
        self.setText(minValEdit, p_minValue)
    
    def setSubPropertyMaxValue(self, p_maxValue, subpropertyName, parentPropertyName):
        maxValEdit = Objects().properties.getSubPropertyMaxValueEdit(subpropertyName, parentPropertyName)
        self.setText(maxValEdit, p_maxValue)
    
    def setSubPropertyTransference(self, p_transference, subpropertyName, parentPropertyName):
        transferenceEdit = Objects().properties.getSubPropertyTransferenceValueEdit(subpropertyName, parentPropertyName)
        self.setText(transferenceEdit, p_transference)
    
    def checkSubPropertyInterpolate(self, subpropertyName, parentPropertyName):
        checkbox = Objects().properties.getSubPropertyInterpolateCheckbox(subpropertyName, parentPropertyName)
        self.click(checkbox)
    
    def checkSubPropertyShow(self, subpropertyName, parentPropertyName):
        checkbox = Objects().properties.getSubPropertyShowCheckbox(subpropertyName, parentPropertyName)
        self.click(checkbox)
    
    def advancedSettingsCheckbox(self):
        checkbox = Objects().properties.getAdvancedSettingsCheckbox()
        self.click(checkbox)

class ViewOnly:
    def __init__(self):
        self.objects = Objects()
        
    def getValueOf(self, subproperty):
        return Objects().viewOnly.getSubPropertyValueObj(subproperty)

class CreateCustomEnvironment:
    def __init__(self):
        self.objects = Objects()
        self.click = Util().click
        self.setText = setText
    
    def createNewEnvironment(self, p_categoryName, p_id, p_displayName, p_metricUnit, p_imperialUnit, p_formulaMetric, p_formulaImperial):
        self.setCategory(p_categoryName)
        self.setEnvironmentID(p_id)
        self.setEnvironmentDisplayName(p_displayName)
        self.setMetricUnit(p_metricUnit)
        self.setImperialUnit(p_imperialUnit)
        self.setMetricToImperialFormula(p_formulaMetric)
        self.setImperialToMetricFormula(p_formulaImperial)
        self.create()
        
    def setCategory(self, p_categoryName):
        combo = Objects().customenvironment.category_combo()
        for i in range(combo.numChildren):
            if p_categoryName in str(combo.optionAt(i).innerText):
                combo.setSelectedOption(combo.optionAt(i).innerText)
                return
        raise Exception('Option not found')
    
    def setEnvironmentID(self, p_id):
        lineedit = TF().findTagWithID(ENV_WEBVIEW, 'enviromentID')
        self.setText(lineedit, p_id)
    
    def setEnvironmentDisplayName(self, p_displayName):
        lineedit = Objects().customenvironment.display_name_edit()
        self.setText(lineedit, p_displayName)
    
    def setMetricUnit(self, p_metricUnit):
        lineedit = Objects().customenvironment.metric_unit()
        self.setText(lineedit, p_metricUnit)
    
    def setImperialUnit(self, p_imperialUnit):
        lineedit = Objects().customenvironment.imperial_unit()
        self.setText(lineedit, p_imperialUnit)
    
    def setMetricToImperialFormula(self, p_formula):
        lineedit = Objects().customenvironment.metric_to_imperial_formula_edit()
        self.setText(lineedit, p_formula)
    
    def setImperialToMetricFormula(self, p_formula):
        lineedit = Objects().customenvironment.imperial_to_metric_formula_edit()
        self.setText(lineedit, p_formula)
    
    def create(self):
        button = Objects().customenvironment.create_button()
        self.click(button)
    
    def cancel(self):
        button = Objects().customenvironment.cancel_button()
        self.click(button)
        
class Environment:
    def __init__(self):
        self.click = Util().click
        self.setText = setText
        self.objects = Objects()
        self.customEnvironment = CreateCustomEnvironment()
        self.properties = Properties()
        self.keyframes = Keyframes()
        self.timelines = Timeline()
        self.timescale = TimeScale()
        self.viewOnly = ViewOnly()
        
    def goToEnvironmentManager(self):
        envBtn = None
        clickPhysical = False
        try:
            envBtn = findObject(GoldenPhysicalToolbarConst.ENVIRONMENT_BUTTON)
            if not envBtn.visible:
                clickPhysical = True
        except LookupError, e:
            clickPhysical = True
        except Execption, e:
            raise
            
        if clickPhysical:
            Util().clickOnPhysical()
        if not envBtn:
            envBtn = waitForObject()
        snooze(2)
        self.click(envBtn)

    def pause(self):
        button = Objects().pause_button()
        self.click(button)
    
    def start(self):
        button = Objects().start_button()
        self.click(button)
    
    def advancedTab(self):
        parent = TF().findTagWithID(ENV_WEBVIEW, 'tabs')
        button = TF().findTagWithProperties(parent, 'A', {'innerText':'Advanced'})
        self.click(button)
    
    def getCurrentTime(self):
        '''Returns the current time. The exceptions is because
        sometimes the webview is not ready even though the
        function getting the time is using the decorator.
        I am not clear why this is but this was the easiest
        workaround I was able to come up with. I didn't want to
        use snooze because that may skew the results more of 
        trying to get the current time.'''
        try:
            currTime = Objects().current_time_label()
        except NotFoundException, e:
            currTime = Objects().current_time_label()
        except Exception, e:
            raise
        return currTime.innerText
    
    def addNote(self, p_note):
        noteArea = Objects().note_textedit()
        self.setText(noteArea, p_note)
    
    def showNotes(self):
        checkbox = Objects().show_notes_checkbox()
        if not checkbox.checked:
            self.click(checkbox)
    
    def hideNotes(self):
        checkbox = Objects().show_notes_checkbox()
        if checkbox.checked:
            self.click(checkbox)
    
    def viewOnlyBtn(self):
        button = Objects().view_only_button()
        self.click(button)
        
    def editBtn(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'editBtn')
        self.click(button)
    
    def createCustomEnvironment(self):
        button = TF().findTagWithID(ENV_WEBVIEW, 'customCreateBtn')
        self.click(button)
    
    def removeCustomEnvironment(self, p_propertyName = None, p_subPropertyName = None):
        button = Objects().remove_custom_environment_button()
        self.click(button)
    
    def setLocation(self, p_location):
        combo = Objects().location_combo()
        bFound = False
        for i in range(combo.numChildren):
            if p_location in str(combo.optionAt(i).text):
                combo.setSelectedIndex(i)
                bFound = True
                break
        if not bFound:
            raise ValueError('Could not find ' + p_location + ' in list of options')
    
    def debug(self):
        button = Objects().debug_button()
        self.click(button)
    
    def errorMessageOk(self):
        button = Objects().error_ok_button()
        self.click(button)
    
    def alertMessageOk(self):
        button = Objects().alert_ok_button()
        self.click(button)
    
    def close(self):
        Util().close(ENVIRONMENT_WINDOW)
    
    def textCheckPoint(self, p_textStringOrObj, p_searchText, p_occurrenceNum = -1, **args):
        if (getType(p_textStringOrObj) == getType('str') or
            getType(p_textStringOrObj) == getType(u'unicode')):
            p_textStringOrObj = str(p_textStringOrObj)
            Util().checkText(p_textStringOrObj, p_searchText, p_occurrenceNum, **args)
        else:
            Util().textCheckPoint(p_textStringOrObj, p_searchText, p_occurrenceNum, **args)
    
    def getEnvironmentWindow(self):
        return findObject(ENVIRONMENT_WINDOW)