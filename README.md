# Securly's Marriage Bot
A discord bot inspired by the acutal Marriage Bot
## About The Bot
Bascically it does fake marriages. It is also very fun lol.

## Commands

----------   
Use ms!help to see everything listed below   
*Each command has aliases. Each of them has an alias for the full word: ms!ad = ms!adopt. You can find all of the aliases in each command's file*   
   
**COMMANDS**      
ms!ad {user} - adopt someone     
ms!m {user} - marry (propose to someone) *partner = the person you married*    
ms!d - remove your partner ~~with utter force~~     
ms!do {child} - remove that child ~~via throwing out the door~~      
ms!c - removes your entire family     
ms!e - remove your parent ~~by running away~~     
**ms!t {user} - show user's family tree or your own is user is blank**     
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
For replit, use the button below (see below on how to keep the bot running)     
     
[![Run on Repl.it](https://repl.it/badge/github/oliver408i/Securly-Marriage-Bot)](https://repl.it/github/oliver408i/Securly-Marriage-Bot)
    
*NOTE: you will still have to manually add the bot token! See settings.py for more info*   

Keeping the bot running with replit hosting:
1. Go to uptimerobot.com
2. Sign up or sign in
3. Start the bot
4. Add a monitor with the url in the web view
    
For self-hosting, see instructions below:   
*Made with Python 3.8.12, but 3.9 should work*
1. If you have git, you can do `git clone https://github.com/oliver408i/Securly-Marriage-Bot` and then use `cd Securly-Marriage-Bot` to navigate into the new directory. If you don't have git, you will have manually download the code, unzip it, and then cd into it    
2. Add your bot token: you can find info on how to do this in settings.py
3. [sometimes required] Do `python3 -m poetry install` if you don't have the packages installed
4. Do `python3 main.py -noWebServer`
5. If you shall want a web server for keepalive (see the replit section), remove the `-noWebServer` flag
## The code and stuff
The entire code is commented so you can easily add stuff. See main.py for more info on the comments. Feel free to contact me at `NitrogenDioxide#2553`!

## Credit
Python modules used:   
- [PickleDB](https://patx.github.io/pickledb/) for database writing and reading
- [Discord.py](https://discordpy.readthedocs.io/en/latest/) for... you know....

Code from others:  
    
Thanks to random stackoverflow topics for help on code       
Thanks to [this post](https://stackoverflow.com/questions/13671119/how-to-create-family-tree) for part of the family tree generator