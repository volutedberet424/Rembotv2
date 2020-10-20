import discord
import random
import asyncio
import os
import json
from discord.ext import commands
from PIL import Image
from io import BytesIO
from discord import VoiceClient
from random import seed
from random import randint

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]      



client = commands.Bot(command_prefix = "r!")

animes = ["Re:ZERO Starting Life in Another World", "Darling in the Franxx", "The Rising of the Shield Hero", "Kill la Kill", "Mob Psycho 100", "Mob Psycho 100 S2", "Re:ZERO Starting Life in Another World S2", "One Punch Man", "One Punch Man S2", "Overlord", "Overlord S2", "Overlord S3", "Satsuriku no Tenshi", "Sakura-sou no Pet na Kanojo", "Youjo Senki", "Uzaki-chan Wants to Hang Out!", "Tejina-senpai", "That Time I Got Reincarnated as a Slime", "Mekakucity Actors", "Tower of god", "Black Rock Shooter", "	Chuunibyou demo Koi ga Shitai!", "Re:zero Memory snow OVA", "Konosuba", "Konosuba S2", "Mushikago no Cagaster", "Neon Genesis Evangelion"
, "Shokugeki no Souma(Foodwars!)", "Shokugeki no Souma(Foodwars!) S2", "Shokugeki no Souma(Foodwars!) S3", "Shokugeki no Souma(Foodwars!) S4", "Shokugeki no Souma(Foodwars!) S5", "Attack on titan", "Attack on titan S2", "Attack on titan S3"]


async def status_task():
        await client.change_presence(activity=discord.Game(name="r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren van bent! │ r!info"))
        await asyncio.sleep(10)
        status_task()
        client.loop.create_task(status_task())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren van bent! │ r!info"))
    print("###########################")
    print("#                         #")
    print("# Rembot by: volutedberet #")
    print("#                         #")
    print("###########################")
    client.loop.create_task(status_task())

        
  
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('A Rembot még bétában van tehát akadhatnak bugok, illetve meg kevés command van csak!```Fontosabb dolgok hogy elkezd használni a botot: Prefix: r!, infó parancs: r!info, Parancslista: r!parancsok```')
        break

 
            

@client.command()
async def info(ctx):
    iembed = discord.Embed(title = "Rembot infók", description = "Egy anime köré épitett bot, de tud sok mást is! Például képmanipulálás, moderálás, és még sok mást is!!", color = discord.Colour.blue())
    iembed.add_field(name = "Készitő:", value = "Volutedberet", inline = True)
    iembed.add_field(name = "Nyelv:", value = "python", inline = True)
    iembed.add_field(name = "Fontosabb infók:", value = "prefix: r!, parancslista: r!parancsok", inline = True)
    iembed.add_field(name = "support szerver", value = "[invite](https://discord.gg/YDRRKQA)", inline = True)
    iembed.add_field(name = "Source code:", value = "[Github repo](https://github.com/volutedberet424/Rembotv2)", inline = True)
    iembed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/rezero/images/0/02/Rem_Anime.png/revision/latest/window-crop/width/200/x-offset/281/y-offset/0/window-width/721/window-height/720?cb=20160730213532")
    iembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=iembed)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    uiembed = discord.Embed(title = f"{member.name} adatai", description = f"{member.mention}", color = discord.Colour.blue())
    uiembed.add_field(name = "ID:", value = member.id , inline = True)
    uiembed.add_field(name="Legnagyobb rang:", value=member.top_role)
    uiembed.set_thumbnail(url = member.avatar_url)
    uiembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=uiembed)




@client.command()
async def makerem(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author


    rtemplate = Image.open("RemTemplate.png")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
    pfp = pfp.resize((477, 477))

    rtemplate.paste(pfp, (250, 60))

    rtemplate.save("remedit.png")

    await ctx.send(file = discord.File("remedit.png"))


@client.command()
async def szemét(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author


    ttemplate = Image.open("TrashTemplate.png")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
    pfp = pfp.resize((200, 200))

    ttemplate.paste(pfp, (100, 60))

    ttemplate.save("trashedit.png")

    await ctx.send(file = discord.File("trashedit.png"))


@client.command()
async def pofon(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    stemplate = Image.open("SlapTemplate.jpg")
    original = ctx.author.avatar_url_as(size = 128)
    other = user.avatar_url_as(size = 128)
    data = BytesIO(await original.read())
    data2 = BytesIO(await other.read())
    pfp = Image.open(data)
    pfp2 = Image.open(data2)
    pfp = pfp.resize((300, 300))
    pfp2 = pfp2.resize((300, 300))

    stemplate.paste(pfp, (460, 50))
    stemplate.paste(pfp2, (850, 300))
    

    stemplate.save("slapedit.jpg")

    await ctx.send(file = discord.File("slapedit.jpg"))

@client.command()
async def kézfogás(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    htemplate = Image.open("HandShakeTemplate.jpg")
    original = ctx.author.avatar_url_as(size = 128)
    other = user.avatar_url_as(size = 128)
    data = BytesIO(await original.read())
    data2 = BytesIO(await other.read())
    pfp = Image.open(data)
    pfp2 = Image.open(data2)
    pfp = pfp.resize((300, 300))
    pfp2 = pfp2.resize((300, 300))

    htemplate.paste(pfp, (50, 50))
    htemplate.paste(pfp2, (1200, 50))
    

    htemplate.save("hshakeedit.jpg")

    await ctx.send(file = discord.File("hshakeedit.jpg"))


@client.command()
async def updateok(ctx):
    await ctx.send("-v0.1 A bot 24/7 fut")

@client.command()
async def randomszám(ctx, num1: int, num2: int):
        value = randint(num1, num2)
        await ctx.send(f"A számod az a:**{value}**")


@client.command()
async def uptime(ctx):
    await ctx.send("A bot 24/7 fut kivéve akkor amikor egy update jön ki, vagy pedig ha egy bug kerül fixálásra!")


@client.command()
async def votegay(ctx, member: discord.Member):
    msg = await ctx.send(f"Szerintetek {member.name} meleg?")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
        
@client.command()
async def watchanime(ctx):
    aniembed = discord.Embed(title = "Anime linkek", description = "Kérd le egy parancsal az itt található animék összes részét, évadát!", color = discord.Colour.green())
    aniembed.add_field(name = "Rezero", value = "r!rezero, r!rezeros2", inline = True)
    await ctx.send(embed=aniembed)
   

@client.command()
async def rezero(ctx):
    reembed = discord.Embed(title = "Re:ZERO Starting Life in Another World", description = "Második évad parancsa: r!rezeros2", color = discord.Colour.blue())
    reembed.add_field(name = "ep1", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_01)", inline = True)
    reembed.add_field(name = "ep2", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_02)", inline = True)
    reembed.add_field(name = "ep3", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_03)", inline = True)
    reembed.add_field(name = "ep4", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_04)", inline = True)
    reembed.add_field(name = "ep5", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_05)", inline = True)
    reembed.add_field(name = "ep6", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_06)", inline = True)
    reembed.add_field(name = "ep7", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_07)", inline = True)
    reembed.add_field(name = "ep8", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_08)", inline = True)
    reembed.add_field(name = "ep9", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_09)", inline = True)
    reembed.add_field(name = "ep10", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_10)", inline = True)
    reembed.add_field(name = "ep11", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_11)", inline = True)
    reembed.add_field(name = "ep12", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_12)", inline = True)
    reembed.add_field(name = "ep13", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_13)", inline = True)
    reembed.add_field(name = "ep14", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_14)", inline = True)
    reembed.add_field(name = "ep15", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_15)", inline = True)
    reembed.add_field(name = "ep16", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_16)", inline = True)
    reembed.add_field(name = "ep17", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_17)", inline = True)
    reembed.add_field(name = "ep18", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_18)", inline = True)
    reembed.add_field(name = "ep19", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_19)", inline = True)
    reembed.add_field(name = "ep20", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_20)", inline = True)
    reembed.add_field(name = "ep21", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_21)", inline = True)
    reembed.add_field(name = "ep22", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_22)", inline = True)
    reembed.add_field(name = "ep23", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_23)", inline = True)
    reembed.add_field(name = "ep24", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_24)", inline = True)
    reembed.add_field(name = "ep25", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_25)", inline = True)
    reembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    reembed.set_thumbnail(url = "https://i5.walmartimages.com/asr/033a9851-afd8-4f5e-a9be-35197e8e1974_1.b506d4333c1c4cb93ae8b519f23e52b5.jpeg")
    
    await ctx.send(embed=reembed)

@client.command()
async def rezeros2(ctx):
    re2embed = discord.Embed(title = "Re:ZERO Starting Life in Another World S2", description = "", color = discord.Colour.blue())
    re2embed.add_field(name = "ep1", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2_evad_1resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep2", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_2resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep3", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_3resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep4", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_4resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep5", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_5resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep6", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_6resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep7", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_7resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep8", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_8resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep9", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_2evad_9resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep10", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_S2_10_resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep11", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_S2_11_resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep12", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_S2_12_resz_Magyar_Felirattal)", inline = True)
    re2embed.add_field(name = "ep13", value = "[Megtekintés](https://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_S2_13_resz_Magyar_Felirattal)", inline = True)

    re2embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    re2embed.set_thumbnail(url = "https://ih1.redbubble.net/image.1297475483.9873/flat,750x,075,f-pad,750x1000,f8f8f8.u1.jpg")
    
    await ctx.send(embed=re2embed)    


@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=753645694799183963&permissions=8&scope=bot")

@client.command()
async def ping(ctx):
    await ctx.send(f"A válaszidőm:```{round(client.latency * 1000)}ms```")
    

@client.command()
async def parancsok(ctx):
    embed = discord.Embed(title = "Parancsok", description = "A bot még bétában van tehát még lesznek parancsok. A bot prefixe: r!", color = discord.Colour.green())
    embed.add_field(name = "Teszt parancsok", value = "ping", inline = True)
    embed.add_field(name = "Alap parancsok", value = "info, parancsok, invite, updateok, uptime, randomszám", inline = True)
    embed.add_field(name = "Moderátor parancsok", value = "clear, kick, ban, slowmode, userinfo", inline = True)
    embed.add_field(name = "Funolós parancsok", value = "votegay", inline = True)
    embed.add_field(name = "Képes parancsok", value = "makerem, pofon, szemét, kézfogás", inline = True)
    embed.add_field(name = "Animével kapcsolatos parancsok", value = "animeajánlás, watchanime(Animékhez hyperlinkeket biztosít)", inline = True)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=embed)

@client.command()
async def animeajánlás(ctx):
    animeoutput = random.choice(animes)
    await ctx.send(animeoutput)

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f"Kitöröltem {amount} üzenetet!")

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,indok = "Nincs indok megadva"):
    await member.kick(reason=indok)
    await ctx.send(f"{member} Ki lett kickelve a következő ok miatt: ```{indok}```")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,indok = "Nincs indok megadva"):
    await member.ban(reason=indok)
    await ctx.send(f"{member} Ki lett bannolva a következő ok miatt: ```{indok}```")


@client.command()
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Erre a csatornára slowmode lett rakva **{seconds}** Másodpercre!")

client.run(os.environ['token'])
