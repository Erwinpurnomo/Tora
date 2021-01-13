import discord
from discord.ext import commands

client = commands.Bot(command_prefix="=")

f = open("rules.txt", "r")
rules = f.readlines()

filtered_words = ["fuck", "fvck", "shit", "dog", "fucking", "fvcking"]

@client.event
async def on_ready():
    print("Bot Is Ready")


@client.command(aliases=['rules'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number) - 1])


@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)


@client.command(aliases=['users', 'whois'])
async def user(ctx, member : discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Colour.blue())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

client.run('Nzk4MzU5NzQwNjg1MzUyOTgx.X_z4cg.egpqvGKl0v99Zc1SLQAGHUzwA-M')
