Core of python Programming
# Indaxing 
The list index starts with 0.
* Negative indexing = > in this case the last value of the list is -1 and the one that is before the last one is -2 and so on
# Slicing
- We can access a bunch of values  from list or string by using the slicing operator ":" .
- syntax:
```python
list_name[starting:stoping:steping]

name="Mrinel Kings"
print(name[3:6:1]) # result: nel
print(name[3:-6]) # nel
print(name[7:]) #kings
print(name[::]) #Mrinel kings
```
- Python's default step is 1
- python's default stop is the last item.

# User Input Handling
There are two types of input 
1. By input function
2. By Arguments
## Input Functions
syntax: 
```python
var=input("text")
```
We can change the input type into int(), float(), str()....
```python
var=int(input('num'))
var=float(input('num'))
var=str(input('name')) 
```
## Arguments
It helps us to get input from the command line.
```python
import sys
name = sys.argv[1]
print(f"hello {name}")
```
# Operators
- They are special symbols that perform operation on variables and values.
- These are :
	- Arithmetic operators
			addition
			subtraction
			Multiplication
			Division
			Modulus
			Power  (a ** b)
	- Assignment Operators
			Assignment  (a = c)
			Addition  (a += b  / a = a + b)
			Subtraction (a = a - 2 / a -= 2)
			Multiplication  (a = a * 2 / a * = 2)
			Division  (a = a / 2 or a /= 2)
			Remainder ( a = a % 2  / a %= 2)
			Exponent (a = a ** 10  /  a **= 10)
	- Comparison Operators
			Is equal to
			Not equal to
			Greater than
			Less than
			Greater than or equal to
			Less than or equal to
	- Logical Operators
			and
			or
			not
	- Special Operators
	- Bitwise Operators
- There is a keyword bin(your_Decimal) => it helps to show the binary value of your decimal.
1. Compliment (not) (~)
This will add one to the number you gave it and then it will make it negative.
```python
print(~12)  # output -13
```
2. And (&)
```python
print(10&7)  #output 2
```
3. OR (|)
Same as And but the logical operator will be changed
```python
print(10|7) #output 15 
```
4. XOR (^)
If the binaries  are the same  =  0  ,  1^1 = 0  or   0^0 = 0
If the binaries are different  = 1 ,  1^0 = 1  or 0^1 = 1
```python
print(10^7)
```
5. Left Shift
It will shift the bits to the left
```python
print (10<<2) #output 40 
```
6. Right Shift
It will shift the bits to the right
```python
print(10>>2) #output  2
```
### Indentations
These are a space which python use for some of its functions.
# If-else conditions
- We use the if statement to run the code if the condition is true.
## If statement
It evaluate the code of it is true.
- Syntax: if condition:
			body
```python
num = 10
if num > 0:
	print("the number is positive")
```
## If else statement
```python
num=-23
if num>0:
	print("the number is positive")
else:
	print("the number is negative")
```
## If elif else statement
We use elif statement if the if statement is not true.
```python 
num=0
if num>0:
	print("the num is positive")
elif num<0:
	Print("the num is negative")
else:
	print("the number is Zero")
```
## Nested if statement 
- If we use if statement in other if statement that statement become nested if statement.
```python
num=3
if num>=0:
	if num=0:
		print("the number is Zero")
	if num>0:
		print("the number is positve")
else:
	print("the number is negative")
```

# Logical error (Exceptions)
They are a run time errors.
- Example:
	- index error
	- Zero division
	- Name error
# Error handling
To handle error we use    try .... except  blocks
Syntax:
	try:
		the code that may cause exception
	except:
		code to run when the exception occurs
```python
try:
	
	num = 10
	numb = 0
	result = num/numb
	print(result)
	
except ZerodivisionError:
	print("Error: Denominator can not be zero.")
try:
	even_number=[2,3,5,74,4]
	print(even_number[5])
except IndexError:
	print("Error: Index out of Bound")
```
# python Loops
- Loops are a program that use to repeat a block of code
- There are two types of loop:
	- For loop
	- While loop
## For loop
syntax: 
	for val in sequence:
		statement
```python
lan=['py','java','css','c++']
for lan in lan:
	print(lan)  # this will print all the values in the list
```
### Range
It is series of  values between two numeric intervals.
```python
for i in range(9):
	print(i)
ha=[1,2,4,5,6,'hafh']
for i in range(len(ha)):
	print(i)  # it will print all the values in ha
```
## While loops
syntax:
while condition:
	body
```python
i=1
n=5
while i<n:
	print(i)
	i+=1
```
- While loop is used when the number of iteration is known. This is what makes it different from for loop(it is used when the number of iteration is known)
- For loops: ends when the iteration is finished.
- While loops: end when the condition is false.
```python 
c_grade = 0
f_grade = 12
while c_grade <= f_grade:
	Print("you have passed grade: ",c_grade)
	c_grade+=1
Print("Congratulation you are now promoted to higher education level!!!")
```
# Break
- It is used to exit an infinite loop.
```python
code = [2343,1342,5656,9387]
error = 0
while True:
	if error <= 5:
		user=int(input(f"please enter the code correctly {code[0]}:\n>>"))
		if user!= int(code[0]):
			print(int[code[0]])
		elif user == int(code[0]);
			print("well done")
			break
	else:
		print(":( Sorry try again next time.")
		break

```

[[Day9_FurtherPy.md]]
