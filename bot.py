# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from uralicNLP import uralicApi

uralicApi.download("fin")
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')

@bot.command(name='lemma')
async def lemmatize(ctx, arg):
    response = []
    lines = uralicApi.lemmatize(arg, "fin")

    if len(lines) == 0:
        await ctx.send('word not found.')
        return

    for line in lines:
        response.append(line) 

    response = ('\n'.join(response))
    await ctx.send(response)

@bot.command(name='analyze')
async def lemmatize(ctx, arg):
    response = []
    lines = uralicApi.analyze(arg, "fin")

    if len(lines) == 0:
        await ctx.send('word not found.')
        return

    for line in lines:
        response.append(line[0]) 

    response = ('\n'.join(response))
    await ctx.send(response)

@bot.command(name='generate')
async def generate(ctx, arg):
    response = []
    lines = uralicApi.generate(arg, "fin")
    if len(lines) > 0:
            for line in lines:
                response.append(line[0])

            response = ('\n'.join(response))
            await ctx.send(response)
    else:
        await ctx.send('generation not possible')

@bot.command(name='wtf')
async def lemmatize(ctx):
    response = 'Welcome to Finland'
    await ctx.send(response)


@bot.command(name='whatis')
async def lemmatize(ctx, arg):
    
    if arg == 'N':
        await ctx.send('Noun')
    elif arg == 'Sg':
        await ctx.send('Singular')
    else:
        await ctx.send('not found.')


bot.run(token)
