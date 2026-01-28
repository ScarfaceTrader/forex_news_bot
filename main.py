import os
import discord
from discord.ext import commands
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
  print(f'✅ Bot conectado: {bot.user}')
@bot.command()
async def ping(ctx):
  await ctx.send('🏓 Pong!')
@bot.command()
async def reporte(ctx):
  await ctx.send('📊 Reporte funcionando')
bot.run(TOKEN)
