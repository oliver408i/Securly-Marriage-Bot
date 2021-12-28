# Securly's Marriage Bot
A bot inspired by the acutal Marriage Bot
## About The Bot
Bascically it does fake marriages. It is also very fun lol.

## Commands
Use ms!help to see everything listed below   
*Each command has aliases. Each of them has an alias for the full word: ms!ad = ms!adopt. You can find all of the aliases in each command's file*
----------   
**COMMANDS**      
ms!ad <user> - adopt someone     
ms!m <user> - marry (propose to someone) *partner = the person you married*    
ms!d - remove your partner ~~with utter force~~     
ms!do <child> - remove that child ~~via throwing out the door~~      
ms!c - removes your entire family     
ms!e - remove your parent ~~by running away~~     
**ms!t - show your family tree**     
Family tree format is:      
```
Parent + Partner
    child1  
    child2   
        child of child2    
            ...and so on
```
----------

## Setup
For replit, use the button below (bot does not keep it self running. You will need to enable always on)     
     
[![Run on Repl.it](https://repl.it/badge/github/oliver408i/Securly-Marriage-Bot)](https://repl.it/github/oliver408i/Securly-Marriage-Bot)
    
*NOTE: you will still have to manually add the bot token! See settings.py for more info*
    
For self-hosting, see instructions below
1. If you have git, you can do `git clone https://github.com/oliver408i/Securly-Marriage-Bot` and then use `cd Securly-Marriage-Bot` to navigate into the new directory. If you don't have git, you will have manually download the code, unzip it, and then cd into it    
2. Add your bot token: you can find info on how to do this in settings.py
3. Do `python Bot.py`. It should automatically install packages, if it doesn't, do `pip install -r requirements.txt` or `pip3 install -r requirements.txt` if you have pip3
## The code and stuff
The entire code is commented so you can easily add stuff. See Bot.py for more info on the comments. Feel free to contact me at `NitrogenDioxide#2553`!

## Credit
Python modules used:   
- [PickleDB](https://patx.github.io/pickledb/) for database writing and reading
- [Dicsord.py](https://discordpy.readthedocs.io/en/latest/) for... you know....
- sys, io, itertools, etc.

Code from others:  
    
Thanks to random stackoverflow topics for help on code       
Thanks to [this post](https://stackoverflow.com/questions/13671119/how-to-create-family-tree) for part of the family tree generator