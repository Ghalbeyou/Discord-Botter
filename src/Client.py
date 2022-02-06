# imports
from discord.ext.commands.bot import Bot
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
    embed=discord.Embed(title="Help Command", description="Use the commans below to use this bot!", color=0x19f528)
    embed.add_field(name=".mute", value="mutes the user usage: .mute <user> <reason> and unmute by: .unm <user>", inline=True)
    embed.add_field(name=".games", value="play games", inline=True)
    embed.add_field(name=".action", value="ban/kick user, usage: .action ban <user> <reason>", inline=True)
    embed.set_footer(text="thats it! this bot is made by ghalbeyou in github: https://github.com/Ghalbeyou")
    await ctx.send(embed=embed)
@bot.command()
@has_permissions(manage_messages=True, manage_roles=True)
async def mute(ctx,user: discord.Member, reason):
    perms = ctx.channel.overwrites_for(user)
    await ctx.channel.set_permissions(user, send_message=not perms.send_message)
    await ctx.send("muted the " + str(user.nick) + " !")
@bot.command()
@has_permissions(manage_messages=True, manage_roles=True)
async def unm(ctx, user: discord.member):
    perms = ctx.channel.overwrites_for(user)
    await ctx.channel.set_permissions(user, send_message=not perms.send_message)
    await ctx.send("unmuted the user!")
@bot.command()
@has_permissions(manage_messages=True, manage_roles=True)
async def action(ctx,do,user: discord.Member, reason):
    if action == 'ban':
        user.ban()
        await ctx.send("BANNED USER!")
        return
    elif action == 'kick':
        user.kick()
        await ctx.send("KICKED USER!")
        return
    else:
        await ctx.send("Usage: \n `.action <do> <user> <reason>`")
        return
# error section
@unm.error
async def unm_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you don't have the perm.")
@mute.error
async def mute_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you don't have the perm.")
@action.error
@mute.error
async def action_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you don't have the perm.")
if check() == "BOT_TOKEN":
    print("Please edit the token in config.json file!")
else:
    bot.run(check())