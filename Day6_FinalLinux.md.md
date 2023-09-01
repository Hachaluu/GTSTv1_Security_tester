# Finishing for linuc
# Script installation
We can download a hacking tool from fit hub, for this pupose git have a feature called clone.
Syntax:
```shell
git clone <link_of _the _script_from_github>
```
Script languages: 
		python
		bash
		go
		ruby
If we want to use this programs we need to install their modules/dependencies
For example :
	1. python:    pip install modulename       for the requirement we use = pip install -r requirement.txt
	2. Go : go install  modulename
	3. Ruby : gem install modulename

## Python Installation 
If pip is not found 
```shell
pip install term
```
If the package exists 
```shell
pip install -r requirement.txt
```

## Go package Installation 
1. Old version 
```shell
go get github.com:capotej/groupcache-db-experiment.git
```
2. New version 
  A. Downloading the package 
```shell
go get github.com/lc/gau/v2/cmdgau@latest
```
  B. Moving the file to /usr/bin/
```shell
sudo mv filename_/usr/bin
```
## Errors you may encounter 
● Don’t close apt while installation
● Repository errors, if this happened you can fix it using
```shell
 sudo apt edit-sources
```

# Help on linix about the commands 
use:
1. man (manual)
2. -h
3. -help
4. - -help

## Linux Processes & Services
to get access to the process :
	option - A == it will view all the running process 
				-u username == view users process 
```shell
ps [options]

```
PID -process ID
- [ ] to stop the process 
	option - kill -19 PID  (to stop the process)
				- kill -18 PID (to resume the process)
				- kill -9 PID (to stop the process immediately)
```shell
kill [option]
```

For this process 
we can use a tool called "top" installed by default 
But we can also use "htop" cus it is more colorful

# Foreground / background
● Thus far, we have run commands at the prompt and waited for them to complete. We call this running in the “foreground.”
● Use the “&” operator, to run programs in the “background” or press ^Z
to get background process to foreground
  - Fg 
to stop a process inside ur shell press ^C

# Null device
● /dev/null - Redirects output to nowhere.
● If you want to ignore output, you can send it to the null device, /dev/null. 
● The null device is a special file that throws away whatever is fed to it. 
● On shell output there are 2 things.
○ STDERR = 2
○ STDOUT = 1
● To redirect the errors from a command result we do 
```shell

command 2> filename => here if you check the file you saved on it have errors only
```
● To redirect the error-FREE output
```shell
 command 1>filename
```
● So if we redirect our commands output to /dev/null we will get error free result
```shell
command 2> /dev/null
```
## Alias 
- It is used to name some commands
```shell
alias name='command_you_want_to_change_to_the_name'
```
- It is temporary (it will work only when the terminal is open)
- But if you want it to work you have to add it to your shell config file
Example for bash and fish, zsh...
```shell
Bash=~/.bashrc
Zsh=~/.zshrc
Fish=~/.config/fish/config.fish
```

# Tmux  (terminal multiplayer)
- Used to classify our terminal work
- To start it 'tmux'\
- To Create config file type
	- nano .tmux.conf
	-  Type this
■ unbind C-b
■ unbind l
■ set -g prefix C-a
■ unbind %
■ bind e split-window -h
■ bind o split-window -v
■ set -g base-index 1
■ setw -g pane-base-index 1
* Save it | exit tmux and open again

● To split horizontally 
	^A then o
● To split vertically 
	 ^A then e
● To exit 
	 ^A then x or 
	  just type ‘exit’
● To create tab 
	 ^A then c
● To rename the tab 
	 ^A then ,(comma)
● To switch tabs
	 ^A then (numbers)
- TO switch partitions 
	  ^A then (arrow)

# Wget
It is used to download files from website/servers
```shell
wget [option][link]
```
# Find
Used to search files/videos/music
```shell
find [search path] [option] [searchword]
```
More commands 
```shell
find/ -name"linux"
find/home-perm777
find-typef | find -type d
```

[[Day7_HelloPython.md]]

