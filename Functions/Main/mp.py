import pickledb
from discord.ext import commands
import discord
import asyncio
class mp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['makeparent', 'bechildof'])
    @commands.guild_only()
    #command for makeparent
    async def mp(self, ctx, member: discord.Member = None):
        author = ctx.author
        target = member
        #check etc
        db = pickledb.load('database.txt', False)
        if target == None:
            return await ctx.send("Please mention a member")
        if target.name+"#"+target.discriminator == author.name+"#"+author.discriminator:
            return await ctx.send("You can't make yourself your parent!!!")
        if db.exists(author.name+"#"+author.discriminator+'partner') and target.name+"#"+target.discriminator == db.get(author.name+"#"+author.discriminator+'partner'):
            return await ctx.send("You can't make your partner your parent!!!")
        if db.exists(author.name+"#"+author.discriminator+'parent'):
            return await ctx.send("You alright have a parent!")
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
            if target.name+"#"+target.discriminator in lastchild:
                return await ctx.send("You cannot make your child (or grandchild etc.) your parent!")
        #basically same thing as ad.py
        question = await ctx.send(f"<@{target.id}>, <@{author.id}> would like to make you their parent!\nReact with ✅ for yes, don't respond for no.")
        await question.add_reaction('✅')
        
        def check(reaction, user):
            return user == target and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send('Timed out')
        else:
            #taking out the list of children of target and appending author
            if db.exists(target.name+"#"+target.discriminator+'child'):
                alrighthas = db.get(author.name+"#"+author.discriminator+'child')
                db.set(target.name+"#"+target.discriminator+'child', alrighthas + "|/" + target.name+"#"+target.discriminator)
            else:
                db.set(target.name+"#"+target.discriminator+'child', str(author.name+"#"+author.discriminator))
            db.set(author.name+"#"+author.discriminator+'parent', str(target.name+"#"+target.discriminator))
            db.dump()
            return await ctx.send(f"<@{author.id}>, <@{target.id}> agreed!")
        



def setup(bot):
    bot.add_cog(mp(bot))
