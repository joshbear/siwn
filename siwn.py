import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import os
from dotenv import load_dotenv
import monster
from random import randint

load_dotenv()

token = os.getenv('TOKEN')
client = commands.Bot(command_prefix='/')
slash = SlashCommand(client, sync_commands=True)


@slash.slash(
    name='roll',
    description='Let\'s roll some dice, baby!',
    guild_ids=[630751149183467522]
)
async def _roll(ctx, args=None):
    """Roll some dice.
    args -- A string to be parsed into dice rolls.
    """
    if args is None:
        # await ctx.send('Create a new monster?')
        embed = discord.Embed(title='Commands')
        embed.add_field(name='Roll Dice',
                        value='Example: /roll 3d6 rolls 3 six-sided dice.',
                        inline=False)
        await ctx.send(content=None, embed=embed)
    else:
        args = args.split(' ')
        dice = []
        results = []
        sum = 0
        embed = discord.Embed(title='Roll Results')
        for arg in args:
            roll = arg.split('d')
            if (len(roll) == 1) or (roll[0] == ''):
                roll = ['1', str(roll[len(roll)-1])]
            if (len(roll) != 2):
                await ctx.send('I could not parse your dice request.')
                return
            else:
                for i in range(int(roll[0])):
                    die = ('d' + roll[1])
                    result = randint(1, int(roll[1]))
                    sum += result
                    dice.append(die.ljust(5, ' '))
                    results.append(str(result).ljust(5, ' '))
        dice.append('Sum')
        results.append(str(sum))
        await ctx.send(f"```{''.join(dice)}\n{''.join(results)}```")


@slash.slash(
    name='new',
    description='Create a new entity. Current entities include: <monster>',
    guild_ids=[630751149183467522]
)
async def _new(ctx, args=None):
    """Create a new entity.
    args -- A string of arguments that can be separated by spaces as I haven't
            figured out how to pass optional arguments in slash commands.
            Currently, no arguments will give instructions. Ultimately, would
            like to have separate entities such as <monster>, <adventure> etc.

    """
    if args is None:
        # await ctx.send('Create a new monster?')
        embed = discord.Embed(title='Commands')
        embed.add_field(name='/new <entity>',
                        value='Create new entity. Current entities include:\n' \
                              '  monster | Generates a monster from WWN\n' \
                              '  dream   | This is not a thing',
                        inline=False)
        embed.add_field(name='/test', value='Just a tester', inline=True)
        await ctx.send(content=None, embed=embed)

    else:
        print(args)
        monst = monster.new_monster()
        await ctx.send(monst)


client.run(os.getenv('TOKEN'))


"""
Code for being annoying to individuals:
    elif ctx.author.id == 143116953366691840:
        await ctx.send(f'No way I\'m listening to a real programmer. Bug off, {ctx.author}! You\'ll deconstruct me!')
    elif ctx.author.id == 542781031422361613:
        monst = monster.new_monster()
        await ctx.send(f'Now {ctx.author} is someone I can trust!\n{monst}')
"""
