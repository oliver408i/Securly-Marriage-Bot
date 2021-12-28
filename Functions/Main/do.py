import pickledb
from discord.ext import commands
import discord

class do(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['disown', 'removechildren', 'leavechildren'])
    @commands.guild_only()
    #disown - remove child
    async def do(self, ctx, member: discord.Member = None):
        author = ctx.author.name+"#"+ctx.author.discriminator
        db = pickledb.load('database.txt', False)
        if member == None:
            return await ctx.send("Please mention a member")
        target = member.mention
        #The list of children is stored as a string in
        #example: child1|/child2|/
        #|/ is the seperator
        targetC = db.get(author+'child').split("|/")
        #check if the child exists
        try:
            targetC.remove(target)
        except:
            return await ctx.send("That user isn't your child!")
        #check if the user has a child. If not, just remove the key
        if targetC == []:
            db.rem(author+'child')
        else:
            #otherwise put the list back into a string and put it into th key
            stuff = "|/".join(targetC)
            db.set(author+'child', stuff)
        db.rem(target+'parent')
        db.dump()
        await ctx.send(f"@{target}, @{author} removed you as a child!")
        



def setup(bot):
    bot.add_cog(do(bot))
