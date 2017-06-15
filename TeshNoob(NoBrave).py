import discord
from discord.ext import commands
import asyncio
import datetime
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import GameGenScript3
import GameGenScript4
import SexDiceGen

def randomchoose(arr):
    return arr[random.randint(0, len(arr)-1)]

server = discord.Server
description = "A bot for Tech's general purposes."
bot = commands.Bot(command_prefix='+', description=description)

logging.basicConfig(filename="TeshNoob-Log.txt", level=logging.DEBUG)

@bot.event
async def on_ready():
    print('[{}] Logged in as'.format(datetime.datetime.now()), bot.user.name)
    logging.info("Logged in as " + bot.user.name)

# ------- start of commands -------

@bot.command(pass_context=True, description="Greets the user!")
async def hello(context):
    #greets the caller
    print("[{}] I got a 'hello' from ".format(datetime.datetime.now()) + context.message.author.name + "!")
    await bot.say("Hello! I'm a bot!")
    logging.info("I got a 'hello' from " + bot.user.name)

@bot.command(pass_context=True, description="Sends a DM to Tech!")
async def veryimportant(context, message : str):
    print("[{}] Very important from ".format(datetime.datetime.now()) + context.message.author.name + "!")
    logging.info("Very important from " + context.message.author.name + "!")
    await bot.send_message(await bot.get_user_info('143117280585187328'), "Very important message from " + context.message.author.name + "!! Message: '" + message.replace("+veryimportant ", "") + "'")
    await bot.say("Message sent to Tesh!")
    logging.info("Message sent to Tesh!")


@bot.command(pass_context=True, description="Hugs a user you mention!")
async def hug(context, member : discord.Member):
    await bot.send_message(context.message.channel, "```\nhugs " + member.name + "\n```")
    print("[{}] Hug sent!".format(datetime.datetime.now()))
    logging.info("Hug sent!")

@bot.command(description="The X Files theme.")
async def xfiles():
    await bot.say("*The sound of the X Files theme song fills the room.*")
    print("[{}] X files! doo doo doo doo doo dooooo".format(datetime.datetime.now()))
    logging.info("X files!")

@bot.command(description="Press F.")
async def payrespects():
    await bot.say("```\nPress F to Pay Respects\n```")
    print("[{}] F has been pressed.".format(datetime.datetime.now()))
    logging.info("F has been pressed.")

@bot.command(description="Generates a game idea.")
async def gameidea():
    sendstring = GameGenScript3.sendToChat()
    await bot.say(sendstring)
    print("[{}] Game idea generated.".format(datetime.datetime.now()))
    logging.info("Game idea generated.")

@bot.command(description="Generates a game idea (FUODM ONLY).")
async def fuodmgameidea():
    sendstring = GameGenScript4.sendToChat()
    await bot.say(sendstring)
    print("[{}] FUODM Game idea generated.".format(datetime.datetime.now()))
    logging.info("FUODM Game idea generated.")

@bot.command(description="Generates a sex dice situation.")
async def sexdice():
    sendstring = SexDiceGen.sendToChat()
    await bot.say(sendstring)
    print("[{}] Sex dice generated.".format(datetime.datetime.now()))
    logging.info("Sex dice generated.")

# ------- end of commands -------

bot.run('MzI0MjUxODQzNjUzOTI2OTE0.DCG-qQ.KSIsjXzNEuamkl5BxLB9PyFajpM')
