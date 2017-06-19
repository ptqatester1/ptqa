from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API.ActivityWizard.ActivityWizard import ActivityWizard
from API import functions

from API.Device.Ioe.MCU import MCU

util = Util()
aw = ActivityWizard()

player = MCU('Player', 545, 405, 'player')
directions = {'r': 'Right', 'l': 'Left', 'u': 'Up', 'd': 'Down'}

def main():
    open_sample('7.1/ioe/sokoban/sokoban.pka')
    play_game()
    check_results()

def open_sample(file_path):
    util.init()
    util.maximizePT()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()
    aw.instructionDialog.close()

def play_game():
    steps = [
        'r', 'u', 'u', 'l', 'l', 'l', 'u', 'l', 'd',
        'r', 'r', 'r', 'r', 'd', 'd', 'l', 'u', 'r',
        'u', 'l', 'l', 'l', 'd', 'd', 'l', 'l', 'l',
        'u', 'u', 'r', 'r', 'd', 'r', 'd', 'l', 'u',
        'u', 'u', 'r', 'd', 'd'
        ]
    select_player()
    snooze(1)
    initial_move(steps.pop(0))
    for step in steps:
        move_player(step)

def select_player():
    util.selectObject(util.currentWorkspace, player.x, player.y)

def initial_move(direction):
    window = util.currentWorkspace.split('.')[0]
    util.typeText(window, '<Shift+%s>' % (directions[direction]))

def move_player(direction):
    window = util.currentWorkspace.split('.')[0]
    util.typeText(window, '<%s>' % (directions[direction]))

def check_results():
    aw.instructionDialog.checkResultsButton()
    aw.instructionDialog.results.overallFeedback.textCheckPoint('Congratulations on completing this activity!')
