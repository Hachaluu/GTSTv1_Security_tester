Further on Linux
# Linux file Hierarchy
It has a special file system than windows 
	File system is a directory that the OS uses
- ^Windows -- system file appears under the local disk c : 
- ^Linux ---system file occurs under the root directory (/)
## File structure in detail 
1. / (root)
		- every single file from this 
		- the root user only can write under this 
		- /root is the root user's home directory which is not same as /
2. bin (binary executable)
Essential command binaries that need to be available in single-user mode; for all users
3. /boot (boot loader file)
- kernel initrd, vmlinux, grub files are located unde /boot
4. /dev (essential device file)
- include terminal devices, usb, or any device attached to the system
5. /etc (etcetera)
- contains configuration files 
- startup, shutdown shell script used to start/ stop/ 
6. /home (home directory)
home directory for all users to store their personal files
7. /lib (libraries essential for the binaries in /bin & /sbin)
- lib names are either id or lib
8. /media (Mount points for removable media such as CD-ROMs)
- it is temporary
9. /mnt (Temporary mounted file)
Temporary mount dir where sysadmins can mount filesystems
10. /opt (Optional application software packages)
- contain add on app from individual vendors
11. /sbin (Essential system binaries)
- contain binary executable 
- the commands mainly used by system admin for sys maintenance purpose
```shell
sudo adduser user_name
```
12. /tmp (tempo files)
- when the system is rebooted the file under this will be deleted
13. /usr (user Utilities)
- Contains binaries, libraries, documentation, and source-code for second level programs
- /usr/lib contain libraries /usr/bin and /usr/sbin
- [+] /usr/src holds the LINUX KERNEL SOURCES, HEADER-FILES and DOCUMENTATION
### Text Editors
- it is a program used for text editing 
- example of linux line text editors :
		-[+] vim                    
		-[+] Nano
		-[+] Emacs
		-[+] Neovim
- examples of linux Graphical Text editors
		-[+] Sublime
		-[+] Vscode
		-[+] Gedit
		-[+] Pluma
# [[VIM]]
- At first vi was the primary editor on linux which lets users to see/edit only one text at a time
- Then vi improved and develop VIM
- It has two modes mainly
		- Command mode
		- Input mode
- it is default on command line when you open it.
- to get insert mode type ' i ' to get back to comment click 'Esc'
```vim
to save  :w + enter_key
to quit  :q = enter_key
to force_quit  w:q! + enter_key
to undo  :undo + enter_key
Execute commands :%!yourcommand

```
# [[NANO]]
- It is a friendly free and open source text editor 
- It comes pre installed in modern linux system
```shell
nano file_name
then state_typing
Ctrl+s --save
Ctrl+x --exit
Alt+E  --redo
Alt+U  --undo
Ctrl+shift+c --copy
Ctrl+shift+X --cut
Ctrl+shift+v --past
```

# Linux User Management
- to know our name on linux type "whoami"
- there are two users on the linux
		- Root id=0
		- Normal user id stat with 1-999
## Creating users
use this to create user
```shell
useradd --simple
sudo useradd user_name
adduser --detailed
sudo adduser user_name
```
- [+] The user files are stored inside on /etc/passwd
- [+] The User password are stored on /etc/shadow

[[Day5_LinuxRUN.md]]
