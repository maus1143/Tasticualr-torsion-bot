import discord
from discord.ext import commands
import logging

TOKEN = 'Bot-token-hier'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

last_used_spell = {}

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name}')

@bot.slash_command(name='zaby', description='Sendet einen Zabygonde edit')
async def zaby(ctx):
    gif_url = 'https://images-ext-1.discordapp.net/external/YYNbtpeCnaQH3MtYrot_kz5zbqqJf4vnkYAUD6cV-6c/https/media.tenor.com/CFl2FOnmqbMAAAPo/bardin-vermintide.mp4'
    logging.info(f'Sending GIF to {ctx.channel} from user {ctx.author}')
    await ctx.send(gif_url)

@bot.slash_command(name='testicular_torsion', description='Cast Testicular torsion')
async def testicular_torsion(ctx, target: discord.Member):
    last_used_spell[ctx.author.id] = 'Testicular Torsion'
    gif_url = 'https://media1.tenor.com/m/Q0lyIn6dmcgAAAAd/ow.gif'
    logging.info(f'{ctx.author} is casting Testicular Torsion on {target} in {ctx.channel}')
    await ctx.send(f'{ctx.author.mention} wirkt Testicular Torsion auf {target.mention}!')
    await ctx.send(gif_url)

@bot.slash_command(name='reflect', description='Back to the sender')
async def reflect(ctx, target: discord.Member):
    spell = last_used_spell.get(target.id, 'keinen Zauber')
    if spell == 'keinen Zauber':
        response = f'{ctx.author.mention} konnte keinen Zauber finden, um ihn zu reflektieren.'
    else:
        logging.info(f'{ctx.author} is reflecting {spell} from {target} in {ctx.channel}')
        response = f'{ctx.author.mention} reflektiert den Zauber "{spell}" von {target.mention}!'
    
    image_url = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fspells8.com%2Fwp-content%2Fuploads%2F2021%2F07%2FMirror-Reversal-Spell-360x240.jpg'
    await ctx.send(response)
    await ctx.send(image_url)

@bot.event
async def on_command_error(ctx, error):
    logging.error(f'An error occurred: {error}')

bot.run(TOKEN)

#by Mausi Schmausi