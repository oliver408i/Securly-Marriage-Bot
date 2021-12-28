import pickledb
from discord.ext import commands


class d(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['leavepartner', 'divorce'])
    @commands.guild_only()
    #D for leaving your partner
    async def d(self, ctx):
        author = ctx.author.name+"#"+ctx.author.discriminator
        db = pickledb.load('database.txt', False)
        if not db.exists(author+'partner'):
            return await ctx.send("You don't have a partner!")
        target = db.get(author+'partner')
        #remove the key. That's all
        db.rem(author+'partner')
        db.rem(target+'partner')
        db.dump()
        await ctx.send(f"@{target}, @{author} removed you as a partner!")
        



def setup(bot):
    bot.add_cog(d(bot))
