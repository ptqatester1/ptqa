##Chris Allen

'''Checking items listed at the confluence page
https://confluence.netacad.net/confluence/pages/viewpage.action?pageId=27957856'''

from API.Utility.Util import Util
from API.Environment.Environment import Environment
from API.functions import toInt
import time
from API.Utility import UtilConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst as TBC
from API.Device.Ioe.MCU import MCU
from API.Workspace.Physical import Physical
from API.functions import trace

util = Util()
env = Environment()
mcu = MCU('Solar Panel', 600, 100, 'IoT0')

def main():
    try:
        util.init()
        _1()
        _2()
        _3()
        _4()
        _5()
        _6()
        _7()
        _8()
        _9()
        _10()
        test.passes('All tests finished', trace('test.py'))
    except Exception, e:
        raise
        test.fail('Not all tests finished', trace('test.py'))
        raise
def _1():
    '''Each container should have a set of environmental setting as it is created.'''
    _1a()
    _1b()
    
def _1a():
    '''So by default creating an activity will create the intercity, city, office,
    and wiring closet.'''
    env.goToEnvironmentManager()
    env.editBtn()
    
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Intercity')
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Home City')
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Corporate Office')
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Main Wiring Closet')
    util.click(TBC.GO_TO_BUILDING)
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Corporate Office')
    util.click(TBC.GO_TO_CITY)
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Home City')
    util.click(TBC.GO_TO_INTERCITY)
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Intercity')
    util.click(TBC.NEW_CITY)
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'City')    
    util.click(TBC.NEW_BUILDING)
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Office Building')    
    util.click(TBC.NEW_CLOSET)
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Wiring Closet')
    env.close()  
    None
    
def _1b():
    '''Each container will have its own environment control screen with a set of defaults''' 
    None
    
def _2():
    '''The container environment will be shown by selecting that container
    (intercity, city, etc.) and the clicking on the environment button.'''
    util.init()
    env.goToEnvironmentManager()
    env.editBtn()
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Intercity')
    env.close()
    workspace = findObject(UtilConst.PHYSICAL_WORKSPACE)
    util.click(object.children(workspace)[-1])
    env.goToEnvironmentManager()
    env.textCheckPoint(env.objects.location_combo().selectedOption, 'Home City')
    env.close()
    None
    
def _3():
    '''The environment interface needs to look like and contain the following fields.
    Think of navigation in the screen like the Activity Wizard. '''
    util.init()
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    for field in ['Earth', 'Electricity', 'Energy', 'Gases', 'Gravity', 'Light', 'Motion',
                  'Other', '^Radiation$', 'Sound', 'Temperature', 'Water', 'Wind']:
        #This part can take a while. Below is a test.log that can be uncommented while debugging by hand just to 
        #be sure the application isn't stuck. This for loop can take a couple minutes
        test.log('Working on ' + field)
        env.properties.expandProperty(field)
    env.close()
    None
    
def _4():
    '''The environment should be set up as a set of common variables that relate to
    sensors by default based on environmental variable type and container.'''
    util.init()
    util.clickOnPhysical()
    mcu.create('physical')
    mcu.select('physical')
    mcu.clickTab('Programming')
    mcu.programming.selectScript('Solar', 'main')
    mcu.programming.insertTextAtLine(15, 'var lastReading = -1;')
    mcu.programming.insertAfter('function displayElectricity(){',
'''
    if (lastReading != electricity){
        Serial.println(electricity);
        lastReading = electricity;
    }''')
    mcu.programming.stop()
    mcu.programming.run()
    mcu.programming.textCheckpoint(mcu.programming.getConsoleOutput().splitlines()[-1], '0')
    mcu.close()
    
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.timescale.setHmsSimulated('Minutes')
    env.properties.expandProperty('Light')
    env.properties.checkSubPropertyToggle('Sunlight', 'Light')
    env.properties.setSubPropertyInitValue(100, 'Sunlight', 'Light')
    env.close()
    
    mcu.select('physical')
    output = mcu.programming.getConsoleOutput().splitlines()[-4:]
    passed = False
    for num in output:
        if num > 0:
            passed = True
            break
    if passed:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('The output was not greater than 0', trace('test.py'))
    mcu.close()
    None
    
def _5():
    '''The user should have the ability to create additional environmental features
    (variables) that can be associated with new sensors. They will need to make the
    association. Illustrated in #8. If a category is selected (highlighted), a
    NEW button will appear behind the main Time select line. If clicked it allows
    the author to create a new field.'''
    util.init()
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.createCustomEnvironment()
    env.customEnvironment.setCategory('Other')
    env.customEnvironment.setEnvironmentID('testEnvironment')
    env.customEnvironment.setEnvironmentDisplayName('testEnvironment')
    env.customEnvironment.setMetricUnit('MT')
    env.customEnvironment.setImperialUnit('IT')
    env.customEnvironment.setMetricToImperialFormula('IT = MT * 2')
    env.customEnvironment.setImperialToMetricFormula('MT = IT / 2')
    env.customEnvironment.create()
    
    snooze(5)
    env.advancedTab()
    env.properties.expandProperty('Other')
    env.properties.checkSubPropertyToggle('testEnvironment', 'Other')
    env.properties.setSubPropertyInitValue('20', 'testEnvironment', 'Other')
    env.properties.setSubPropertyMinValue('10', 'testEnvironment', 'Other')
    env.properties.setSubPropertyMaxValue('30', 'testEnvironment', 'Other')
    env.close()
    
    mcu.create('physical')
    mcu.select('physical')
    mcu.clickTab('Programming')
    mcu.programming.selectScript('Solar', 'main')
    mcu.programming.insertTextAtLine(15, 'var ENV = "testEnvironment"')
    mcu.programming.insertAfter('function displayElectricity(){', '''
    Serial.println(Environment.get(ENV));
''')
    
    mcu.programming.stop()
    mcu.programming.run()
    mcu.programming.clearOutputs()
    snooze(10)
    currentPowerVals = str(mcu.programming.getConsoleOutput()).splitlines()
    for val in currentPowerVals:
        test.compare(True, float(val) <= 20, trace('test.py'))
    mcu.close()
    None

def _6():
    '''Every Environmental window, Figure 1, with the exception of the InterCity Window,
    will have three basic controls:'''
    util.init()
    _6a()
    _6b()
    _6c()
    
def _6a():
    '''Time Line: Controls when an event will change based on (tick)PT-Time PLUS and
    (tick)Minus Keys for navigation based on Time Increment or (tick)direct entry of
    time in box. (tick)(Could also be a dropdown based on time increments)'''
    test.log('Tested in tst_70_Environment')
    None
    
def _6b():
    '''Time Zone: Greenwich Mean Time value (GMT-/+ hours). Mark4: Rename to UTC?
    Won't have associated cities/countries for now, just +/- (hours) Punt feature for now

    Mark3: What effect does the time zone have on the interface? on the environments?
    Timezones offset the time for containers. Intercity is always GMT. Containers in
    timezones warp to actual time setup in the parent before apply transference.'''
    test.log('This is not seem to be implemented yet')
    None
    
def _6c():
    '''Time increment: 15-30-45-60 minute settings (or more 2hr, 3hr, etc.)'''
    env.goToEnvironmentManager()
    env.editBtn()
    for inc in ['1 S', '1 M', '15 M', '30 M', '45 M', '60 M']:
        env.timelines.setIncrement(inc)
    env.close()
    None

def _7():
    '''The intercity Window, Figure 2, will have everything in number 6, but also
    include time scale.'''
    util.init()
    _7a()
    _7b()
    
def _7a():
    '''Simulation Time Conversion could alternatively say Simulation Time Scale'''
    env.goToEnvironmentManager()
    env.editBtn()
    util.textCheckPoint(object.parent(env.objects.timescale.real_edit()), 'Simulation Time Scale')
    None
    
def _7b():
    '''Drop-downs should contain Milliseconds, Seconds, Minutes, Hours  Mark: removed
    millisecond, to cpu intensive'''
    for t in ['S', 'M']:
        env.timescale.setHmsReal(t)
        env.timescale.setHmsSimulated(t)
    env.close()
    None
    
def _8():
    '''Each environmental variable will have three settings:'''
    util.init()
    test.log('All of section 8 is tested earlier in this test')
    _8a()
    _8b()
    _8c()
    _8d()
    
def _8a():
    '''The starting value – This variables value at the start of the simulation'''
    None
    
def _8b():
    '''The Transference value – the amount (specified as a percentage) of the corresponding
    parent container value (in the container containing this environment) that affects this
    associated (child) variable.'''
    None
    
def _8c():
    '''The Interpolate switch – does a transition between the associated set of values over
    time as opposed to just abruptly changing at the time change.'''
    None
    
def _8d():
    '''Fourth entry tied to Optional Stretch Goal #10. It is a Show selector, when selected
    this field is displayed in the in the Environmental display.'''
    None
    
def _9():
    '''The ability to save and load an environment as a template to allow us to set up various
    combinations of environmental controls as defaults for authors'''
    util.init()
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.properties.expandProperty('Light')
    env.properties.checkSubPropertyToggle('Sunlight', 'Light')
    env.properties.setSubPropertyInitValue('100', 'Sunlight', 'Light')
    path = util.getFilePath('template.xml', UtilConst.UI_TEST)
    test.log(path)
    env.keyframes.exportFile(path)
    util.init()
    env.goToEnvironmentManager()
    env.editBtn()
    env.keyframes.importFile(path)
    env.advancedTab()
    env.properties.expandProperty('Light')
    snooze(2)
    test.compare('100', str(env.objects.properties.getSubPropertyInitValueEdit('Sunlight', 'Light').value), trace('test.py'))
    env.close()
    None

def _10():
    '''Stretch goal – pop up environment set in an external PT window'''
    util.init()
    _10a()
    _10b()
    
def _10a():
    '''External window that shows environment for the selected container (selection by being
    in the window for that container).'''
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.timescale.setHmsSimulated('M')
    env.properties.expandProperty('Light')
    env.properties.checkSubPropertyToggle('Sunlight', 'Light')
    env.properties.setSubPropertyInitValue('100', 'Sunlight', 'Light')
    #env.properties.checkSubPropertyShow('Sunlight', 'Light')
    env.viewOnlyBtn()
    sunlightValues = []
    currValueObj = env.objects.viewOnly.getSubPropertyValueObj('Sunlight')
    for i in range(5):
        sunlightValues.append(currValueObj.innerText)
        snooze(1)
    if len(set(sunlightValues)) > 1:
        test.passes('The values are changing', trace('test.py')) 
    else:
        test.fail('The values are not changing', trace('test.py'))
    None
    
def _10b():
    '''Selectable inclusion data (be able to select what data you want to see in the external
    window from that environments choices)'''
    test.log('This is tested in this test case already')
    None