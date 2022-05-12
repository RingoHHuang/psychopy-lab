#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on November 12, 2021, at 09:53
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
expName = 'visual_memory_template'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\huang\\Box\\186C\\week7\\visual_memory_template.py',
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
text = visual.TextStim(win=win, name='text',
    text='Welcome!\n\nCateegorize the images:\n1=Animal\n2=Produce\n3=Tool',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
import random

# Import stimuli_list
stimuli_list = data.importConditions('stimuli_list.xlsx')

animal_images = list()
tool_images = list()
produce_images = list()
for item in stimuli_list:
    animal_images.append(item['Animal_Image_Files'])
    tool_images.append(item['Tool_Image_Files'])
    produce_images.append(item['Produce_Image_Files'])



# Select three from each category to be encoded:
random.seed(expInfo['participant'])
random.shuffle(animal_images)
random.shuffle(tool_images)
random.shuffle(produce_images)
phase_1_animals = animal_images[0:3]
phase_1_tools = tool_images[0:3]
phase_1_produce = produce_images[0:3]

# Build the phase_1_sequence:
phase_1_sequence = list()
for im in phase_1_animals:
    phase_1_sequence.append(im)
for im in phase_1_tools:
    phase_1_sequence.append(im)
for im in phase_1_produce:
    phase_1_sequence.append(im)
random.shuffle(phase_1_sequence)

# Build the phase_2_sequence:
phase_2_sequence = list()
for im in animal_images:
    phase_2_sequence.append(im)
for im in tool_images:
    phase_2_sequence.append(im)
for im in produce_images:
    phase_2_sequence.append(im)
random.shuffle(phase_2_sequence)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "encoding"
encodingClock = core.Clock()
encoding_image = visual.ImageStim(
    win=win,
    name='encoding_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
encoding_kb = keyboard.Keyboard()
import pandas as pd

# initiate this
encoding_session_list = list()

# Initialize components for Routine "random_task"
random_taskClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='delay task?\n\nnext test - memory\n\n1=old\n2=new',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "memory"
memoryClock = core.Clock()
memory_image = visual.ImageStim(
    win=win,
    name='memory_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
memory_kb = keyboard.Keyboard()
memory_session_list = list()




# Initialize components for Routine "finished"
finishedClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='you finished\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [text, key_resp]
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
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
phase_1 = data.TrialHandler(nReps=9.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='phase_1')
thisExp.addLoop(phase_1)  # add the loop to the experiment
thisPhase_1 = phase_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPhase_1.rgb)
if thisPhase_1 != None:
    for paramName in thisPhase_1:
        exec('{} = thisPhase_1[paramName]'.format(paramName))

for thisPhase_1 in phase_1:
    currentLoop = phase_1
    # abbreviate parameter names if possible (e.g. rgb = thisPhase_1.rgb)
    if thisPhase_1 != None:
        for paramName in thisPhase_1:
            exec('{} = thisPhase_1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "encoding"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    encoding_im = phase_1_sequence[phase_1.thisRepN]
    
    
    encoding_image.setImage(encoding_im)
    encoding_kb.keys = []
    encoding_kb.rt = []
    _encoding_kb_allKeys = []
    # keep track of which components have finished
    encodingComponents = [encoding_image, encoding_kb]
    for thisComponent in encodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    encodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "encoding"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = encodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=encodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encoding_image* updates
        if encoding_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_image.frameNStart = frameN  # exact frame index
            encoding_image.tStart = t  # local t and not account for scr refresh
            encoding_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_image, 'tStartRefresh')  # time at next scr refresh
            encoding_image.setAutoDraw(True)
        if encoding_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                encoding_image.tStop = t  # not accounting for scr refresh
                encoding_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_image, 'tStopRefresh')  # time at next scr refresh
                encoding_image.setAutoDraw(False)
        
        # *encoding_kb* updates
        waitOnFlip = False
        if encoding_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encoding_kb.frameNStart = frameN  # exact frame index
            encoding_kb.tStart = t  # local t and not account for scr refresh
            encoding_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encoding_kb, 'tStartRefresh')  # time at next scr refresh
            encoding_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(encoding_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(encoding_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if encoding_kb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encoding_kb.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                encoding_kb.tStop = t  # not accounting for scr refresh
                encoding_kb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encoding_kb, 'tStopRefresh')  # time at next scr refresh
                encoding_kb.status = FINISHED
        if encoding_kb.status == STARTED and not waitOnFlip:
            theseKeys = encoding_kb.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _encoding_kb_allKeys.extend(theseKeys)
            if len(_encoding_kb_allKeys):
                encoding_kb.keys = _encoding_kb_allKeys[-1].name  # just the last key pressed
                encoding_kb.rt = _encoding_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in encodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "encoding"-------
    for thisComponent in encodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    phase_1.addData('encoding_image.started', encoding_image.tStartRefresh)
    phase_1.addData('encoding_image.stopped', encoding_image.tStopRefresh)
    # check responses
    if encoding_kb.keys in ['', [], None]:  # No response was made
        encoding_kb.keys = None
    phase_1.addData('encoding_kb.keys',encoding_kb.keys)
    if encoding_kb.keys != None:  # we had a response
        phase_1.addData('encoding_kb.rt', encoding_kb.rt)
    phase_1.addData('encoding_kb.started', encoding_kb.tStartRefresh)
    phase_1.addData('encoding_kb.stopped', encoding_kb.tStopRefresh)
    
    encoding_resp = encoding_kb.keys
    encoding_rt = encoding_kb.rt
    
    encoding_trial_list = [encoding_im, encoding_resp, encoding_rt]
    
    encoding_session_list.append(encoding_trial_list)
    thisExp.nextEntry()
    
# completed 9.0 repeats of 'phase_1'


# ------Prepare to start Routine "random_task"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
random_taskComponents = [text_2, key_resp_3]
for thisComponent in random_taskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
random_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "random_task"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = random_taskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=random_taskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_3.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in random_taskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "random_task"-------
for thisComponent in random_taskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
phase_2 = data.TrialHandler(nReps=18.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='phase_2')
thisExp.addLoop(phase_2)  # add the loop to the experiment
thisPhase_2 = phase_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPhase_2.rgb)
if thisPhase_2 != None:
    for paramName in thisPhase_2:
        exec('{} = thisPhase_2[paramName]'.format(paramName))

for thisPhase_2 in phase_2:
    currentLoop = phase_2
    # abbreviate parameter names if possible (e.g. rgb = thisPhase_2.rgb)
    if thisPhase_2 != None:
        for paramName in thisPhase_2:
            exec('{} = thisPhase_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "memory"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    memory_im = phase_2_sequence[phase_2.thisRepN]
    
    
    memory_image.setImage(memory_im)
    memory_kb.keys = []
    memory_kb.rt = []
    _memory_kb_allKeys = []
    # keep track of which components have finished
    memoryComponents = [memory_image, memory_kb]
    for thisComponent in memoryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    memoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "memory"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = memoryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=memoryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *memory_image* updates
        if memory_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            memory_image.frameNStart = frameN  # exact frame index
            memory_image.tStart = t  # local t and not account for scr refresh
            memory_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memory_image, 'tStartRefresh')  # time at next scr refresh
            memory_image.setAutoDraw(True)
        if memory_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > memory_image.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                memory_image.tStop = t  # not accounting for scr refresh
                memory_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(memory_image, 'tStopRefresh')  # time at next scr refresh
                memory_image.setAutoDraw(False)
        
        # *memory_kb* updates
        waitOnFlip = False
        if memory_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            memory_kb.frameNStart = frameN  # exact frame index
            memory_kb.tStart = t  # local t and not account for scr refresh
            memory_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memory_kb, 'tStartRefresh')  # time at next scr refresh
            memory_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(memory_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(memory_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if memory_kb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > memory_kb.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                memory_kb.tStop = t  # not accounting for scr refresh
                memory_kb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(memory_kb, 'tStopRefresh')  # time at next scr refresh
                memory_kb.status = FINISHED
        if memory_kb.status == STARTED and not waitOnFlip:
            theseKeys = memory_kb.getKeys(keyList=['1', '2'], waitRelease=False)
            _memory_kb_allKeys.extend(theseKeys)
            if len(_memory_kb_allKeys):
                memory_kb.keys = _memory_kb_allKeys[-1].name  # just the last key pressed
                memory_kb.rt = _memory_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memoryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "memory"-------
    for thisComponent in memoryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    phase_2.addData('memory_image.started', memory_image.tStartRefresh)
    phase_2.addData('memory_image.stopped', memory_image.tStopRefresh)
    # check responses
    if memory_kb.keys in ['', [], None]:  # No response was made
        memory_kb.keys = None
    phase_2.addData('memory_kb.keys',memory_kb.keys)
    if memory_kb.keys != None:  # we had a response
        phase_2.addData('memory_kb.rt', memory_kb.rt)
    phase_2.addData('memory_kb.started', memory_kb.tStartRefresh)
    phase_2.addData('memory_kb.stopped', memory_kb.tStopRefresh)
    memory_resp = memory_kb.keys
    memory_rt = memory_kb.rt
    
    memory_trial_list = [memory_im, memory_resp, memory_rt]
    
    memory_session_list.append(memory_trial_list)
    thisExp.nextEntry()
    
# completed 18.0 repeats of 'phase_2'


# ------Prepare to start Routine "finished"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# Write encoding data
session_df = pd.DataFrame(encoding_session_list,
                         columns = ["encoding_im", "encoding_resp", "encoding_rt"])

output_filepath = 'sub-' + expInfo['participant'] + '_encoding.csv'

session_df.to_csv(output_filepath)

# Write memory data
session_df = pd.DataFrame(memory_session_list,
                         columns = ["memory_im", "memory_resp", "memory_rt"])

output_filepath = 'sub-' + expInfo['participant'] + '_memory.csv'

session_df.to_csv(output_filepath)

# keep track of which components have finished
finishedComponents = [text_3]
for thisComponent in finishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finished"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finished"-------
for thisComponent in finishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

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
