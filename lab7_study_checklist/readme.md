# Lab 7 - Creating a Study Checklist

I want to gear today's lab towards helping you create your experiments. Today, we will learn about randomization, but also do a high-level review of the major steps in building PsychoPy experiments. I've created a memory study template for visual stimuli that you can work off of. We will review the main steps that go into each experiment. As we go through each step, if you have specific questions pertinent to your own experiment or want me to go into more detail, feel free to ask!

## Random Assignment

Most studies will involve multiple counterbalanced or experimental conditions. You would aim to have the number of subjects in each condition to be equal and randomly assign participants to one of your conditions.

For your purposes, because we know all the subjects, we will do the random assignment ahead of time. **For your final projects, you will need to randomly assign your classmates to one of the conditions in your experiment.**

We will go over an example of this process in a bit. But first, I want to review the `random.shuffle` method that we saw before, and to introduce the concept of a random seed.

#### Random Seed


With this approach, it's necessary to randomly shuffle the image sequence. You'll need to import the random module to do this.


##### Ex 1: Using the `random.shuffle` method:


```python
# import random module
import random
```


```python
# define a sequence to randomize:
sequence = [1, 2, 3, 4, 5]

# shuffle this sequence a few times:
for i in range(4):
    random.shuffle(sequence)
    print(sequence)
```

##### Ex 2: Let's do the same thing as Ex 1, but this time we will first set a randomization seed:


```python
# define a sequence to randomize:
sequence = [1, 2, 3, 4, 5]

# set a randomization seed (can be a character, string, integer, float):
random.seed('ringo_huang')

# shuffle this sequence a few times:
for i in range(4):
    random.shuffle(sequence)
    print(sequence)
```

Notice what happens to the printed sequences when I repeatedly run the code block in Ex 1 versus when I run the code block in Ex 2? What is going on and why?

##### Ex 3: Let's now re-seed with the same seed as Ex 2, and run `random.shuffle` a single time. Compare this shuffled sequence with the first sequence printed in Ex 2:


```python
# define a sequence to randomize:
sequence = [1, 2, 3, 4, 5]

# re-seed with the same seed as Ex 2:
random.seed('ringo_huang')

# shuffle once and compare this to the first shuffle call in Ex 2:
random.shuffle(sequence)
print(sequence)
```

You can think of a seed as a password that unlocks the sequences of your psuedo-random number generator (PRNG). If you pass the same seed to the same PRNG algorithm, you will unlock the same (psuedo)randomizated sequences. This can be an issue if you're not careful! For example, the default randomization seed for Matlab's PTB Shuffle function is the same whenever you launch a new session of Matlab. If you forget to re-seed after you start a new Matlab session you'd be "randomizing" with the same seed, and all your subjects may be getting the same sequence even though you thought they were random! 

The Python `random` module defaults to the OS time as the seed, and so it's not as much of a problem for PsychoPy experiments; however, it is still best practice to set a unique seed for each of your sessions. In your final projects, we expect you to seed your experiments with the participant's full name (e.g. `random.seed('ringo_huang')`).

## Example of Random Assignment - Your Presentation Dates!

On Week 10, you will be presenting your final projects! Half of you are to present on Wednesday of Week 10, and the other half are to present on Friday.

I need to randomly assign 4 of you to present on Wednesday and 4 of you to present on Friday. Right now, I still don't know who will go on Wednesday and who will go on Friday.

We will go through every step of this random assignment together, so that there is complete transparency! In fact, I'll have you choose your own random seed.

The objective here is twofold. At the end of this section, we'll know which 4 of our teams will present on Wednesday and which 4 will present on Friday. Additionally, you will be conducting a very similar procedure when you randomly assign your classmates to different conditions in your experiment.

**Step 1:** Identify the set of "subjects" (or groups in this example) that you need to randomly assign. Here, the eight groups are stored in a list of strings called `groups`. I'm only using the name of the group member whose first name occurs last alphabetically.


```python
groups = ['Alex','Jesse','Jessica','Madeline','Nikki','Nila','Ray','Zongchan']
```

**Step 2:** Let's choose a seed for this randomization! I am placing the fate of your presentation date in your hands. The result of the PRNG algorithm will depend on the seed that you choose. The seed can be a word, a sentence, your favorite number, anything!


```python
random.seed('PINEapple8')
```

**Step 3**: Although there are many procedures for random assignment, I'll stick to using the `shuffle` method.


```python
random.shuffle(groups)
```

**Step 4**: After running Step 3, our `groups` list of teams is now randomly shuffled. For the final step, the first 4 teams in the shuffled list will be assigned to condition 1 (Wednesday) and the last 4 teams will be assigned to condition 2 (Friday).


```python
wednesday_groups = groups[0:4]
friday_groups = groups[4:8]
```

Let's put it all together!


```python
# groups:
groups = ['Alex','Jesse','Jessica','Madeline','Nikki','Nila','Ray','Zongchan']

# random seed:
random.seed('PINEapple8')

# shuffle groups:
random.shuffle(groups)

# assign first 4 to wed, last 4 to fri:
wednesday_groups = groups[0:4]
friday_groups = groups[4:8]

# let's shuffle the order of each condition (wednesday_groups & friday_groups)
random.shuffle(wednesday_groups)
random.shuffle(friday_groups)

print(wednesday_groups)
print(friday_groups)
```

# Presentation Order:

As determined by the seed that your classmates selected ('PINEapple8'), your final project presentations will be done in this order:

## Wednesday (12/1):
1. Alex
2. Nila
3. Zongchan
4. Ray

## Friday (12/3):
1. Madeline
2. Jessica
3. Jesse
4. Nikki

You will be doing a similar procedure in order to randomly assign your classmates to different conditions in your experiment. You would follow the same procedure as above, but the main difference is that you substitute the "Wednesday" and "Friday" conditions with your experiment conditions (can be 2 or more).

## Experiment templates

Several proposals involve a memory test of some sort. I will go over a very basic memory test experiment and point out the following main steps that are involved in building these sorts of experiments.

You can then use this experiment file as a template for your own experiments.

#### Read in the stimuli list
The following code will go in code components in our example PsychoPy code component in the "Begein Experiment" tab. We're simpling reading the data from a file called stimuli_list into a list called `stimuli_list`. We are then taking each of the columns in stimuli_list.xlsx and putting it into separate lists.


```python
# Import stimuli_list
stimuli_list = data.importConditions('stimuli_list.xlsx')

animal_images = list()
tool_images = list()
produce_images = list()
for item in stimuli_list:
    animal_images.append(item['Animal_Image_Files'])
    tool_images.append(item['Tool_Image_Files'])
    produce_images.append(item['Produce_Image_Files'])
```

#### Randomization and building presentation sequences
Where and why should you add `random.shuffle`? 
1. Randomly select a subset of our full set of images (e.g., you may only want to present 3 out of 6 images during the encoding phase)
2. If there's some sort of pattern in your list sequence, call `random.shuffle` to randomize the full sequence.

#### Create routines and add components to each routine
Some important reminders:
1. Remember to use the $ special character when you want a field to be a variable.
2. Remember to "set every repeat" for fields that need to be updated with each iteration of a loop.
3. `thisRepN` is an attribute of the loop object that keeps track of which iteration you are on. This is often used as the index in your sequence lists.

#### Log data
1. Use the `pandas` module for convenience. Put `import pandas as pd` in your "Begin Experiment" tab.
2. In the "End Routine" tab of each trial, record the relevant data in something called a `trial_list`. This `trial_list` can then be appended to something called a `session_list`.
3. At the end of the experiment, you can convert `session_list` (which is a list of `trial_list`'s) to a dataframe. This dataframe can then be put into a csv file.

### For Auditory Stimuli:
The steps are very similar to the steps for the visual memory test, but you'll be creating sequences based on the auditory file names instead of the image filenames. You'll also be using the "Sound" component instead of the "Image" component.

If interested, I can show you how to adapt the Image Memory test template for Auditory stimuli.
