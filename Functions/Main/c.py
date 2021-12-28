import pickledb
from discord.ext import commands
import discord
import asyncio

class c(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['clear', 'rm', 'remove', 'killfamily'])
    @commands.guild_only()
    #delete your entire tree :D
    async def c(self, ctx):
        db = pickledb.load('database.txt', False)
        author = ctx.author.name+"#"+ctx.author.discriminator
        if not db.exists(author.name+"#"+author.discriminator+"partner") and not db.exists(author.name+"#"+author.discriminator+"child"):
            return await ctx.send("You have no family to remove")
        #just to make sure
        question = await ctx.send(f"<@{ctx.author.id}>, are you sure you want to remove ALL (children, parent, partner) of your family members?\nReact with ✅ for yes, don't respond for no.")
        await question.add_reaction('✅')
        
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            #They said no basically
            return await ctx.send('Action cancelled!')
        else:
            #delete stuff now
            #first children, if it exists
            if db.exists(author+'child'):
                #loop through all the children and remove each's parent (the author)
                for child in db.get(author+'child').split("|/"):
                    if child == '':
                        pass
                    else:
                        db.rem(child+'parent')
                db.rem(author+'child')
            #remove parent now...
            if db.exists(author+'parent'): 
                #do the same thing as in e.py
                target = db.get(author+'parent')
                db.rem(author+'parent')
                #update the child list. same way as in do.py
                targetC = db.get(target+'child').split("|/")
                try:
                    targetC.remove(author)
                except: #this case shouldn't happen unless there was an error with the database
                    return await ctx.send("That user is not your parent!")
                if targetC == []:
                    db.rem(target+'child')
                else:
                    stuff = "|/".join(targetC)
                    db.set(target+'child', stuff)
                    if db.exists(author+'partner'): 
                        partner = db.get(author+'partner')
                        db.rem(partner+'partner')
                        db.rem(author+'partner') 
            db.dump()
            return await ctx.send(f"{ctx.author.mention}, you have removed all of your family members!")
        



def setup(bot):
    bot.add_cog(c(bot))
