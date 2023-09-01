# FUNCTION

- function is a block of code that performs a specific task. 
$$ DRY$$Types of function 
1. [Standard library function ] 
2. [User-defined function]

syntax:
```python

def function_name(arguments):
#to call a function
function_name()
```
## Return statement 
Python function use the [return] statement to return some value.

for instance: 
```python 
def add(num1, num1)
	return num1 + num2
print(add(2,9))
#output  11
```
### Recursion

 - it is a process of defining something in terms of itself.
### Anonymous / lambda Function 
- If a function does not have a name it is called [lambda function].
- We use them to return one line code.
```python 
name lambda argument: expression
name lambda : print("Hello world!")
number lambda a, b : a + b
print(number (1,2))
#output  3
```
We don't use a return function in this case.

# Function taker Function
[filter], [map]& [reduce] are the function that take another function.

[filter] :- are used to filter or search some function from a sequence.
```python

filter(function or none )

nums = [22,34,5,2,1,72,45]
even = list(filter(lambda n: n% 2 ==0, nums))
prit(even)
# output [22,2,72]
```
 [map] :- it runs some operation on a given function.
 example 
 ```python
num = [2,7,3,6]
doubles = list(map(lambda n: n*2,num))
print(doubles)
#output [4,14,6,12]
```
## Append
 used to add some value to a list.
 ```python
my_listname.append(new_value)

a = []
c = 3
a.append(c)
print(a)
#output [3]
```

# [[Object-Oriented Programing /OOP]]
python is an OOP language.
so what is object?
    - it is anything which have action and name
    - they have attribute(properties) and method(action or function)

## Python class and object
- class is a place where we create our Object's attribute and behavior in blueprint
- class is a blue print for that object.
```python 
#to creat a blueprint (attribute)for an object
class class_name:
	class1 = ""
	class2 = ""
	class3 = ""
	def  function_name(self):
		return "something "
#to create an object
 object_name1 = class_name()
 object_name1.class1 = "something"
 object_name1.class2 = "something"
 object_name1.class3 = "something"
#creating another object
 object_name2 = class_name()
 object_name2.class1 = "something"
 object_name2.class2 = "something"
 object_name2.class3 = "something"
 ................
 print(class_name.function_name(object_name))
```
__________
### Python Constructors
- we can also initialize a value using a constructors
```python
__init__( )#is a constructor function that is called when ever a new object of the class is initialized
#example

class human:
	def __init__(self,name,age,work):
		self.name = name
		self.age = age 
		self.work = work
JSimpson =human("Simpson",23,"Business man" ) 
print(f"JSimpson's name is called: {JSimpson.name}\nHe is {JSimpson.age} years old\nHis work is {JSimpson.work}")

```   
## Python Inheritance
- is a way of creating new class with some properties of existing
```python
class robot:
	def move (self):
		print('I can move here and there!')
	def jump (self);
		print('I can jump!')
class RCrobot(robot):
	def run(self):
		print('I can run very fast!')

robot1 = RCrobot()
robot1.move()
robot1.jump()
robot1.run()
```
## Python Encapsulation

It refers to bundling of attribute and method inside a single class

```python 
class computer:
	def __init__(self, name):
		self.name = name
	def setname(self,name):
		self.name = name
chuk_computer = computer("Alien Ware")
print(f"chuk_computer name is: {chuk_computer.name}!")

chuk_computer.setname ("Preditor")

print(f"chuk_computer name is: {chuk_computer.name}!")

```

####  Package installation 
 ```python
 #on terminal
 pip install pakagename
```


[[Day10_FirstBash.md]]
