# Regular expressions!/regex/
- they are patterns that helps to filter so text, space, tabs & symbols.
- Regex is pattern.
- Regex are used on linux tool called grep, awk and sed
```python 
import re
a = re.search("patern","searching File").group(0)
print(a)
```
## Metacharacters
. ----------used to get all the lines except newline
^something---------(assertion )t will search for statement that starts with the word you gave it
something$----------(assertion)it will find for statement that ends with the word you give it

[*]------ used to the last letter u gave it if it occurs 0 or more times (quantity)*
+-------(quantity) it used to get a pattern that occurs 1 and more times
     example: syntax -hellos+                      ---- result will be a text hello that have s at least one times and more 
?--------(quantity)used to get line that occurs 0 and 1 times
{ } -------(quantity) {min, max}

[ ]----(custom pattern)used to create your own pattern example[a-z] -searches for something that have a-z letter
( )
| used to search 2 different things    (t|n---it will search for t or n)
\\------ (Escape)  used to search symbols that are metacharacters 
   example \\. like this  it will search for .
           \\w  ----used to get all text except new lines
           \\W ---used to get all except alphanumeric
           \\n ---used to select new line
           \\s ---used to select space
           \\S---used to select all except spaces
           \\d --- select digit/number
           \\D----select all except digit/number
## Bash regex
we can use it on awk, sed, grep
for kali use:
```kali
grep -Eo "your pattern"
grep "^.*@.*\.(com|org|net)\$"
```
for bash we can use =~ operator for regex
here we use double bracket
```shell
read -p "Enter your number: " num
pattern="[0-9]"
if [[$num =~ ${pattern}]]
then 
echo "your input is number!"
else
echo "plese enter a number only!"
fi

```

# Bash else if
```shell
if condition
then 
body
elif condition
then
body
else
body
fi
```
## Loops

1. For loop
for condition
do 
body
done
example: 
```shell
for num in {1..10}
do
echo $num
done
```
for loop with 3 expressins
example:
```shell
for ((start; end; increment))
do
echo $
done

for ((i=1; i<=10; i++))
do
echo $i
done


for num in {1..10..-1}
do
echo $num
done
```

 ## While loop
 ```shell
while [expression]
do
body
done

read -p "Enter a number to start with: " snum
read -p "Enter an= number to end with: " enum 

while [[$snum -le $enum]]
do 
echo $num 
((snum++))
done
```

[[Day12_network.md]]
