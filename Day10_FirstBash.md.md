# What is Bash Script
- Bash = Bourne Again Shell
- Bash is a shell that used to interact with the kernel
- Script is a file that contains shell commands
- Original SH - BOURNE SHELL
## USES of BASH
- Script development 
- simplifying task
- simplifying linux ability
- developing hacking script 


Bash have the ''.sh'' extention
 ### Displaying output
 - to start every bash script use shebang 
```bash
#! /bin/bash
#! /bin/sh

```
- to display output
```shell
echo "text"
```
- to run your project 
```shell
/bin/bash<file>
./<file>
....
```


#### Variables

same as python
    - no space b/n = 
    - use $before the variable name to use it
    - ${variable name}
    - bash variable is string by default


The [set] command can be used to assign values to positional parameters
```shell
#! /bin/bash

set hachalu ketema shiferaw 

echo $1 $3
#output hachalu ketema 

```
## system Variable
```SHELL

 $BASH
 $BASH_VERSION
 $PWD
 $HOME
 $PATH   AND SO MANY LIKE  LALNG, TERM, MAIL, EDITOR, USER, SHELL
 $USER - prints the user name 
```
### Variable & Data Type

Array
    -  it is list or tuples on python
```shell
var=("list1""list2""list3")
var[index_number]='list' -----add list to the index you give it

echo ${var[0]}
echo ${var[@]} ---displays all the lists
echo ${#var[@]} ---displays the length
echo ${!var[@]} ---displays the index value
var[4]="list" ---add element on the array
unset var[3] ---removes the array at index 3
```

### Bash input
1. Read function
- used to accept input while running the script
```shell
read -p "text to display" var
read -sp 'password' ------------to accept 
read -a  -------------to accept array
```
1. Arguments
Helps to get input before the script starts
```shell
$0-$9 
`````

##### COMMENT
```shell
# asdfadsf aajdklf;adshfas fahdsfhkaerrqadisafbva 
<<COMMENTS
akjldshafewrafdsads
fadshfawe
rfadhsfiaerwqadfbv asf
dsfaeuiwraff

COMMENTS
```
# Bash sleep
```shell
sleep <number>s ----------(second)
```

## Operation
A. Arithmetic Operator
```shell
$((expretion))
```
B. Assignment Operation
```shell
leta+=3
leta-=3
leta*=3
leta/=3
```
C. Comparison operator
```shell
-gt ---------greater_than
-lt ---------less_than
-ge ---------greater_and_equals
-le ---------less_and_equals
-eq ---------equal
-ne ---------not_equal
```
# If Else condition 
if you use [ ] you will use alphabetic operation(-gt,-lt,-eq,-ne,....) 
for ( ( ) ) string u can use sign(><=+-)
```sh
if [condition] or if ((condition))
then
body
else
body
fi
```

[[Day11_proBash.md]]
