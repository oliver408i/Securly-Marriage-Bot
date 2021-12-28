import pickledb
from discord.ext import commands
import discord
import asyncio
class ad(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    #COMMAND OF ADOPTION
    async def ad(self, ctx, member: discord.Member = None):
        author = ctx.author
        target = member
        #open database
        db = pickledb.load('database.txt', False)
        if target == None:
            return await ctx.send("Please mention a member")
        if target.name+"#"+target.discriminator == author.name+"#"+author.discriminator:
            return await ctx.send("You can't adopt yourself!!!")
        if db.exists(author.name+"#"+author.discriminator+'partner') and target.name+"#"+target.discriminator == db.get(author.name+"#"+author.discriminator+'partner'):
            return await ctx.send("You can't adopt your partner!!!")
        if db.exists(target.name+"#"+target.discriminator+'parent'):
            return await ctx.send("That user alright has a parent!")
        
        #ask for {target}'s approval
        question = await ctx.send(f"<@{target.id}>, <@{author.id}> would like to adopt you!\nReact with ✅ for yes, don't respond for no.")
        await question.add_reaction('✅')
        
        def check(reaction, user):
            return user == target and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            #They said no basically
            return await ctx.send('Timed out')
        else:
            #they said yes
            #check if they alright have a parent etc.
            if db.exists(target.name+"#"+target.discriminator+'parent'):
                return await ctx.send(f"<@{author.id}>, <@{target.id} user alright has a parent!")
            #append the name if target alright has children
            if db.exists(author.name+"#"+author.discriminator+'child'):
                alrighthas = db.get(author.name+"#"+author.discriminator+'child')
                db.set(author.name+"#"+author.discriminator+'child', alrighthas + "|/" + target.name+"#"+target.discriminator)
            else:
                #otherwise just set it
                db.set(author.name+"#"+author.discriminator+'child', str(target.name+"#"+target.discriminator))
            db.set(target.name+"#"+target.discriminator+'parent', str(author.name+"#"+author.discriminator))
            db.dump()
            return await ctx.send(f"<@{author.id}>, <@{target.id}> agreed!")
        



def setup(bot):
    bot.add_cog(ad(bot))
