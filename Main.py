import discord
import random
import asyncio
import os
import json 
import dbl
import youtube_dl
import requests
import dashcord
from discord.ext import commands, tasks
from PIL import Image, ImageEnhance
from io import BytesIO
from discord.voice_client import VoiceClient
from random import seed
from random import randint
from random import choice







client = commands.Bot(command_prefix = "r!")
client.remove_command("help")

animes = ["Re:ZERO - Starting Life in Another World", "Darling In The Franxx", "The Rising of the Shield Hero", "Kill la Kill", "Mob Psycho 100", "Mob Psycho 100 S2", "Re:ZERO - Starting Life in Another World S2", "One-Punch Man", "One-Punch Man S2", "Overlord", "Overlord S2", "Overlord S3", "Satsuriku no Tenshi", "The Pet Girl of Sakurasou", "Youjo Senki", "Uzaki-chan Wants to Hang Out!", "Tejina-senpai", "That Time I Got Reincarnated as a Slime", "Mekakucity Actors", "Tower of God", "Black Rock Shooter", "Chūnibyō Demo Koi ga Shitai!", "Re:ZERO - Memory snow OVA", "Konosuba", "Konosuba S2", "Mushikago no Cagaster", "Neon Genesis Evangelion"
, "Shokugeki no Souma (Food Wars!)", "Shokugeki no Souma (Food Wars!) S2", "Shokugeki no Souma(Foodwars!) S3", "Shokugeki no Souma (Food Wars!) S4", "Shokugeki no Souma (Food Wars!) S5", "Attack on Titan", "Attack on Titan S2", "Attack on Titan S3"]

pps = ["8D", "8=D", "8==D", "8===D", "8D", "8=D", "8==D", "8===D", "8====D", "8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D",  "8=====D", "8======D", "8=======D",  "8=====D", "8======D", "8=======D",  "8=====D", "8======D", "8=======D", "8========D", "8========D", "8=========D", "8==========D", "8===========D", "8=======================================================D" , "Úristen! Ez akkora, hogy ki sem tudom írni..."]
fights = ["leütötte", " felhasználót leütötte", "kiütötte", " felhasználót kiütötte", "megverte", " felhasználót megverte"]
uselesswebs = ["https://hooooooooo.com/", "http://eelslap.com/", "https://thatsthefinger.com/", "http://corndog.io/", "https://mondrianandme.com/", "http://burymewithmymoney.com/", "https://smashthewalls.com/", "https://trypap.com/", "http://www.republiquedesmangues.fr/", "https://jacksonpollock.org/", "https://cant-not-tweet-this.com/", "http://endless.horse/", "http://www.rrrgggbbb.com/", "http://www.staggeringbeauty.com/"]


class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc1MzY0NTY5NDc5OTE4Mzk2MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA0OTU3NTAyfQ.mb55JBnvLGhsoFxpBjzynIrzxX8GM4v9jMvCdmkt8kY' # ez a dbl token nem a dc s token, semmire nem mész vele
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True) 

    async def on_guild_post():
        print("Server count posted successfully")



def setup(bot):
    bot.add_cog(TopGG(bot))

async def status_task():
        await client.change_presence(activity=discord.Game(name="Néhány infó rólam: r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren vagyok bent │ r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Ide mit írjak? │ r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Nem tudod, mikre vagyok képes? Írd be: r!parancsok"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Szavazni az r!vote paranccsal lehetséges"))
        await asyncio.sleep(10)
        status_task()
        client.loop.create_task(status_task())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren vagyok bent │ r!info"))
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
            await channel.send('A Rembot még bőven nem a végleges állapotban van, ezért előfordulhatnak hibák. Illetve folyamatosan bővül a parancsok száma. ```Egyéb tudnivalók: r!info; parancslista: r!parancsok``` Supportszerver: https://discord.gg/tCFesQjx. Partnereink megtekintéséhez használd az r!partner parancsot.')
        break


@client.command()
async def partnerek(ctx):
    partnerembed = discord.Embed(title = "Szerverek, ahol hírdetik a botot", description = "Ahhoz, hogy megtekinthesd az egyes szerverek leírását, használd az adott szerver nevét parancsként.", color = discord.Colour.green())
    partnerembed.add_field(name = "Csíkszereda", value = "Egy magyar Discord-szerver mindenkinek! Akármilyen érdeklődési körrel is rendelkezz...", inline = True)
    await ctx.send(embed=partnerembed)

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
async def csíkszereda(ctx):
    partner1embed = discord.Embed(title = "Csíkszereda", description = "Egy magyar Discord-szerver mindenkinek! Akármilyen érdeklődési körrel is rendelkezz...", color = discord.Colour.green())
    partner1embed.add_field(name = "Leírás:", value = "Mi is emeli ki a nagy tömegből? » Kedves, befogadó közösség    » Több mint 100 emoji         🔹Nitro Boosted   » Jól konfigurált bot   » Aktívabb csatornák   » Partnerségi lehetőség   » Valamint segítőkész, kedves, könnyen elérhető vezetőség", inline = True)
    partner1embed.add_field(name = "Invite:", value = "https://discord.gg/e9B5fSWb2E", inline = True)
    partner1embed.set_thumbnail(url = "https://cdn.discordapp.com/icons/611266581435252746/8807efff8b233b9d5da7cf7f3798f81a.webp?size=1024")
    await ctx.send(embed=partner1embed)


@client.command()
async def updateok(ctx):
    await ctx.send("Végre valami haladás több hónap lustaság után: szerverinfo parancs!")    

@client.command()
async def info(ctx):
    iembed = discord.Embed(title = "Rembot információk", description = "Egy anime témájú bot, mely sok-sok dolgot tartalmaz. Többek között képmanipulálás, beépített moderálás és ezek mellett még sok más...", color = discord.Colour.blue())
    iembed.add_field(name = "Készítő:", value = "Volutedberet", inline = True)
    iembed.add_field(name = "Helyesírás javitó:", value = "Ferko", inline = True)
    iembed.add_field(name = "Programozási nyelv:", value = "Python", inline = True)
    iembed.add_field(name = "Fontosabb információk:", value = "prefix: r!; r!parancsok", inline = True)
    iembed.add_field(name = "Supportszerver", value = "[Invite](https://discord.gg/tCFesQjx)", inline = True)
    iembed.add_field(name = "Source code:", value = "[Github repo](https://github.com/volutedberet424/Rembotv2)", inline = True)
    iembed.add_field(name = "Meghívó a bothoz:", value = "[Invite](https://discord.com/api/oauth2/authorize?client_id=753645694799183963&permissions=8&scope=bot)", inline = True)
    iembed.set_thumbnail(url = "https://vignette.wikia.nocookie.net/rezero/images/0/02/Rem_Anime.png/revision/latest/window-crop/width/200/x-offset/281/y-offset/0/window-width/721/window-height/720?cb=20160730213532")
    iembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=iembed)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    uiembed = discord.Embed(title = f"{member.name} adatai", description = f"{member.mention}", color = discord.Colour.blue())
    uiembed.add_field(name = "ID:", value = member.id , inline = True)
    uiembed.add_field(name="Legmagasabb rang:", value=member.top_role)
    uiembed.set_thumbnail(url = member.avatar_url)
    uiembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=uiembed)

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    pfpembed = discord.Embed(title = f"{member.name} profilképe", description = f"{member.mention}", color = discord.Colour.blue())
    pfpembed.set_image(url = member.avatar_url)
    pfpembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=pfpembed)

@client.command()
async def serverinfo(ctx):
    sinfoembed = discord.Embed(title = f"{ctx.guild.name}", description = f"A szerver tulajdonosa: {ctx.guild.owner}", color = discord.Colour.blue())
    sinfoembed.add_field(name="Tagszám:", value=ctx.guild.member_count)
    sinfoembed.add_field(name="Szerver régiója:", value=ctx.ctx.guild.region)
    sinfoembed.add_field(name = "ID:", value = ctx.guild.id , inline = True)
    sinfoembed.set_thumbnail(url = ctx.guild.icon_url)
    sinfoembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=sinfoembed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ez a parancs nem létezik. ＾_＾ Ha a parancs listázva van, viszont mégsem jó, abban az esetben szólj nyugodtan a supportszerverünkön. https://discord.gg/tCFesQjx"),
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Kérlek, várj egy pillanatot, mielőtt újra használnád a parancsot.")
@client.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Jelenleg nem vagy hangcsatornában.")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command()
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

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
async def hornyjail(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author


    rtemplate = Image.open("bonktemplate.png")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
    pfp = pfp.resize((300, 300))

    rtemplate.paste(pfp, (950, 440))

    rtemplate.save("bonk.png")

    await ctx.send(file = discord.File("bonk.png"))


@client.command()
async def gay(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
    pfp = pfp.resize((300, 300))
    g1template = Image.open("rainbow.png")
    g1template = g1template.resize((300, 300))
    g1template.putalpha(1)


    pfp.paste(g1template, (950, 440))

    gtemplate.save("gayedit.jpg")

    await ctx.send(file = discord.File("gayedit.jpg"))





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
async def vote(ctx):
    await ctx.send("Ezen az oldalon tudsz szavazni a botra: https://top.gg/bot/753645694799183963/vote. Minden szavazat sokat számít nekünk!")

@client.command()
async def randomszám(ctx, num1: int, num2: int):
        value = randint(num1, num2)
        await ctx.send(f"Az általad véletlenszerűen generált szám az a(z) **{value}**")


@client.command()
async def uptime(ctx):
    await ctx.send("A bot a hét minden napján fut, kivéve, ha egy frissítés jön ki hozzá.")


@client.command()
async def votegay(ctx, member: discord.Member):
    msg = await ctx.send(f"Szerintetek {member.name} meleg?")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")
        
@client.command()
async def watchanime(ctx):
    aniembed = discord.Embed(title = "Animékhez linkek", description = "Egy paranccsal lekérheted az itt található animék összes részét vagy évadját.", color = discord.Colour.green())
    aniembed.add_field(name = "Re:ZERO", value = "r!rezero, r!rezeros2", inline = True)
    aniembed.add_field(name = "Darling In The Franxx", value = "r!darling", inline = True)
    await ctx.send(embed=aniembed)
   
@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
async def rezero(ctx):
    reembed = discord.Embed(title = "Re:ZERO - Starting Life in Another World", description = "Második évad: r!rezeros2", color = discord.Colour.blue())
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
    reembed.add_field(name = "ep25", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_25_Vege_)", inline = True)
    reembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    reembed.set_thumbnail(url = "https://i5.walmartimages.com/asr/033a9851-afd8-4f5e-a9be-35197e8e1974_1.b506d4333c1c4cb93ae8b519f23e52b5.jpeg")
    
    await ctx.send(embed=reembed)

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
async def rezeros2(ctx):
    re2embed = discord.Embed(title = "Re:ZERO - Starting Life in Another World S2", description = "Ez az évad jelenleg is fut. Ha kijön egy új rész, a lista frissülni fog.", color = discord.Colour.blue())
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


@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
async def darling(ctx):
    darembed = discord.Embed(title = "Darling In The Franxx", description = "Sajnos még nincs második évad. :(", color = discord.Colour.blue())
    darembed.add_field(name = "ep1", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_01resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep2", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_02resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep3", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_03resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep4", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_04resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep5", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_05resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep6", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_06resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep7", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_07resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep8", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_08resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep9", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_09resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep10", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_10resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep11", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_11resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep12", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_12resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep13", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_13resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep14", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_14resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep15", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_15resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep16", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_16resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep17", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_17resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep18", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_18resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep19", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_19resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep20", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_20resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep21", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_21resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep22", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_22resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep23", value = "[Megtekintés](http://indavideo.hu/video/Darling_in_the_FranXX_23resz_Magyar_Felirat)", inline = True)
    darembed.add_field(name = "ep24", value = "[Megtekintés](https://indavideo.hu/video/Darling_in_the_FranXX_24resz_EndMagyar_Felirat)", inline = True)
    darembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    darembed.set_thumbnail(url = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQV59nZDyGolIySBJcF-aFnLexrH5piD7uS6ONiFQwdn5TUhSXT")
    
    await ctx.send(embed=darembed)

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=753645694799183963&permissions=8&scope=bot")

@client.command()
async def ping(ctx):
    await ctx.send(f"Válaszidőm: ```{round(client.latency * 1000)} ms```")
    
@client.command()
async def servercount(ctx):
    await ctx.send(f"{len(client.guilds)} szerveren vagyok bent.")
        
@client.command()
async def howsimp(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
      
    simpembed = discord.Embed(title = "Simpség mérő", description = "", color = discord.Colour.green())
    simpembed.add_field(name = "Simpség", value = f"{user.mention} {random.randint(0,100)}%-ban simp. 😞" , inline = True)
    simpembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=simpembed)

@client.command()
async def howfat(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
      
    fffembed = discord.Embed(title = "Zsírmérő", description = "", color = discord.Colour.green())
    fffembed.add_field(name = "Dagadtság:", value = f"{user.mention} {random.randint(0,100)}%-ban dagadt. 🍔 Ha 50% fölött van, akkor ideje fogyózni szerintem..." , inline = True)
    fffembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=fffembed)

@client.command()
async def epikgamerrate(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
      
    gamembed = discord.Embed(title = "Mennyire vagy *epikus* gamer?", description = "", color = discord.Colour.green())
    gamembed.add_field(name = "*Epikus* gamer mérték:", value = f"{user.mention} {random.randint(0,100)}%-ban epikus gamer. 😎" , inline = True)
    gamembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=gamembed)

@client.command()
async def howgay(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    gayembed = discord.Embed(title = "Melegség mérő", description = "", color = discord.Colour.green())
    gayembed.add_field(name = f"Melegség:", value = f"{user.mention} {random.randint(0,100)}%-ban meleg. 🏳️‍🌈", inline = True)
    gayembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=gayembed)

@client.command()
async def howcringe(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    cringeembed = discord.Embed(title = "Cringe-mérő", description = "", color = discord.Colour.green())
    cringeembed.add_field(name = f"Cringe-ség:", value = f"{user.mention} {random.randint(0,100)}%-ban cringe! 🤮", inline = True)
    cringeembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=cringeembed)
 

@client.command()
async def rankthot(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    thotembed = discord.Embed(title = "Ribancságmérő", description = "", color = discord.Colour.green())
    thotembed.add_field(name = f"Ribancság:", value = f"{user.mention} {random.randint(0,100)}%-ban egy ribanc! 😏", inline = True)
    thotembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=thotembed)

@client.command()
async def parancsok(ctx):
    embed = discord.Embed(title = "Parancslista", description = "A kategóriák elérési útjait itt olvashatod le. Parancsok száma: 53", color = discord.Colour.green())
    embed.add_field(name = "Teszt 🧪", value = "```r!teszt```", inline = True)
    embed.add_field(name = "Alap", value = "```r!alap```", inline = True)
    embed.add_field(name = "Moderálás 🛂", value = "```r!moderator```", inline = True)
    embed.add_field(name = "Fun 😂", value = "```r!fun```", inline = True)
    embed.add_field(name = "Képmanipulálás 🖼️", value = "```r!képmanipulálás```", inline = True)
    embed.add_field(name = "Anime 🤷‍♀️", value = "```r!anime```", inline = True)
    embed.add_field(name = "Zene 📀", value = "```r!zene```", inline = True)
    embed.add_field(name = "Roleplay 👋", value = "```r!roleplay```", inline = True)
    embed.add_field(name = "Ekonómia 💸", value = "```Fejlesztés alatt.```", inline = True)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=embed)

@client.command()
async def fun(ctx):
    funembed = discord.Embed(title = "Fun", description = "", color = discord.Colour.green())
    funembed.add_field(name = "Parancsok száma: 10", value = "votegay, howsimp, rankthot, howgay, howcringe, howfat, pp, epikgamerrate, fight, uselessweb", inline = True)
    funembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=funembed)

@client.command()
async def zene(ctx):
    musembed = discord.Embed(title = "Zenebot parancsok", description = "Jelenleg még készül ez a funkció.", color = discord.Colour.green())
    musembed.add_field(name = "Jelenlegi parancsok száma: 2", value = "join, leave", inline = True)
    musembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=musembed)

@client.command()
async def teszt(ctx):
    tesztembed = discord.Embed(title = "Teszt", description = "", color = discord.Colour.green())
    tesztembed.add_field(name = "Jelenlegi parancsok száma: 2", value = "ping, servercount", inline = True)
    tesztembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=tesztembed)

@client.command()
async def moderator(ctx):
    modembed = discord.Embed(title = "Moderátor parancsok", description = "", color = discord.Colour.green())
    modembed.add_field(name = "Jelenlegi parancsok száma: 6", value = "clear, kick, ban, slowmode/sm/slowm, userinfo", inline = True)
    modembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=modembed)

@client.command()
async def képmanipulálás(ctx):
    imgembed = discord.Embed(title = "képmanipulálós parancsok", description = "", color = discord.Colour.green())
    imgembed.add_field(name = "Jelenlegi parancsok száma: 5", value = "makerem, pofon, szemét, kézfogás, hornyjail", inline = True)
    imgembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=imgembed)

@client.command()
async def roleplay(ctx):
    rpembed = discord.Embed(title = "Szerepjáték parancsok", description = "", color = discord.Colour.green())
    rpembed.add_field(name = "Jelenlegi parancsok száma: 12", value = "hug, kiss, headpat, cry, laugh, laughat, shoot, bite, slap, smack, blush, profil (fejlesztés alatt)", inline = True)
    rpembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=rpembed)

@client.command()
async def anime(ctx):
    animeembed = discord.Embed(title = "Anime parancsok", description = "", color = discord.Colour.green())
    animeembed.add_field(name = "Parancsok száma: 2", value = "animeajánlás, watchanime", inline = True)
    animeembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=animeembed)

@client.command()
async def alap(ctx):
    mainembed = discord.Embed(title = "Alap parancsok", description = "", color = discord.Colour.green())
    mainembed.add_field(name = "Parancsok száma: 14", value = "partner, twitter, info, vote, uwu, owo, development, parancsok, invite, updateok, uptime, randomszám, avatar", inline = True)
    mainembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=mainembed)


@client.command()
async def uselessweb(ctx):
    weboutput = random.choice(uselesswebs)
    await ctx.send(weboutput) 

@client.command()
async def animeajánlás(ctx):
    animeoutput = random.choice(animes)
    await ctx.send(animeoutput) 

@client.command()
async def pp(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    ppoutput = random.choice(pps)    
    ppembed = discord.Embed(title = "PP-méret meghatározó", description = "", color = discord.Colour.green())
    ppembed.add_field(name = "PP-méret:", value = f"{user.mention} PP-je: {ppoutput} 😏", inline = True)
    ppembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=ppembed)


@client.command()
async def fight(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    fightoutput = random.choice(fights)    
    fightembed = discord.Embed(title = "Harctér", description = "", color = discord.Colour.green())
    fightembed.add_field(name = "harc:", value = f"{ctx.author.mention} {fightoutput} {user.mention}(t)", inline = True)
    fightembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=fightembed)

@client.command()
async def development(ctx):
    await ctx.send("A botot fejleszteni időbe telik, mivel jelenleg egyedül dolgozom a projekten. Amennyiben segíteni szeretnél a bot fejlesztésében, és ismered a Python-t, mint programozási nyelvet, akkor keress fel engem, a bot fejlesztőjét(Volutedberet#1663).")

@client.command()
async def uwu(ctx):
    await ctx.send(f"{ctx.author.mention} UwU! :3")

@client.command()
async def owo(ctx):
    await ctx.send(f"{ctx.author.mention} OwO! (⋋▂⋌)")


@client.command()
async def twitter(ctx):
    await ctx.send("Érdekel a bot fejlesztése? Kövesd a Twitter-fiókom! https://twitter.com/volutedberet")


@client.command()
async def lol(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("Mi volt ez a pusztító alpáriság?!")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount + 1)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member = None ,*,indok = "Nincs indok megadva."):
    await member.kick(reason=indok)
    await ctx.send(f"{member} ki lett dobva a következő indokkal: ```{indok}```")   



@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,indok = "Nincs indok megadva"):
    await member.ban(reason=indok)
    await ctx.send(f"{member} Ki lett tiltva a következő indokkal: ```{indok}```")


@client.command()
@commands.has_permissions(manage_messages = True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"⌛ Erre a csatornára lassú mód lett aktiválva (**{seconds}** másodperc).")

@client.command()
@commands.has_permissions(manage_messages = True)
async def sm(ctx, seconds: int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"⌛ Erre a csatornára lassú mód lett aktiválva (**{seconds}** másodperc).")

@client.command()
@commands.has_permissions(manage_messages = True)
async def slowm(ctx, seconds: int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"⌛ Erre a csatornára lassú mód lett aktiválva (**{seconds}** másodperc).")


@client.command()
@commands.has_permissions(manage_messages = True)
async def addrole(ctx, rolename):
    author = ctx.message.author
    await client.create_role(author.server, name=f"{rolename}")
    await ctx.send(f"Készítettem egy rangot {rolename} néven.")


@client.command()
async def profil(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    profilembed = discord.Embed(title = f"{member} profilja", description = f"{member} adatai. Jelenleg nem működik ez a funkció; ez még csak egy koncepció, hogy hogyan fog kinézni.", color = discord.Colour.green())
    profilembed.set_thumbnail(url=member.avatar_url)
    profilembed.add_field(name = "Készpénz:", value = "0")
    profilembed.add_field(name = "Bank:", value = "0")
    profilembed.add_field(name = "Szint:", value = "0")
    profilembed.add_field(name = "XP:", value = "▰▰▱▱▱▱▱")
    profilembed.add_field(name = "Itemek:", value = "0")
    profilembed.add_field(name = "Munka:", value = "Munkanélküli")
    await ctx.send(embed=profilembed)

#rp

@client.command()
async def hug(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    hugembed = discord.Embed(title = f"{ctx.author.name} megölelte {member.name} felhasználót.", description = "", color = discord.Colour.green())
    hugembed.set_image(url="https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif")
    await ctx.send(embed=hugembed)


@client.command()
async def kiss(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    kissembed = discord.Embed(title = f"{ctx.author.name} megcsókolta {member.name} felhasználót!", description = "", color = discord.Colour.green())
    kissembed.set_image(url="https://media1.giphy.com/media/FqBTvSNjNzeZG/giphy.gif")
    await ctx.send(embed=kissembed)

@client.command()
async def headpat(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    headembed = discord.Embed(title = f"{ctx.author.name} megsimogatta {member.name} felhasználót.", description = "", color = discord.Colour.green())
    headembed.set_image(url="https://64.media.tumblr.com/a72dd82535f3e7accd827c202dacc09a/tumblr_pfyiqz0pFL1th206io1_640.gif")
    await ctx.send(embed=headembed)

@client.command()
async def cry(ctx):
    cryembed = discord.Embed(title = f"{ctx.author.name} elsírta magát. :(", description = "", color = discord.Colour.green())
    cryembed.set_image(url="https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif")
    await ctx.send(embed=cryembed)

@client.command()
async def laugh(ctx):
    lembed = discord.Embed(title = f"{ctx.author.name} épp nevet. :D ", description = "", color = discord.Colour.green())
    lembed.set_image(url="https://media.tenor.com/images/a2741132a4f7ddf637513737364d87d9/tenor.gif")
    await ctx.send(embed=lembed)

@client.command()
async def laughat(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    laembed = discord.Embed(title = f"{ctx.author.name} kinevette {member.name} felhasználót. :d ", description = "", color = discord.Colour.green())
    laembed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/619/204/8c0.gif")
    await ctx.send(embed=laembed)

@client.command()
async def shoot(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    shembed = discord.Embed(title = f"{ctx.author.name} lelőtte {member.name} felhasználót. ", description = "", color = discord.Colour.green())
    shembed.set_image(url="https://cdn.discordapp.com/attachments/775840670069030952/775840696170577940/tenor.gif")
    await ctx.send(embed=shembed)

@client.command()
async def bite(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    bitembed = discord.Embed(title = f"{ctx.author.name} megharapta {member.name} felhasználót. ", description = "", color = discord.Colour.green())
    bitembed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776924443322220624/tenor.gif")
    await ctx.send(embed=bitembed)

@client.command()
async def smack(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    smaembed = discord.Embed(title = f"{ctx.author.name} megütötte {member.name} felhasználót. ", description = "", color = discord.Colour.green())
    smaembed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776935394695577610/tenor.gif")
    await ctx.send(embed=smaembed)

@client.command()
async def slap(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    slambed = discord.Embed(title = f"{ctx.author.name} megpofozta {member.name} felhasználót. ", description = "", color = discord.Colour.green())
    slambed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776935679791202304/tenor_1.gif")
    await ctx.send(embed=slambed)


@client.command()
async def fuck(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    fembed = discord.Embed(title = f"{ctx.author.name} az gecire kanos!! Én vigyáznék vele...", description = "", color = discord.Colour.green())
    fembed.set_image(url="https://i.imgur.com/LxG1qGl.gif")
    await ctx.send(embed=fembed)


@client.command()
async def blush(ctx):
    blembed = discord.Embed(title = f"{ctx.author.name} elpirult.", description = "", color = discord.Colour.green())
    blembed.set_image(url="https://i.pinimg.com/originals/ac/2f/1f/ac2f1f727d4d96a6a7c4fb5ae5a41cf0.gif")
    await ctx.send(embed=blembed)




##ekonómia rendszer


#client run function, token herokun belül van setupolva
client.run(os.environ['token'])
