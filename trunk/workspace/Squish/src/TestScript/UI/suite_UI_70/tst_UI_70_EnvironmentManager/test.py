##Chris Allen

from API.Utility.Util import Util
from API.Environment.Environment import Environment
from API.functions import toInt
from API.functions import trace
import time

util = Util()
env = Environment()

def main():
    util.init()
    start = time.time()
    testOpenAndClose()
    testPauseStart()
    testChangeTimeScale()
    testChangeTimeLine()
    testChangingKeyframe()
    testAddingNotes()
    testSelectingProperties()
    end = time.time()
    test.log(str((end-start)))
    None

def testOpenAndClose():
    env.goToEnvironmentManager()
    test.compare(True, env.getEnvironmentWindow().visible, trace('test.py'))
    env.close()
    try:
        window = env.getEnvironmentWindow()
        test.compare(False, window.visible, trace('test.py'))
    except LookupError, e:
        pass
    except Exception, e:
        raise Exception(e)
    
    snooze(2)

def testPauseStart():
    env.goToEnvironmentManager()
    currTime = env.getCurrentTime()
    snooze(2)
    newTime = env.getCurrentTime()
    if convertTime(newTime) > convertTime(currTime):
        test.passes('Time is progressing')
    else:
        test.fail('Time stayed the same', trace('test.py'))
        env.pause()
    env.pause()
    snooze(1)
    currTime = env.getCurrentTime()
    snooze(2)
    newTime = env.getCurrentTime()
    if convertTime(newTime) == convertTime(currTime):
        test.passes('Time is the same')
    else:
        test.fail('Time is NOT the same', trace('test.py'))
    env.start()
    currTime = env.getCurrentTime()
    snooze(2)
    newTime = env.getCurrentTime()
    if convertTime(newTime) > convertTime(currTime):
        test.passes('Time is progressing')
    else:
        test.fail('Time stayed the same', trace('test.py'))
    env.close()

def testChangeTimeScale():
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.timescale.setSimulationTimeScale(2, 30, 'M', 'M')
    env.textCheckPoint(env.objects.timescale.real_edit().value, '2')
    env.textCheckPoint(env.objects.timescale.simulation_edit().value, '30')
    env.textCheckPoint(env.objects.timescale.hms_real_combo().selectedOption, 'Minute')
    env.textCheckPoint(env.objects.timescale.hms_simulation_combo().selectedOption, 'Minute')
    env.close()

def testChangeTimeLine():
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.timelines.increment()
    currTime = env.objects.timeline.edit().value[:-2]
    currTimeTuple = convertTime(currTime)
    baseTimeTuple = convertTime('12:00:00')
    difference = ((currTimeTuple[1] * 60 + currTimeTuple[2]) - (baseTimeTuple[1] * 60 + baseTimeTuple[2]))
    test.log(str(difference))
    if 50 < difference < 80:#Check the difference is about 1 minute
        test.passes('The time was incremented')
    else:
        test.fail('The minute was not incremented by one', trace('test.py'))
    
    env.timelines.decrement()
    baseTime = currTime
    currTime = env.objects.timeline.edit().value[:-2]
    currTimeTuple = convertTime(currTime)
    baseTimeTuple = convertTime(baseTime)
    difference = ((currTimeTuple[1] * 60 + currTimeTuple[2]) - (baseTimeTuple[1] * 60 + baseTimeTuple[2]))
    if 50 < -difference < 70:#Check the difference is about 1 minute
        test.passes('The time was decremented')
    else:
        test.fail('The minute was not decremented by one', trace('test.py'))
    
    env.timelines.setIncrement('45 M')
    env.textCheckPoint(env.objects.timeline.combo().selectedOption, '45 Minutes')
    env.close()
    
def testChangingKeyframe():
    env.goToEnvironmentManager()
    env.editBtn()
    if toInt(env.keyframes.getCurrentKeyframe()) == 1:
        test.passes('Current frame is 1')
    else:
        test.fail('Current frame is not 1', trace('test.py'))
    
    env.keyframes.next()
    if toInt(env.keyframes.getCurrentKeyframe()) == 2:
        test.passes('Current frame is 2')
    else:
        test.fail('Current frame is not 2', trace('test.py'))
    
    env.timelines.increment()
    env.keyframes.add()
    if toInt(env.keyframes.getTotalKeyframe()) == 6:
        test.passes('Total is 6')
    else:
        test.fail('Total is NOT 6', trace('test.py'))
    
    #for i in range(toInt(env.keyframes.getTotalKeyframe()) - toInt(env.keyframes.getCurrentKeyframe())):
    #    env.keyframes.next()
    env.keyframes.remove()
    if toInt(env.keyframes.getTotalKeyframe()) == 5:
        test.passes('Total is 5')
    else:
        test.fail('Total is NOT 5', trace('test.py'))
    
    #Check can't remove the first and last
    for i in range(toInt(env.keyframes.getTotalKeyframe())):
        if toInt(env.keyframes.getCurrentKeyframe()) == 1:
            break
        env.keyframes.previous()
    for i in range(toInt(env.keyframes.getTotalKeyframe()) - 2):#Remove all but first and last
        env.keyframes.next()
        env.keyframes.remove()
    if toInt(env.keyframes.getTotalKeyframe()) == 2:
        test.passes('Total is 2')
    else:
        test.fail('Total is NOT 2', trace('test.py'))
    env.close()
    
def testAddingNotes():
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.addNote('This is a test')
    env.showNotes()
    env.textCheckPoint(env.objects.note_textedit().value, 'This is a test')
    if env.objects.show_notes_checkbox().checked:
        test.passes('Checked')
    else:
        test.fail('Show notes is not checked', trace('test.py'))
        
    env.hideNotes()
    if env.objects.show_notes_checkbox().checked:
        test.fail('Checked', trace('test.py'))
    else:
        test.passes('Show notes is not checked')
    env.close()
    
def testSelectingProperties():
    env.goToEnvironmentManager()
    env.editBtn()
    env.advancedTab()
    env.properties.advancedSettingsCheckbox()
    env.properties.checkProperty('Earth Physical Features')
    env.properties.expandProperty('Electricity')
    env.properties.checkSubPropertyToggle('Ohms', 'Electricity')
    env.properties.setSubPropertyInitValue('1', 'Ohms', 'Electricity')
    env.properties.setSubPropertyMinValue('0', 'Ohms', 'Electricity')
    env.properties.setSubPropertyMaxValue('1000000000', 'Ohms', 'Electricity')
    env.properties.setSubPropertyTransference('0', 'Ohms', 'Electricity')
    env.properties.checkSubPropertyInterpolate('Ohms', 'Electricity')
    env.properties.checkSubPropertyShow('Ohms', 'Electricity')
    check(env.objects.properties.getSubPropertyInitValueEdit('Ohms', 'Electricity').value == '1')
    check(env.objects.properties.getSubPropertyMinValueEdit('Ohms', 'Electricity').value == '0')
    check(env.objects.properties.getSubPropertyMaxValueEdit('Ohms', 'Electricity').value == '1000000000')
    check(env.objects.properties.getSubPropertyTransferenceValueEdit('Ohms', 'Electricity').value == '0')
    check(not env.objects.properties.getSubPropertyInterpolateCheckbox('Ohms', 'Electricity').checked)
    check(env.objects.properties.getSubPropertyShowCheckbox('Ohms', 'Electricity').checked)
    
def check(condition, msg = 'Fail'):
    if condition:
        test.passes('PASS')
    else:
        test.fail(msg, trace('test.py'))
    None

def convertTime(p_time):
    return time.strptime(p_time, '%H:%M:%S')[3:6]#Returns hour minute second in tuple format