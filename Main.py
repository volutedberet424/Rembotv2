import discord
import random
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix="r!")

animes = ["Re:ZERO Starting Life in Another World", "Darling in the Franxx", "The Rising of the Shield Hero", "Kill la Kill", "Mob Psycho 100", "Mob Psycho 100 S2", "Re:ZERO Starting Life in Another World S2", "One Punch Man", "One Punch Man S2", "Overlord", "Overlord S2", "Overlord S3", "Satsuriku no Tenshi", "Sakura-sou no Pet na Kanojo", "Youjo Senki", "Uzaki-chan Wants to Hang Out!", "Tejina-senpai", "That Time I Got Reincarnated as a Slime", "Mekakucity Actors", "Tower of god", "Black Rock Shooter", "	Chuunibyou demo Koi ga Shitai!", "Re:zero Memory snow OVA", "Konosuba", "Konosuba S2", "Mushikago no Cagaster", "Neon Genesis Evangelion"
, "Shokugeki no Souma(Foodwars!)", "Shokugeki no Souma(Foodwars!) S2", "Shokugeki no Souma(Foodwars!) S3", "Shokugeki no Souma(Foodwars!) S4", "Shokugeki no Souma(Foodwars!) S5", "Attack on titan", "Attack on titan S2", "Attack on titan S3", ""]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren van bent! │ r!info"))
    print("###########################")
    print("#                         #")
    print("# Rembot by: volutedberet #")
    print("#                         #")
    print("###########################")
  
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Prefixem: r!, infók: r!info, parancslista: r!parancsok")
        break


@client.command()
async def info(ctx):
    await ctx.send("Egy anime köré épitett magyar nyelvü discord bot! De még sok másra is jó. Prefix: r! Parancslista: r!parancsok")

@client.command()
async def updateok(ctx):
    await ctx.send("Itt lesz minden update amit a bot kap!!!")

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=753645694799183963&permissions=8&scope=bot")

@client.command()
async def ping(ctx):
    await ctx.send(f"A válaszidőm:```{round(client.latency * 1000)}ms```")

@client.command()
async def parancsok(ctx):
    embed = discord.Embed(title = "Parancsok", description = "A bot még bétában van tehát még lesznek parancsok", color = discord.Colour.green())
    embed.add_field(name = "Teszt parancsok", value = "ping", inline = True)
    embed.add_field(name = "Alap parancsok", value = "info, parancsok", inline = True)
    embed.add_field(name = "Moderátor parancsok", value = "clear", inline = True)
    embed.add_field(name = "Animével kapcsolatos parancsok", value = "animeajánlás", inline = True)
    await ctx.send(embed=embed)

@client.command()
async def animeajánlás(ctx):
    animeoutput = random.choice(animes)
    await ctx.send(animeoutput)

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)



client.run("NzUzNjQ1Njk0Nzk5MTgzOTYz.X1pNPw.7dhSNA9-rwnH9JIGfwHvtWNC-BE")