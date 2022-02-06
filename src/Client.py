# imports
from config_checker import check
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='.',help_command=None)
from discord.ext.commands import has_permissions, CheckFailure
# bot event
@bot.event
# if the bot was ready
async def on_ready():
    print("Bot is online!") #Bot is online!
#!COMMAND SECTION
@bot.command()
async def help(ctx):
    await ctx.send("Hello " + str(ctx.author.mention) +  " ! \nYou Can Ban users, by typing: \n`.ban <user>`\n or, kicking by: \n`.kick <user>`\n**By GHALBEYOU in github**")
@bot.command()
@has_permissions(manage_messages=True, manage_roles=True)
async def ban(ctx,user: discord.Member):
    await user.send(content="You have been banned from " + str(ctx.guild.name) + " !",delete_after=5)
    await ctx.send("Banned user!")
    await user.ban()
@bot.command()
@has_permissions(manage_messages=True, manage_roles=True)
async def kick(ctx,user: discord.Member):
    await user.kick()
    await ctx.send("Kicked user!")
@ban.error
async def ban_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you don't have the perm.")
@kick.error
async def kick_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you don't have the perm.")
if check() == "BOT_TOKEN":
    print("Please edit the token in config.json file!")
else:
    bot.run(check())