import pickledb
from discord.ext import commands
import itertools
import sys
import io
import discord


class t(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    #this gotta be the harest command yet D:
    @commands.command(aliases=['tree', 'familytree', 'gettree'])
    @commands.guild_only()
    async def t(self, ctx, member: discord.Member = None):
        if member == None:
            noFamilyResponse = "You have no family :("
            author = ctx.author
        else:
            author = member
            noFamilyResponse = "They have no family :("
        db = pickledb.load('database.txt', False)

        class Person: #here we set up a class and some functions to generate the tree at the end
            ID = itertools.count()
            def __init__(self, name, parent=None, level=0):
                self.id = next(self.__class__.ID)
                self.parent = parent
                self.name = name
                self.level = level
                self.children = []

        def createTree(d, parent=None, level=0):
            if d:
                member = Person(d['parent'], parent, level)
                level = level + 1
                member.children = [createTree(child, member, level) for child in d['children']]
                return member
        if not db.exists(author.name+"#"+author.discriminator+"partner") and not db.exists(author.name+"#"+author.discriminator+"child"):
            return await ctx.send(noFamilyResponse)
        #so if everything went fine, then start creating the tree
        await ctx.send("Getting data and creating tree...")
        
        partner = db.get(author.name+"#"+author.discriminator+"partner")
        def childrenSort(parent): #this function gets the children of the person in question
            finalChildren = []
            children = db.get(parent+"child").split("|/") #get all the children
            for child in children:
                if child == '': #ghost children idk if it happens now
                    children.remove(child)
            print(children) #debug
            for child in children:
                if child == parent: #geez this shouldn't be a thing...
                    break
                #in the elifs before, four cases lead to four outputs. The cases are the person have partner + children, only partner, only children, or nothing at all
                elif db.exists(child+"partner") and db.exists(child+"child"):
                    familytree = {'parent':child+" + " + partner, 'children':childrenSort(child)}
                elif not db.exists(child+"partner") and db.exists(child+"child"):
                    familytree = {'parent':child, 'children':childrenSort(child)} #we called childrenSort again if the child has more children
                elif db.exists(child+"partner") and not db.exists(child+"child"):
                    familytree = {'parent':child+" + " + partner, 'children':[]}
                else:
                    familytree = {'parent':child, 'children':[]}
                finalChildren.append(familytree) #append the family tree
            print(finalChildren)
            return finalChildren #returns the entire tree
        #more sorting etc...
        if (not db.exists(author.name+"#"+author.discriminator+"child")) and db.exists(author.name+"#"+author.discriminator+"partner"):
            familytree = {'parent':author.name+"#"+author.discriminator+" + " + partner, 'children':[]}
        elif (not db.exists(author.name+"#"+author.discriminator+"partner")) and db.exists(author.name+"#"+author.discriminator+"child"):
            familytree = {'parent':author.name+"#"+author.discriminator, 'children':childrenSort(author.name+"#"+author.discriminator)}
        else:
            
            familytree = {'parent':author.name+"#"+author.discriminator+" + " + partner, 'children':childrenSort(author.name+"#"+author.discriminator)}
        print(familytree)
        #now we can acutally  make the tree
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()
        t = createTree(familytree)
        def printout(parent, indent=0):
            
            
            print('\t'*indent, parent.name)
            for child in parent.children:
                printout(child, indent+1)        
        printout(t)
        sys.stdout = old_stdout # Put the old stream back in place
        whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        await ctx.send("```"+whatWasPrinted+"```") #send the tree
        await ctx.send("Use ms!help to see the format of the tree")
        #GOSH THAT WAS HARD
    
        
def setup(bot):
    bot.add_cog(t(bot))
