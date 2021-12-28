import pickledb
from discord.ext import commands
import discord
import asyncio
class m(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['makepartner', 'partner', 'marry'])
    @commands.guild_only()
    #command for getting a partner
    async def m(self, ctx, member: discord.Member = None):
        db = pickledb.load('database.txt', False)
        author = ctx.author
        print(type(member))
        #do some checks and stuff
        if member == None:
            return await ctx.send("Please mention a member")
        if member.name+"#"+member.discriminator == author:
            return await ctx.send("You can partner with yourself")
        if db.exists(member.name+"#"+member.discriminator+'partner') or db.exists(author.name+"#"+author.discriminator+'partner'):
            return await ctx.send("Either you or the other user alright has a partner!")
        if db.exists(author.name+"#"+author.discriminator+"child"):
            def getChildren(parent):
                childlist = []
                for child in db.get(parent+'child').split("|/"):
                        if child == '':
                            pass
                        else:
                            if db.exists(child+'child'):
                                childlist.extend(db.get(child+"child").split('|/'))
                                childlist.extend(getChildren(child))
                            else:
                                return childlist
            lastchild = db.get(author.name+"#"+author.discriminator+"child").split("|/")
            for thischild in lastchild:
                if thischild == '':
                    lastchild.remove(thischild)
                elif db.exists(thischild+'child'):
                    lastchild.extend(getChildren(thischild))
                else:
                    break
            if member.name in lastchild:
                return await ctx.send("You cannot marry you child (or grandchild etc.)!")
        #ask for acept
        question = await ctx.send(f"<@{member.id}>, <@{author.id}> would like to partner with you!\nReact with ✅ for yes, don't respond for no.")
        await question.add_reaction('✅')
        
        def check(reaction, user):
            return user == member and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send('Timed out')
        else:
            #push the values
            db.set(author.name+"#"+author.discriminator+'partner', str(member.name+"#"+member.discriminator))
            db.set(member.name+"#"+member.discriminator+'partner', str(author.name+"#"+author.discriminator))
            db.dump()
            return await ctx.send(f"<@{author.id}>, <@{member.id}> agreed!")
        



def setup(bot):
    bot.add_cog(m(bot))
