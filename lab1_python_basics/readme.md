## Psych 186C W1: Python Basics 

In this worksheet you will learn some of the basics of programming in the Python programming langauge. 

We will cover:
- Python syntax such as indentation, defining variables, and how to comment your code
- Basic data types like strings, ints, bools, floats, doubles, lists, and dicts
- Control flows (aka if-else branching)
- The for loop and while loop

The homework problems will require you bring together the concepts you learned in the Python Basics section of the worksheet. Please consult the How To Submit Homework Document on CCLE. 


## Python syntax

Python syntax refers to how the code is written. To start we will cover 3 basic components to Python's syntax

### Indentation (Significant Spacing)
Unlike other programming langauges, how you choose to indent your code is very important in Python. This is because indents tell the Python interpreter which chunks of code should be ran together before moving onto the next part of the program. For those familiar with other programming langauges, indentation replaces the function of the curly brackets in other languages like Java `{ }`.

If you fail to indent things properly, you may get a syntax error. For instance, consider the block of code below, which will print the statement `"Yes, 1 is greater than 0"` if the expression `1 > 0` returns `true`. Note the indent following the new line. 


```python
if 1 > 0:
    print('Yes, 1 is greater than 0')
```

    Yes, 1 is greater than 0
    

By indenting, we indicate the two seperate code blocks needing to be executing: (1) evaluating the expression `1 > 0` and (2) printing the string `'Yes, 1 is greater than 0'`. In general, indentation signfies each individual code block (i.e., a set of commands that should be executed *together* before moving onto the next part of the program).

Whenever we type a `:` in Python, the interpreter will expect that you indent the next line of code. Notice, what happens if I fail to indent the second line of code, an error is returned.


```python
if 1 > 0:    
print('Yes, 1 is greater than 0')
```

    Yes, 1 is greater than 0
    This will cause an error
    

In the remainder of the tutorial, I will make note of when you should indent your code and by the end of this tutorial, indentation will feel very natural and intuitive. However, if you still feel like you need more information on indentation, check out this great resource: https://docs.python.org/2.0/ref/indentation.html

### Exercise 1
Fix the code in this block so it prints the string `'I\'m feeling pretty good today!'`


```python
mood = 'happy'

if mood == 'happy':
    print("I\\'m feeling pretty good today!")
```

    I\'m feeling pretty good today!
    

### Exercise 2

For the following 3 code blocks, try to predict (before executing it) if the code will produce an error. If it does, fix the code so it doesn't produce an error. 


```python
"""
make sure the output of this block reads 
2
is
greater
than
1
"""
if 2 > 1: 
print('2')
    print('is')
     print('greater')
    print('than')
    print('1')
```

    2
    is
    greater
    than
    1
    


```python
#make sure the output of this block reads 2 is greater than 1
if 2 > 1:
    print("2 is greater than 1")
else:
    print("2 is NOT greater than 1")
```

    2 is greater than 1
    


```python
#make sure the output of this block reads 2 is greater than 1
if 1 > 2:
    print("1 is greater than 2")
    else:
        print("2 is greater than 1")
```


      File "C:\Users\huang\AppData\Local\Temp/ipykernel_28484/2019678454.py", line 4
        else:
        ^
    SyntaxError: invalid syntax
    


## Defining variables
We oftentimes what to define variables which can be used multiple times in our program. An example of a variable can be seen in the indentation example where I define a variable named `mood` to the string `happy`. I did this by typing out `mood = 'happy'`. In the code block below I create 5 variables of different data types (more about data types below) and then print the values of those variables out. Notice how I call the variable name in the print function, but the value that the variable is assigned is what's printed.


```python
name = 'Max'
age_human_years = 4
age_dog_years = age_human_years * 7
color = 'white'
personality = 'constantly sad'

#don't worry too much about this print statement yet
print(f'I have a dog named %s who is %d year(s) old in human years and %d year(s) old in dog years. %s is a %s dog with a %s personality.' %
     (name, age_human_years, age_dog_years, name, color, personality))
```

    I have a dog named Max who is 4 year(s) old in human years and 28 year(s) old in dog years. Max is a white dog with a constantly sad personality.
    asd
    

### Exercise 3 
Now add your own values to the variable names and print the resulting statement. Notice how `age_dog_years` doesn't need to be explictly defined by you. This is because the value is determined from the number you assign `age_human_years`.


```python
name = '' #make sure the value is wrapped in quotes. e.g., type 'bingo' not bingo
age_human_years =  #make sure you don't wrap the number in quotes. e.g., type 3 not '3'
age_dog_years = age_human_years * 7
color = '' #make sure the value is wrapped in quotes
personality = '' #make sure the value is wrapped in quotes

#don't worry too much about this print statement yet
print(f'I have a dog named %s who is %d year(s) old in human years and %d year(s) old in dog years. %s is a %s dog with a %s personality' %
     (name, age_human_years, age_dog_years, name, color, personality ))
```

You have a lot of flexibility in what you choose to name your variables. However there are some restrictions. 
For instance, invalid variable names have spaces and lead with number. See the examples below. 


```python
2name = 'some string'
```


      File "<ipython-input-126-84c680502a47>", line 1
        2name = 'some string'
            ^
    SyntaxError: invalid syntax
    



```python
#numbers are okay, you just can't lead with them
name2 = 'some string'
print(name2)
```

    some string
    


```python
#no special characters like *, !, @, #, ect
string* = 'some string'
```


      File "<ipython-input-128-30f13b2276ce>", line 2
        string* = 'some string'
                ^
    SyntaxError: invalid syntax
    



```python
string! = 'some string'
```


      File "<ipython-input-129-0a5466776445>", line 1
        string! = 'some string'
              ^
    SyntaxError: invalid syntax
    



```python
string@ = 'some string'
```


      File "<ipython-input-130-7d746d2130b0>", line 1
        string@ = 'some string'
                ^
    SyntaxError: invalid syntax
    


### Comments
It is good practice to comment your code. Commenting means that you provide a verbal description of what you are having your program do. If you are interested in learning how to be an effective code commenter, check out this website: https://www.elegantthemes.com/blog/wordpress/how-to-comment-your-code-like-a-pro-best-practices-and-good-habits

There are two ways to comment your code:
- With the pound sign `#`
- Between a pair triple quotes `''' '''`

When you use these symbols, you tell the python interpreter to ignore whatever follows


```python
#This is a comment using the pound sign. Note that you can only comment out one line of text
```


```python
"""
This is a multi-line comment. 
You can write more lengthy descriptions in this
type of comment.
"""
```

## Basic data types

In this section I will go over the basic data types in Python and how you use them. 

The basic data types are: 
- strings (more info: https://www.w3schools.com/python/python_strings.asp)
- ints (more info: https://www.tutorialspoint.com/python/python_numbers.htm)
- booleans (or 'bools') (more info: https://www.w3schools.com/python/python_booleans.asp)
- floats and doubles 
- lists (more info: https://www.w3schools.com/python/python_lists.asp)
- and dictionarys (or 'dicts') (more info: https://www.w3schools.com/python/python_dictionaries.asp)

If you would like to go deeper into data types than what I cover here, check out these resources: 
- https://docs.python.org/3/tutorial/datastructures.html
- http://www.math.wsu.edu/math/kcooper/M300/pythontypes.php#:~:text=These%20are%20almost%20the%20same,and%20hence%20is%20slightly%20different.

### Strings
You can define a string with either single quote `''` or double quotes `""`. A string variable will then represent the characters you placed between the quotes. Below are a few examples of strings.


```python
string1 = 'i am a string'
string2 = '2352&(#)'
string3 = "35"
notstring = 35
```


```python
#We can check if these variables are strings by using the `type()` function. 
type(string1)
```




    str




```python
#We can test if a variable is a string. Output is a boolean (True/False):
type(string2) == str
```




    True




```python
#Another way to test if a variable is a string. Output is a boolean (True/False):
isinstance(string3,str)
```




    True




```python
#We can include boolean statements in if statements:
if isinstance(notstring,str):
    print("This variable is a string")
else:
    print("This variable is not a string")
```

    This variable is not a string
    


```python
#you can find the length of a string by using the following function. note that len will report the number of 
#characters in the string
len(string1)
```




    13



### Integers
Integers are the most basic type of numeric representation in Python. Below are a few examples of integers (or 'ints')


```python
int1 = 3
int2 = 243242
int3 = 300
```


```python
#check if variable int2 is an integer
type(int2)
```




    int



You can do mathematical operation on integers:


```python
3 + 3
```




    6




```python
3 - 2
```




    1




```python
#Divison with a backslash
3/2
```




    1.5




```python
#multplication is performed using a *
123*3
```




    369




```python
#take exponents using **
3**2
```




    9




```python
#greater than is with a > 
3 > 2
```




    True




```python
#less than is with a <
3 < 2
```




    False




```python
#greater than and equal to is >=
3 >= 3
```




    True




```python
#less than and equal to is <=
3 <= 3
```




    True




```python
#you can create more complex expression using parens ()

(3 + 2) / 2 ** 2 > (34 * 2)/4
```




    False



### Exercise 4
Can you explain why these two expressions are different? What may be going on?


```python
value1 = 9 / 2

print(value1)
```

    4.5
    


```python
value2 = 10 // 3

print(value2)
```

    3
    

### Exercise 5
The modulus operation is very common in computer programming. Given the examples below, can you figure out what the modulus operation `%` is doing? 


```python
7 % 2
```




    1




```python
8 % 4
```




    0




```python
17 % 5
```




    2



### Booleans
It is oftentimes important to know if an expression is true or false. Booleans (or 'bools') are data types that return either a `True` or `False` value given the truth value of an expression.

I will give a few examples for how you can work with and assign bool values.


```python
bool1 = True

print(bool1)
```

    True
    


```python
bool2 = 3 + 3 < 5

print(bool2)
```

    False
    


```python
bool3 = 17 == 17

print(bool3)
```

    True
    


```python
bool4 = bool3 == bool2

print(bool4)
```

    False
    


```python
s = 'this is a string'
bool5 = type(s) is str
print(bool5)
```

    True
    


```python
i = 6
bool6 = type(i) is int
print(bool6)
```

    True
    

### Difference between `=` and `==`
You may now notice that there is a difference between `=` and `==`. This is confusing to some people at first, because `=` doesn't mean equal in the everday sense of the word. Rather, `=` can only be used to assign variables. If you are wanting to test if two values are equal, use `==`. 


```python
#variable assigment
a = 6
```


```python
#testing for equality
a == 6
```




    True




```python
#you can also use is instead of == to test for equality, although sometimes problems emerge so == is more reliable
a is 6
```




    True



## Floats and doubles
For our present purposes, we wont worry too much about the difference between floats and doubles (if you are interested, read this: https://hackr.io/blog/float-vs-double), but just keep in mind that if you want to represent a number to more precision than just its integer value (i.e., include decimal points), the resulting data type is no longer an `int` but rather a `float` or `double`. See the examples below:


```python
type(3.5)
```




    float




```python
type(9/2)
```




    float



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
    


```python
#you can access a list element by indexing the list as follows. 
#Note that the first element in a python list is indexed as 0
item = list2[1]

print(item)
```

    orange
    


```python
#you can remove an item in a list using the del command
#here, i remove the first element, orange.
del list2[1]
print(list2)
```

    ['apple', 'pear']
    


```python
A = [1, 2, 3, 4, 5]
B = A
```


```python
#you can access a range of elements using the following notation
#here we access the 2nd to 7th elements in a list and assign it to a new list variable
big_list = ['orange','apple','pear','watermelon','cherry','lime','lemon', 3, 6, ['list', 'of','other','things']]
small_list = big_list[2:7]
print(small_list)
```

    ['pear', 'watermelon', 'cherry', 'lime', 'lemon']
    

Often we will want to add items to our list. There are a few ways we can do this


```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)
```

    [1, 2, 3, 4, 5, 6]
    


```python
list1 + [4]
```




    [1, 2, 3, 4]




```python
#notice how we recieve an error if we don't make our int 4 into a list (by wrapping it in [])
list1 + 4
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-82-0b3b4d442676> in <module>
          1 #notice how we recieve an error if we don't make our int 4 into a list (by wrapping it in [])
    ----> 2 list1 + 4
    

    TypeError: can only concatenate list (not "int") to list



```python
# we can also use the append function
list1 = [1, 2, 3]
list2 = [3, 5, 6]

for item in list2:
    list1.append(item)

print(list1)
```

    [1, 2, 3, 3, 5, 6]
    

You can find the length of a list (how many elements are contained in it) by using the `len()` function. This will be very handy very soon!


```python
list1 = [1, 2, 3, 4, 5]
print(len(list1))
```

    5
    


```python
#why do you think the length is 4 and not 6?
list2 = [1, 2, 3, 4, 5, 6]
print(len(list2))
```

    6
    


```python
print(len(list1) < len(list2))
```

    True
    

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
#here is a simple dict.
simple_dict = {
    'key1' : 1, 
    'key2' : 'two',
    'key3' : [3]
}
simple_dict
```




    {'key1': 1, 'key2': 'two', 'key3': [3]}




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
```


```python
shopping_list
```




    {'fruits': ['orange', 'apple', 'pear', 'banana'],
     'soda': ['coke', 'dr. pepper'],
     'vegetables': None,
     'breads': 'Daves Killer Bread'}



### Exercise 6
Define a dictionary containing data that may be generated by an experiment with 3 participants. I will provide an example and then you create an example, try to use different key names (or experimental measures) than the one's I use in the example).


```python
eg_experiment_data = {
    'subjectID': [1, 2, 3],
    'age': [23, 25, 20],
    'rt': [34.44, 24.2, 55.3],
    'condition': [1, 2, 1]
}

experiment_data = {
    
}
```

## Control flows

You may want to branch your code so it performs different operations given the truth values of other expressions. To do so you can use an if-else statement. The syntax follows: 

`if` _expression_ : \
$\;\;\;\;\;\;$ do something

`elif` _expression_ : \
$\;\;\;\;\;\;$ do something else

`else` : \
$\;\;\;\;\;\;$ do something else

Note that the `elif` expression is optional, and if you only want a simple if-else statement you can drop it as follows: 

`if` _expression_ : \
$\;\;\;\;\;\;$ do something

`else` : \
$\;\;\;\;\;\;$ do something else


For more detailed information, see: https://www.w3schools.com/python/python_conditions.asp

Let's look at a few examples to make this idea more concrete. 


```python
expression = 1 == 1

if expression:
    print(expression)
else:
    print(expression)
```

    True
    


```python
expression = 1 == 2

if expression:
    print(expression)
else:
    print(expression)
```

    False
    


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

The syntax for defining a for loop is

`for` _item_ in _variable_ : \
$\;\;\;\;\;\;$ do something


You can put whatever label you want for _item_ , but the data type in _variable_ must be a data type that you can iterate over. You will then perform a series of computations with each item you pulled form the object you are iterating over. 

I will provide a few examlpes to make this clearer.


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

`while` _someExpression_ : \
$\;\;\;\;\;\;$ _do something_

The program will continue to execute the code in the _do something_ block until the expression evalues to False (that is, as long as _someExpression_ evaluates as `True`, the program wont leave the loop)


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
    
