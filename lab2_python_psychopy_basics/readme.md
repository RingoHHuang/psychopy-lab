## Psych 186C Worksheet

Topics to be covered:
- data containers (lists and dictionaries)
- control flow (`if..elif..else` statements)
- loops (`for` and `while` loops)
- functions
- useful functions
- object-oriented programming
- intro to PsychoPy GUI

In today's lab, we will continue where we left off with a few important Python programming concepts. I will then introduce the PsychoPy GUI and describe how the programming concepts we covered relate to different elements in the GUI. We tinker with a demo of the Sternberg Working Memory Task that was built using the PsychoPy GUI.

In the first part of lab, I will go over and give a live demo of all the sections in the worksheet. There are some Exercises throughout the worksheet, which you will work on after I finish the live demo (time-permitting). 

## Lists
Lists are defined by using square brackets `[]` and will contain a list of other data types. These other data types can be ints, strings, other lists, among other things.


```python
list1 = [1, 4, 6]
print(list1)
```

    [1, 4, 6]
    


```python
list2 = ['apple', 'orange', 'pear']
print(list2)
```

    ['apple', 'orange', 'pear']
    

Oftentimes, you'll want to interact with or modify your lists. You can do so using a variety approaches, including built-in methods. A review of Python list methods can be found here: https://www.programiz.com/python-programming/methods/list/index. We will go over common use cases of lists.

##### Accessing an element in the list
Importantly, in Python, the first index of a list starts with `0`. This is different from some other languages like Matlab, which starts with a `1`.


```python
item = list2[1]

print(item)
```

    orange
    

You may also access arange of elements using the following notation:


```python
#here we access the 2nd to 7th elements in a list and assign it to a new list variable
big_list = ['orange','apple','pear','watermelon','cherry','lime','lemon', 3, 6, ['list', 'of','other','things']]
small_list = big_list[2:7]
print(small_list)
```

    ['pear', 'watermelon', 'cherry', 'lime', 'lemon']
    

##### Replacing an element in the list


```python
list2[0] = 3

print(list2)
```

    [3, 'orange', 'pear']
    

##### Adding an element to the list
There are two main ways to add an element to the list.

Using the `append()` method:


```python
print(list1)

list1.append(3)

print(list1)
```

    [1, 4, 6]
    [1, 4, 6, 3]
    

Using the `+` operator, you can concatenate two lists together. You can also add a single element if it is contained within a list:


```python
# adding a single element:
list1 = list1 + [3]
print(list1)

# concatenating two lists:
list_concatenated = list1 + list2
print(list_concatenated)
```

    [1, 4, 6, 3, 3]
    [1, 4, 6, 3, 3, 3, 'orange', 'pear']
    

### Exercise 2.1
(a) Fix the error in this code so that it adds an element to the list:


```python
list1 = list1 + 8

print(list1)
```

(b) Does the following code concatenate `list1` and `list2`?


```python
list1.append(list2)

print(list1)
```

(c) If you want to use a list method instead of the `+` operator to concatenate two lists, you can use `extend()`. Use the `extend()` list method to concatenate `list1` and `list2`.


```python
# Concatenate list1 and list2 using extend():


```

##### Removing an element (if you know the index)

Use the `pop()` method:


```python
# Remove the 2nd item from the list:
print(big_list)
big_list.pop(1)
print(big_list)

# Remove the last item from the list:
big_list.pop(-1)
print(big_list)
```

    ['orange', 'apple', 'pear', 'watermelon', 'cherry', 'lime', 'lemon', 3, 6, ['list', 'of', 'other', 'things']]
    ['orange', 'pear', 'watermelon', 'cherry', 'lime', 'lemon', 3, 6, ['list', 'of', 'other', 'things']]
    ['orange', 'pear', 'watermelon', 'cherry', 'lime', 'lemon', 3, 6]
    

Use the `del` statement:


```python
# delete the 1st and 2nd element of the list:

del big_list[1]
print(big_list)
```

    ['pear', 'cherry', 'lime', 'lemon', 3, 6]
    

##### Copying a list
Let's say you want to modify a list, but you want to save the state of the current list. How would you go about doing so?

In Matlab, you might assign an array (or cell or data struct) to a different variable and modify the new array variable. What happens if you use this approach in Python?


```python
# Matlab-like approach:
fruit_list = ['orange','apple','pear','watermelon','cherry','lime','lemon']
print(fruit_list)

# Assign list to a new variable:
temp_list = fruit_list

# Modify temp_list:
temp_list[0] = 'dragonfruit'
temp_list.pop(-1)

# Print temp_list
print(temp_list)
```

    ['orange', 'apple', 'pear', 'watermelon', 'cherry', 'lime', 'lemon']
    ['dragonfruit', 'apple', 'pear', 'watermelon', 'cherry', 'lime']
    

Everything looks fine right? But what happens when we print `fruit_list`, which is the original copy that we wanted to save:


```python
print(fruit_list)
```

    ['dragonfruit', 'apple', 'pear', 'watermelon', 'cherry', 'lime']
    

As you can see, the modifications that we did to `temp_list` transfers to `fruit_list`. When we make assignments in Python, we did not actually make a copy of the object. In order to make a copy, we will use the `copy()` method:


```python
fruit_list = ['orange','apple','pear','watermelon','cherry','lime','lemon']
print(fruit_list)

# Assign a copy of fruit_list to temp_list
temp_list = fruit_list.copy()

# Modify temp_list:
temp_list[0] = 'dragonfruit'
temp_list.pop(-1)

# Print temp_list
print(temp_list)

# Print the original fruit_list:
print(fruit_list)
```

    ['orange', 'apple', 'pear', 'watermelon', 'cherry', 'lime', 'lemon']
    ['dragonfruit', 'apple', 'pear', 'watermelon', 'cherry', 'lime']
    ['orange', 'apple', 'pear', 'watermelon', 'cherry', 'lime', 'lemon']
    

##### Find the length of a list
You can find the length of a list (how many elements are contained in it) by using the `len()` function:


```python
len(fruit_list)
```




    7



### Exercise 2.2
Use `len()` function to find and print the lengths of `list1` and `list2`. Why do you think `list2` is longer than `list1`?


```python
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, [4, 5, 6]]




```

## Sets
Sets are similar to lists, but they don't maintain item order (so there is no indexing) and they don't maintain duplicate elements. You define a set by using curly braces `{}`


```python
set1 = {1, 2, 3}
print(set1)
```

    {1, 2, 3}
    


```python
set2 = {1, 2, 3, 4, 3, 2, 1, 'a', 1.5}
print(set2)
```

    {1, 2, 3, 4, 1.5, 'a'}
    

## Dictionaries 
Dictionaries are similar to lists, but they assign a key-value pair to represent items. Dicts are defined using curly braces `{}` and must be provided at least one key-value pair, which takes the following form `key:value`. While values can be whatever data type you like (lists, integers, strings, other dictionaries), key's must be a string.


```python
shopping_list = {
    'fruits': ['orange', 'apple','pear'],
    'soda': ['coke','dr. pepper'],
    'vegetables': None
}
shopping_list
```




    {'fruits': ['orange', 'apple', 'pear'],
     'soda': ['coke', 'dr. pepper'],
     'vegetables': None}




```python
#we access values in a dict by indexing the dictionary with the key name
shopping_list['fruits']
```




    ['orange', 'apple', 'pear']




```python
#we can easily add to our dictionary in one of two ways. First we can add an item to a key that is already present
shopping_list['fruits'].append('banana')

print(shopping_list['fruits'])
```

    ['orange', 'apple', 'pear', 'banana']
    


```python
#or we can create a new key and add it to the dictionary 
shopping_list['breads'] = 'Daves Killer Bread' 
shopping_list
```




    {'fruits': ['orange', 'apple', 'pear', 'banana'],
     'soda': ['coke', 'dr. pepper'],
     'vegetables': None,
     'breads': 'Daves Killer Bread'}



### Exercise 2.3
Why do you think we can use the `append()` method with `shopping_list['fruits']`?  What data type is `shopping_list['fruits']`? Use the `type()` function to find out the data type of `shopping_list['fruits']` and `shopping_list`: 


```python
# Use type() to figure out the data types:

type(shopping_list['fruits'])
```

### Exercise 2.4
Below are two dictionaries - `subject_data` contains the data for a single subject and `experiment_data` contains the compiled dataset of subjects 1 thru 3. Add subject 4's data to the `experimend_data` dictionary. There are a couple of ways to accomplish this - try to use the most programmatic approach.


```python
# Subject 4's data
subject_data = {
    'subjectID': [4],
    'age': [21],
    'rt': [43.1],
    'condition': [2]
}

# Compiled data
experiment_data = {
    'subjectID': [1, 2, 3],
    'age': [23, 25, 20],
    'rt': [34.44, 24.2, 55.3],
    'condition': [1, 2, 1]
}


# Add sub 4's data to the compiled dataset dictionary:



```

## Control flows

You may want to branch your code so it performs different operations given the truth values of other expressions. To do so you can use an if-else statement. The syntax follows:


```python
if expression:
    # Do something
elif expression:
    # Do something else
else expression:
    # Do something else
```

Note that the `elif` expression is optional, and you can just use a simple `if..else` statement.

For more detailed information, see: https://www.w3schools.com/python/python_conditions.asp

Let's look at a few examples to make this idea more concrete. 


```python
expression = 1 == 1

if expression:
    print('The expression evaluated as true!')
else:
    print('The expression evaluated as :(')
```

    The expression evaluated as true!
    


```python
expression = 1 == 2

if expression:
    print('The expression evaluated as true!')
else:
    print('The expression evaluated as :(')
```

    The expression evaluated as :(
    


```python
list1 = ['apples','pear','orange']

if len(list1[0]) < 1:
    print(list1[0])
else:
    #what do you think the syntax 1: is telling python to do? 
    print(list1[1:])
```

    ['pear', 'orange']
    

## Loops
We will now go over the basic ways to iterate over data types like lists and dicts. If you would like more information, check out this website https://www.w3schools.com/python/python_for_loops.asp

We will focus on two types of loops the `for` loop and the `while` loop. 

### For loop
The for loop will iterate over a list of items (either a list a dictionary or a set). When starting out, you will be using for loops more than while loops (although both do appear). I will provide a few examples of how you can use for loops.

Here's an example to get an idea of the `for` loop syntax:


```python
some_iterable_data = range(0,3)
for variable_name in some_iterable_data:
    print(variable_name)
```

    0
    1
    2
    

You can put whatever label you want for `variable_name`, but the data type in `some_iterable_data` must be a data type that you can iterate over. You will then perform a series of computations with each item you pulled form the object you are iterating over. 

I will provide a few examlpes to make this clearer. This first example uses a list, which is an iterable data type.


```python
list1 = ['a', 2 , [1, 2, 3]]

for item in list1:
    print(item)
```

    a
    2
    [1, 2, 3]
    


```python
#notice how my switching the label item to somethign else, the loop will still compute. 
for some_other_label in list1:
    print(some_other_label)
```

    a
    2
    [1, 2, 3]
    


```python
list1 = ['a', 2 , [1, 2, 3]]

for item in list1:
    if type(item) == list:
        print(item)
```

    [1, 2, 3]
    


```python
list1 = ['a', 2 , 3, 4, 5, [1, 2, 3]]
new_list = []

for item in list1:
    if type(item) == int:
        new_list.append(item)
        
print(new_list)
```

    [2, 3, 4, 5]
    


```python
list1 = ['apple','orange','pear','one', 1, 'two', 2]

for item in list1:
    
    #instead of saying == to see if two variables equal one another, we can say is
    if type(item) is str:
        print('%s is a string' % item)
    elif type(item) is int:
        print('%d is an int' % item)
```

    apple is a string
    orange is a string
    pear is a string
    one is a string
    1 is an int
    two is a string
    2 is an int
    

### While loop
The while loop will continue to run until an expression returns `false`.

The program will continue to execute the code in the block repeatedly until the expression after the `while` statement evalues to False. Here's an example:


```python
count = 0

while count < 100:
    count = count + 10
    print('Count is now at %d' % count)
```

    Count is now at 10
    Count is now at 20
    Count is now at 30
    Count is now at 40
    Count is now at 50
    Count is now at 60
    Count is now at 70
    Count is now at 80
    Count is now at 90
    Count is now at 100
    

## Functions

We use the `def` statement to define a function. For example, the function `concatenate` below takes two arguments `string1` and `string2` and will return a concatenated string separated by a space. Note that the `return` statement specifies the output of the function:


```python
def concatenate(string1, string2):
    return string1 + ' ' + string2
```


```python
concatenate('Hello,', 'Class!')
```




    'Hello, Class!'



What happens if we pass more than two arguments?


```python
concatenate('Hello,','it''s','me...')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\AppData\Local\Temp/ipykernel_9324/1758432633.py in <module>
    ----> 1 concatenate('Hello,','it''s','me...')
    

    TypeError: concatenate() takes 2 positional arguments but 3 were given


### Exercise 2.5
Let's create a more robust concatenate function that handles a variable number of strings. This function should accept **one list argument**, where the list can contain any number of strings. Hint - `for` loops and `len()`:


```python
# This is the test input argumetn:
test_argument = ['Try','to','concatenate','this','list','of','strings']

```

## Object Oriented Programming

Python implements a style of coding called Object Oriented Programming. In a nutshell, Python allows you to create **classes**, which are structures that contain **methods** and **attributes**. Methods and attributes are like functions and variables that are associated with the class.

Let's look at an example defining a `class`:


```python
class Dog:
    
    # Class Attribute
    species = "Canis familiaris"
     
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age
        
    # Instance Method
    def bark(self):
        return 'woof'
     
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def introduce(self):
        return f"My name is {self.name}. I am {self.age}. I am a {self.species}. Nice to meet you!"
```

In order to do anything with the class, we need to **instantiate an object** of the class like so:


```python
# Instantiate a Dog object
molly = Dog('Molly', 13)
```

You have instantiated `molly`, an object of the `Dog` class, whose name is 'Molly' and age is 13.

You can call methods and modify attributes using **dot notation**. You're already familiar with dot notation from using them with lists. Lists are a built-in Python class, and `append()`, `pop()` etc. are just different methods of the List class!

You can call one of `molly`'s methods:


```python
molly.introduce()
```




    'My name is Molly. I am 13. I am a Canis familiaris. Nice to meet you!'




```python
molly.speak('bow wow')
```




    'Molly says bow wow'



You can update the attributes of `molly`:


```python
# Change Molly's age from 13 to 14:
molly.age = 14

# Change Molly's species:
molly.species = 'Good Girl'

# Introduce Molly:
molly.introduce()
```




    'My name is Molly. I am 14. I am a Good Girl. Nice to meet you!'



OOP is widely used when you're programming with PsychoPy (in fact, all the components in the GUI are classes!).

If you would like to learn more about object-oriented programming, check out this tutorial: https://realpython.com/python3-object-oriented-programming/

## Intro to the PsychoPy GUI
If we're just going to be using the PsychoPy GUI, what's the point of learning Python?
1. Unless you're planning to run an *extremely* simple experiment, you'll likely include code chunks in your experiment
2. The GUI is a graphical implementation of Python programming. I will introduce some of the GUI elements and discuss how they relate to some of the programming concepts that we covered.

#### Loops and Classes:

![fig1-2.svg](attachment:fig1-2.svg)

#### Accessing Object Properties, Flow Control:

![fig2.svg](attachment:fig2.svg)

Next week, we will start using the PsychoPy GUI and exploring some experiment demos.
