Advanced Linux User!
# Some advanced user commands
```shell
sudo passwd username  -- tochange password
sudo usermod -u new_id username --to change id
sudo userdel -r username  -- to delete user

```
## Sudowers file
- It is a file linux and Unix administrator use to allocate system right to system users
- The user u created does not have a sudo power like the original  
- To access the sudowers file 
```shell
sudo visudo
```

## Linux Power permission 

There is a 5 main parts on the listing :
	- Permission
	- Owners
	- Data
	- Size
	- Filename
#### Ownership
It have two kinds 
	- user 
	- Group 
To change the owner of a file:
```shell
chown user:group filename
```
#### Permission
There are 3 types of permissions
	- Read(r)
	- Write(w)
	- Execute(x)
This part also have three parts 
- user-group-other
1. User(u) = power of the user defined on the ownership
2. Group(g) = Power of group defined on the  ownership
3. Other(o) =  Power of other users
4. All(a) = power of all which can be found in the 3 above 

### CHMOD command
This command helps to change file permission
Each of the permission have a number representation:
	Read -  4-r
	Write - 2 -w
	Execute - 1-x
The syntax is :
```shell
chmod <parameter> filename
```
● The parameter can be in numbers and symbols
A) Parameters in symbol
-  chmod a+x filename -> adding execute permission for all ( chmod +x filename)
-  chmod u+x filename -> adding execute permission for user
-  chmod g+x filename -> adding execute permission for group
-  chmod o+x filename -> adding execute permission for other
-  chmod -x filename -> removing execute permission for all
-  chmod a+rwx , u-rw , g-x , o-xw filename -> gives rwx for all and removes something from all
B) Parameters in Number
● chmod 621 filename -> 6 for user, 2 for group, 1 for other ( 6 = 4+2 ), 6 =r w
● chmod 777 filename -> 7 for users, 7 for group , 7 for others (7 =4+2+1), 7 = rwx
# Package Installation On linux
You can use :
	- apt, pacman, pkg
	-If you are using Debian package manager there is 'dpkg'
## Repository
It is the site/server kali uses to upload the packages
# Advanced package tool/apt
syntax:
```shell
sudo apt update
sudo apt search <softwarename>
sudo apt install <softwarename>
sudo apt remove <softwarename>
sudo apt upgrade
sudo apt purge <softwarename>
```
# Package Dependencies
There is a 'module' this are a programs that another program will be built on .
So a program to work properly the dependencies have to be installed
# Dpkg /Debian Package Manager /
- It is an offline program
- The packages have an extensions ".deb"
syntax:
```shell
sudo dpkg -i <packagename>
sudo dpkg -r <packagename>
sudo dpkg -p <packagename>
```
[[Day6_FinalLinux.md]]














