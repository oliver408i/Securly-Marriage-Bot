import pickledb
from discord.ext import commands
import itertools
import sys
import io
import discord


class t(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['tree', 'familytree', 'gettree'])
    @commands.guild_only()
    async def t(self, ctx, member: discord.Member = None):
        if member == None:
            author = ctx.author
        else:
            author = member
        db = pickledb.load('database.txt', False)

        class Person:
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
            return await ctx.send("You have no family :(")
        await ctx.send("Getting data and creating tree...")
        
        partner = db.get(author.name+"#"+author.discriminator+"partner")
        def childrenSort(parent):
            finalChildren = []
            children = db.get(parent+"child").split("|/")
            for child in children:
                if child == '':
                    children.remove(child)
            print(children)
            for child in children:
                if child == parent:
                    break
                elif db.exists(child+"partner") and db.exists(child+"child"):
                    familytree = {'parent':child+" + " + partner, 'children':childrenSort(child)}
                elif not db.exists(child+"partner") and db.exists(child+"child"):
                    familytree = {'parent':child, 'children':childrenSort(child)}
                elif db.exists(child+"partner") and not db.exists(child+"child"):
                    familytree = {'parent':child+" + " + partner, 'children':[]}
                else:
                    familytree = {'parent':child, 'children':[]}
                finalChildren.append(familytree)
            print(finalChildren)
            return finalChildren
        if (not db.exists(author.name+"#"+author.discriminator+"child")) and db.exists(author.name+"#"+author.discriminator+"partner"):
            familytree = {'parent':author.name+"#"+author.discriminator+" + " + partner, 'children':[]}
        elif (not db.exists(author.name+"#"+author.discriminator+"partner")) and db.exists(author.name+"#"+author.discriminator+"child"):
            familytree = {'parent':author.name+"#"+author.discriminator, 'children':childrenSort(author.name+"#"+author.discriminator)}
        else:
            
            familytree = {'parent':author.name+"#"+author.discriminator+" + " + partner, 'children':childrenSort(author.name+"#"+author.discriminator)}
        print(familytree)
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()
        t = createTree(familytree)
        def printout(parent, indent=0):
            
            
            print('\t'*indent, parent.name)
            # Call your algorithm function.
            # etc...
            
            
            for child in parent.children:
                printout(child, indent+1)        
        printout(t)
        sys.stdout = old_stdout # Put the old stream back in place
        whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        await ctx.send("```"+whatWasPrinted+"```")
        await ctx.send("Use ms!help to see the format of the tree")
    
        
        



def setup(bot):
    bot.add_cog(t(bot))
