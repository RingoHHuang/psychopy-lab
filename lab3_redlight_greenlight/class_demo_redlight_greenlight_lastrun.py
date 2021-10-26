#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on October 19, 2021, at 16:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'class_demo_redlight_greenlight'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\huang\\Desktop\\Github\\RingoHHuang\\psychopy-lab\\lab3_redlight_greenlight\\class_demo_redlight_greenlight_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instr_text = visual.TextStim(win=win, name='instr_text',
    text='The game that you are about to play is called Red Light, Green Light. You will see a rapid serial presentation of two dolls - one facing forward and the other facing backwards. Whenever you see a doll facing backwards ("Green Light"), you will respond by pressing the space bar as quickly as you can. Whenever you see a doll facing forwards ("Red Light"), you will withhold responding. \n\nWhen you\'re ready, please press the spacebar to begin!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intr_kb = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
# Approach 1 (simple hard-coding):
#im_sequence = ["resources\squid_game_doll_backward", "resources\squid_game_doll_backward", "resources\squid_game_doll_backward", "resources\squid_game_doll_forward"]

# Approach 3 (using indexing):
sequence = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0]
image_names = ["resources\squid_game_doll_backward","resources\squid_game_doll_forward"]

im_sequence = []
for i in sequence:
    im_sequence.append(image_names[i])
    
# Specify the nReps:
seq_len = len(sequence)
doll_im = visual.ImageStim(
    win=win,
    name='doll_im', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.35, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
task_kb = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
fb_text = visual.TextStim(win=win, name='fb_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fb_kb = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
intr_kb.keys = []
intr_kb.rt = []
_intr_kb_allKeys = []
# keep track of which components have finished
instrComponents = [instr_text, intr_kb]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text* updates
    if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text.frameNStart = frameN  # exact frame index
        instr_text.tStart = t  # local t and not account for scr refresh
        instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        instr_text.setAutoDraw(True)
    if instr_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_text.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            instr_text.tStop = t  # not accounting for scr refresh
            instr_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_text, 'tStopRefresh')  # time at next scr refresh
            instr_text.setAutoDraw(False)
    
    # *intr_kb* updates
    waitOnFlip = False
    if intr_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intr_kb.frameNStart = frameN  # exact frame index
        intr_kb.tStart = t  # local t and not account for scr refresh
        intr_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intr_kb, 'tStartRefresh')  # time at next scr refresh
        intr_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intr_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intr_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intr_kb.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > intr_kb.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            intr_kb.tStop = t  # not accounting for scr refresh
            intr_kb.frameNStop = frameN  # exact frame index
            win.timeOnFlip(intr_kb, 'tStopRefresh')  # time at next scr refresh
            intr_kb.status = FINISHED
    if intr_kb.status == STARTED and not waitOnFlip:
        theseKeys = intr_kb.getKeys(keyList=['space'], waitRelease=False)
        _intr_kb_allKeys.extend(theseKeys)
        if len(_intr_kb_allKeys):
            intr_kb.keys = _intr_kb_allKeys[-1].name  # just the last key pressed
            intr_kb.rt = _intr_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_text.started', instr_text.tStartRefresh)
thisExp.addData('instr_text.stopped', instr_text.tStopRefresh)
# check responses
if intr_kb.keys in ['', [], None]:  # No response was made
    intr_kb.keys = None
thisExp.addData('intr_kb.keys',intr_kb.keys)
if intr_kb.keys != None:  # we had a response
    thisExp.addData('intr_kb.rt', intr_kb.rt)
thisExp.addData('intr_kb.started', intr_kb.tStartRefresh)
thisExp.addData('intr_kb.stopped', intr_kb.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=seq_len, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(1.200000)
    # update component parameters for each repeat
    doll_im_path = im_sequence[trials.thisRepN]
    doll_im.setImage(doll_im_path)
    task_kb.keys = []
    task_kb.rt = []
    _task_kb_allKeys = []
    # keep track of which components have finished
    trialComponents = [doll_im, task_kb]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *doll_im* updates
        if doll_im.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            doll_im.frameNStart = frameN  # exact frame index
            doll_im.tStart = t  # local t and not account for scr refresh
            doll_im.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(doll_im, 'tStartRefresh')  # time at next scr refresh
            doll_im.setAutoDraw(True)
        if doll_im.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > doll_im.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                doll_im.tStop = t  # not accounting for scr refresh
                doll_im.frameNStop = frameN  # exact frame index
                win.timeOnFlip(doll_im, 'tStopRefresh')  # time at next scr refresh
                doll_im.setAutoDraw(False)
        
        # *task_kb* updates
        waitOnFlip = False
        if task_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            task_kb.frameNStart = frameN  # exact frame index
            task_kb.tStart = t  # local t and not account for scr refresh
            task_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(task_kb, 'tStartRefresh')  # time at next scr refresh
            task_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(task_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(task_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if task_kb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > task_kb.tStartRefresh + 1.2-frameTolerance:
                # keep track of stop time/frame for later
                task_kb.tStop = t  # not accounting for scr refresh
                task_kb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(task_kb, 'tStopRefresh')  # time at next scr refresh
                task_kb.status = FINISHED
        if task_kb.status == STARTED and not waitOnFlip:
            theseKeys = task_kb.getKeys(keyList=['space'], waitRelease=False)
            _task_kb_allKeys.extend(theseKeys)
            if len(_task_kb_allKeys):
                task_kb.keys = _task_kb_allKeys[-1].name  # just the last key pressed
                task_kb.rt = _task_kb_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('doll_im.started', doll_im.tStartRefresh)
    trials.addData('doll_im.stopped', doll_im.tStopRefresh)
    # check responses
    if task_kb.keys in ['', [], None]:  # No response was made
        task_kb.keys = None
    trials.addData('task_kb.keys',task_kb.keys)
    if task_kb.keys != None:  # we had a response
        trials.addData('task_kb.rt', task_kb.rt)
    trials.addData('task_kb.started', task_kb.tStartRefresh)
    trials.addData('task_kb.stopped', task_kb.tStopRefresh)
    thisExp.nextEntry()
    
# completed seq_len repeats of 'trials'


# ------Prepare to start Routine "feedback"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# Grabs the keys for task_kb
task_kb_keys = trials.data['task_kb.keys']

# Counts of commission errors and nogo trials
commission_error_count = 0
nogo_count = 0
for i in range(len(task_kb_keys[0])):
    # Checks if it is a nogo trial
    if sequence[i] == 1:
        nogo_count += 1
        # Checks if a space was pressed (and it was a nogo trial)
        if task_kb_keys[0][i] == 'space':
            commission_error_count += 1

# Calculate commision error rate based on counts
commission_error_rate = commission_error_count/nogo_count

# build the feedback string
feedback_str = 'Commission error rate: ' + str(commission_error_rate)
fb_text.setText(feedback_str)
fb_kb.keys = []
fb_kb.rt = []
_fb_kb_allKeys = []
# keep track of which components have finished
feedbackComponents = [fb_text, fb_kb]
for thisComponent in feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fb_text* updates
    if fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fb_text.frameNStart = frameN  # exact frame index
        fb_text.tStart = t  # local t and not account for scr refresh
        fb_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fb_text, 'tStartRefresh')  # time at next scr refresh
        fb_text.setAutoDraw(True)
    if fb_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fb_text.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            fb_text.tStop = t  # not accounting for scr refresh
            fb_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fb_text, 'tStopRefresh')  # time at next scr refresh
            fb_text.setAutoDraw(False)
    
    # *fb_kb* updates
    waitOnFlip = False
    if fb_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fb_kb.frameNStart = frameN  # exact frame index
        fb_kb.tStart = t  # local t and not account for scr refresh
        fb_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fb_kb, 'tStartRefresh')  # time at next scr refresh
        fb_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(fb_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(fb_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if fb_kb.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fb_kb.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            fb_kb.tStop = t  # not accounting for scr refresh
            fb_kb.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fb_kb, 'tStopRefresh')  # time at next scr refresh
            fb_kb.status = FINISHED
    if fb_kb.status == STARTED and not waitOnFlip:
        theseKeys = fb_kb.getKeys(keyList=['space'], waitRelease=False)
        _fb_kb_allKeys.extend(theseKeys)
        if len(_fb_kb_allKeys):
            fb_kb.keys = _fb_kb_allKeys[-1].name  # just the last key pressed
            fb_kb.rt = _fb_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fb_text.started', fb_text.tStartRefresh)
thisExp.addData('fb_text.stopped', fb_text.tStopRefresh)
# check responses
if fb_kb.keys in ['', [], None]:  # No response was made
    fb_kb.keys = None
thisExp.addData('fb_kb.keys',fb_kb.keys)
if fb_kb.keys != None:  # we had a response
    thisExp.addData('fb_kb.rt', fb_kb.rt)
thisExp.addData('fb_kb.started', fb_kb.tStartRefresh)
thisExp.addData('fb_kb.stopped', fb_kb.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
