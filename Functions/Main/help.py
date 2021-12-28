from discord.ext import commands
import discord

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h', 'plshelp', 'helppls'])
    @commands.guild_only()
    #help command yea
    async def help(self, ctx):
        await ctx.send("**commands**\nms!ad <user> - adopt someone\nms!m <user> - marry (propose to someone) *partner = the person you married*\nms!d - remove your partner ~~with utter force~~\nms!do <child> - remove that child ~~via throwing out the door~~\nms!e - remove your parent ~~by running away~~\nms!c - removes your entire family\n**ms!t - show your family tree**\nFamily tree format is:\n```Parent + Partner\n    child1\n    child2\n        child of child2\n...and so on```")
        



def setup(bot):
    bot.add_cog(help(bot))
