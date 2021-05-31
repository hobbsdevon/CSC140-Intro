import discord
import math
import random
import pymongo
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient('your mongoDB login here')

db = cluster["discord"]
characters = db["characters"]
inventories = db["inventories"]
info = db["info"]


client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def roll(ctx, roll : str, mod : int):
    total = 0
    diceNum = roll.split('d')[0]
    diceVal = roll.split('d')[1]
    rolls, limit = map(int, roll.split('d'))
    for i in range(rolls):
        result = random.randint(1, limit)
        total += result
    total += mod
    await ctx.send('Your total is ' + str(total))

@roll.error
async def rollError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Add your modifier ffs')

@client.command()
async def deathsave(ctx):
    result = random.randint(1, 20)
    if result == 1:
        await ctx.send(f'Big L, you rolled a {result}. Two failures for you>')
    elif result > 1 and result < 10:
        await ctx.send(f'Cringe ass failed with a {result}')
    elif result >= 10 and result <20:
        await ctx.send(f'Success! with a {result}')
    else:
        await ctx.send(f'Cheater rolled a {result}. You regain conciousness.')

@client.command()
async def spellinfo(ctx, thing):
    thing = thing.lower()
    results = info.find({'_id':'spells'})
    for result in results:
        answer = result[thing]
    await ctx.send(f'{thing}\n{answer}')

@client.command()
async def rollcheck(ctx, mod : int):
    result = random.randint(1, 20)
    result += mod
    await ctx.send(f'You rolled a {result}')



'''
@client.command()
async def stats(ctx, name):
    results = characters.find({'_id' : name})
    for result in results:
        name = result['_id']
        Str = result['Str']
        Dex = result['Dex']
        Con = result['Con']
        Int = result['Int']
        Wis = result['Wis']
        Cha = result['Cha']
    await ctx.author.send(f'{name}\nYour stats are:\nStr: {Str}\nDex: {Dex}'
                          f'\nCon: {Con}\nInt: {Int}\nWis: {Wis}\nCha: {Cha}')
@client.command()
async def createChar(ctx, name, playerName, race, klass, level, background, alignment,
                     speed, hp, Str, Dex, Con, Int, Wis, Cha):
    char = {'_id':name}, {'playerName':playerName}, {'race':race}, {'class(es)':klass},
    {'level':level}
    characters.insert([char])
    await ctx.author.send(f'{name} has been created!')
'''

client.run('your token here')
