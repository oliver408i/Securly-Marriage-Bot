import pickledb
from discord.ext import commands


class e(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['runaway', 'emancipate', 'leaveparent'])
    @commands.guild_only()
    #Command for removing your parent
    async def e(self, ctx):
        author = ctx.author.name+"#"+ctx.author.discriminator
        db = pickledb.load('database.txt', False)
        if not db.exists(author+'parent'):
            return await ctx.send("You don't have a parent!")
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
        db.dump()
        await ctx.send(f"{target}, {author} removed you as a parent!")
        



def setup(bot):
    bot.add_cog(e(bot))
