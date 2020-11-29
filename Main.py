import discord
import random
import asyncio
import os
import json 
import dbl
import youtube_dl
from discord.ext import commands, tasks
from PIL import Image, ImageEnhance
from io import BytesIO
from discord.voice_client import VoiceClient
from random import seed
from random import randint
from random import choice


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



client = commands.Bot(command_prefix = "r!")
client.remove_command("help")

animes = ["Re:ZERO Starting Life in Another World", "Darling in the Franxx", "The Rising of the Shield Hero", "Kill la Kill", "Mob Psycho 100", "Mob Psycho 100 S2", "Re:ZERO Starting Life in Another World S2", "One Punch Man", "One Punch Man S2", "Overlord", "Overlord S2", "Overlord S3", "Satsuriku no Tenshi", "Sakura-sou no Pet na Kanojo", "Youjo Senki", "Uzaki-chan Wants to Hang Out!", "Tejina-senpai", "That Time I Got Reincarnated as a Slime", "Mekakucity Actors", "Tower of god", "Black Rock Shooter", "	Chuunibyou demo Koi ga Shitai!", "Re:zero Memory snow OVA", "Konosuba", "Konosuba S2", "Mushikago no Cagaster", "Neon Genesis Evangelion"
, "Shokugeki no Souma(Foodwars!)", "Shokugeki no Souma(Foodwars!) S2", "Shokugeki no Souma(Foodwars!) S3", "Shokugeki no Souma(Foodwars!) S4", "Shokugeki no Souma(Foodwars!) S5", "Attack on titan", "Attack on titan S2", "Attack on titan S3"]

pps = ["8D", "8=D", "8==D", "8===D", "8D", "8=D", "8==D", "8===D", "8====D", "8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D",  "8=====D", "8======D", "8=======D",  "8=====D", "8======D", "8=======D",  "8=====D", "8======D", "8=======D", "8========D", "8========D", "8=========D", "8==========D", "8===========D", "8=======================================================D" , "Úristen! Ez akkora hogy ki sem tudom írni..."]
fights = ["kiütötte", "(e)t kiütötte", "megfejelte", "(e)t megfejelte", "leütötte", "(e)t leütötte"]
queue = []


class TopGG(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc1MzY0NTY5NDc5OTE4Mzk2MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA0OTU3NTAyfQ.mb55JBnvLGhsoFxpBjzynIrzxX8GM4v9jMvCdmkt8kY' # ez a dbl token nem a dc s token, semmire nem mész vele :)
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True) 

    async def on_guild_post():
        print("Server count posted successfully")

def setup(bot):
    bot.add_cog(TopGG(bot))

async def status_task():
        await client.change_presence(activity=discord.Game(name="r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name=f"{len(client.guilds)} szerveren van bent! │ r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Mehetnek a karácsonyi zenék! │ r!info"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="r!parancsok"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Szavazni az r!vote al lehet! │ r!info  "))
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
    setup()
    client.loop.create_task(status_task())

        
  
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('A Rembot még bétában van tehát akadhatnak bugok, illetve meg kevés command van csak! ```Fontosabb dolgok hogy elkezd használni a botot: Prefix: r!, infó parancs: r!info, Parancslista: r!parancsok```')
        break

@client.command()
async def info(ctx):
    iembed = discord.Embed(title = "Rembot infók", description = "Egy anime köré épitett bot, de tud sok mást is! Például képmanipulálás, moderálás, és még sok mást is!!", color = discord.Colour.blue())
    iembed.add_field(name = "Készitő:", value = "Volutedberet", inline = True)
    iembed.add_field(name = "Nyelv:", value = "python", inline = True)
    iembed.add_field(name = "Fontosabb infók:", value = "prefix: r!, parancslista: r!parancsok", inline = True)
    iembed.add_field(name = "Support szerver", value = "[Invite](https://discord.gg/YDRRKQA)", inline = True)
    iembed.add_field(name = "Source code:", value = "[Github repo](https://github.com/volutedberet424/Rembotv2)", inline = True)
    iembed.add_field(name = "Invite a bothoz:", value = "[Invite](https://discord.com/api/oauth2/authorize?client_id=753645694799183963&permissions=8&scope=bot)", inline = True)
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
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    pfpembed = discord.Embed(title = f"{member.name} Profilképe", description = f"{member.mention}", color = discord.Colour.blue())
    pfpembed.set_image(url = member.avatar_url)
    pfpembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=pfpembed)


@client.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Jelenleg nem vagy egy voice csatornában!")
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


    gtemplate = Image.open("blank.png")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)    
    pfp = pfp.resize((300, 300))
    g1template = Image.open("rainbow.png")
    g1template = g1template.resize((300, 300))
    g1template.putalpha(1)


    gtemplate.paste(pfp, (950, 440))
    gtemplate.paste(g1template, (950, 440))

    gtemplate.save("gay.png")

    await ctx.send(file = discord.File("gay.png"))





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
    await ctx.send("-V0.1.2 Extra animés, képes parancsok, Illetve vote parancs mivel a bot felkerült Top.gg re.    ")

@client.command()
async def vote(ctx):
    await ctx.send("A botra itt tudsz szavazni hogy több emberhez eljusson: https://top.gg/bot/753645694799183963/vote . Minden szavazatot nagyra értékelek")

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
    aniembed.add_field(name = "Darling in the franx", value = "r!darling", inline = True)
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
    reembed.add_field(name = "ep25", value = "[Megtekintés](http://indavideo.hu/video/ReZero_kara_Hajimeru_Isekai_Seikatsu_-_25_Vege_)", inline = True)
    reembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    reembed.set_thumbnail(url = "https://i5.walmartimages.com/asr/033a9851-afd8-4f5e-a9be-35197e8e1974_1.b506d4333c1c4cb93ae8b519f23e52b5.jpeg")
    
    await ctx.send(embed=reembed)

@client.command()
async def rezeros2(ctx):
    re2embed = discord.Embed(title = "Re:ZERO Starting Life in Another World S2", description = "Ez az évad még jelenleg fut tehát új részek kikerülnek ide amikor kijönnek!", color = discord.Colour.blue())
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
async def darling(ctx):
    darembed = discord.Embed(title = "Darling in the franxx", description = "Sajnos nincs még második évad :(", color = discord.Colour.blue())
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
    await ctx.send(f"A válaszidőm:```{round(client.latency * 1000)}ms```")
    
@client.command()
async def servercount(ctx):
    await ctx.send(f"Jelenleg {len(client.guilds)} szerveren vagyok bent.")
        
@client.command()
async def howsimp(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
      
    simpembed = discord.Embed(title = "Simp mérő", description = "", color = discord.Colour.green())
    simpembed.add_field(name = "Simpség", value = f"{user.mention} az {random.randint(0,100)}% ban simp! 😞" , inline = True)
    simpembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=simpembed)

@client.command()
async def epikgamerrate(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
      
    gamembed = discord.Embed(title = "Gamerség mérő", description = "", color = discord.Colour.green())
    gamembed.add_field(name = "Epikus gamer ráta:", value = f"{user.mention} az {random.randint(0,100)}% ban epikus gamer! 😎" , inline = True)
    gamembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=gamembed)

@client.command()
async def howgay(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    gayembed = discord.Embed(title = "Melegség mérő", description = "", color = discord.Colour.green())
    gayembed.add_field(name = f"Melegség:", value = f"{user.mention} az {random.randint(0,100)}% ban meleg! 🏳️‍🌈", inline = True)
    gayembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=gayembed)

 

@client.command()
async def parancsok(ctx):
    embed = discord.Embed(title = "Parancsok", description = "A bot még bétában van tehát még lesznek parancsok. A bot prefixe: r! Jelenlegi parancsok száma: 44", color = discord.Colour.green())
    embed.add_field(name = "Teszt parancsok(2)", value = "ping, servercount", inline = True)
    embed.add_field(name = "Alap parancsok(12)", value = "twitter, info, vote, uwu, development, parancsok, invite, updateok, uptime, randomszám, avatar", inline = True)
    embed.add_field(name = "Moderátor parancsok(5)", value = "clear, kick, ban, slowmode, userinfo", inline = True)
    embed.add_field(name = "Funolós parancsok(6)", value = "votegay, howsimp, howgay, pp, epikgamerrate, fight", inline = True)
    embed.add_field(name = "Képes parancsok(5)", value = "makerem, pofon, szemét, kézfogás, hornyjail", inline = True)
    embed.add_field(name = "Animés parancsok(2)", value = "animeajánlás, watchanime(Animékhez hyperlinkeket biztosít)", inline = True)
    embed.add_field(name = "Roleplay(12)", value = "hug, kiss, headpat, cry, laugh, laughat, shoot, bite, slap, smack, blush, profil(Nincs még kész)", inline = True)
    embed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=embed)

@client.command()
async def animeajánlás(ctx):
    animeoutput = random.choice(animes)
    await ctx.send(animeoutput) 

@client.command()
async def pp(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    ppoutput = random.choice(pps)    
    ppembed = discord.Embed(title = "PP méret meghatározó", description = "", color = discord.Colour.green())
    ppembed.add_field(name = "PP méret:", value = f"{user.mention} pp je: {ppoutput} 😏", inline = True)
    ppembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=ppembed)


@client.command()
async def fight(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    fightoutput = random.choice(fights)    
    fightembed = discord.Embed(title = "Harctér", description = "", color = discord.Colour.green())
    fightembed.add_field(name = "harc:", value = f"{ctx.author.mention} {fightoutput} {user}", inline = True)
    fightembed.set_footer(icon_url = "https://cdn.discordapp.com/avatars/753645694799183963/bb546ed943c00348a3b43039efb6c138.webp?size=1024", text = "@Rembot")
    await ctx.send(embed=fightembed)

@client.command()
async def development(ctx):
    await ctx.send("A botot fejleszteni egy kis időbe telik, mivel jelenleg egyedül dolgozom a projecten. Amennyiben segiteni szeretnél a bot fejlesztésében, és ismered a pythont mint programozási nyelvet, akkor keresd meg a bot fejlesztőjét (Volutedberet#1663)!")

@client.command()
async def uwu(ctx):
    await ctx.send(f"{ctx.author.mention} UwU! :3")


@client.command()
async def twitter(ctx):
    await ctx.send("Amennyiben érdekel a bot fejlesztése akkor kövesd a twitteremet! Link: https://twitter.com/volutedberet")


@client.command()
async def lol(ctx):
    await ctx.channel.purge(limit = 1)
    await ctx.send("Mi volt ez a pusztító alpáriság?")

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount + 1)

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
    await ctx.send(f"Erre a csatornára slowmode lett rakva **{seconds}** másodpercre!")



@client.command()
async def profil(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    profilembed = discord.Embed(title = f"{member} profilja", description = f"{member} adatai. Még nem működik a profil, mivel még nincs kész a mentés rendszer! **Ez még csak egy concept hogy hogyan fog kinézni!**", color = discord.Colour.green())
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
    hugembed = discord.Embed(title = f"{ctx.author.name} megöleli {member.name} (e)t.", description = "", color = discord.Colour.green())
    hugembed.set_image(url="https://i.pinimg.com/originals/f2/80/5f/f2805f274471676c96aff2bc9fbedd70.gif")
    await ctx.send(embed=hugembed)


@client.command()
async def kiss(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    kissembed = discord.Embed(title = f"{ctx.author.name} megcsókolta {member.name} (e)t.", description = "", color = discord.Colour.green())
    kissembed.set_image(url="https://media1.giphy.com/media/FqBTvSNjNzeZG/giphy.gif")
    await ctx.send(embed=kissembed)

@client.command()
async def headpat(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    headembed = discord.Embed(title = f"{ctx.author.name} megsimogatta {member.name} (e)t.", description = "", color = discord.Colour.green())
    headembed.set_image(url="https://64.media.tumblr.com/a72dd82535f3e7accd827c202dacc09a/tumblr_pfyiqz0pFL1th206io1_640.gif")
    await ctx.send(embed=headembed)

@client.command()
async def cry(ctx):
    cryembed = discord.Embed(title = f"{ctx.author.name} elsírta magát :(", description = "", color = discord.Colour.green())
    cryembed.set_image(url="https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif")
    await ctx.send(embed=cryembed)

@client.command()
async def laugh(ctx):
    lembed = discord.Embed(title = f"{ctx.author.name} elnevette magát :D ", description = "", color = discord.Colour.green())
    lembed.set_image(url="https://media.tenor.com/images/a2741132a4f7ddf637513737364d87d9/tenor.gif")
    await ctx.send(embed=lembed)

@client.command()
async def laughat(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    laembed = discord.Embed(title = f"{ctx.author.name} kinevette {member.name} (e)t ", description = "", color = discord.Colour.green())
    laembed.set_image(url="https://i.kym-cdn.com/photos/images/original/000/619/204/8c0.gif")
    await ctx.send(embed=laembed)

@client.command()
async def shoot(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    shembed = discord.Embed(title = f"{ctx.author.name} lelőtte {member.name} (e)t ", description = "", color = discord.Colour.green())
    shembed.set_image(url="https://cdn.discordapp.com/attachments/775840670069030952/775840696170577940/tenor.gif")
    await ctx.send(embed=shembed)

@client.command()
async def bite(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    bitembed = discord.Embed(title = f"{ctx.author.name} megharapta {member.name} (e)t ", description = "", color = discord.Colour.green())
    bitembed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776924443322220624/tenor.gif")
    await ctx.send(embed=bitembed)

@client.command()
async def smack(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    smaembed = discord.Embed(title = f"{ctx.author.name} megütötte {member.name} (e)t ", description = "", color = discord.Colour.green())
    smaembed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776935394695577610/tenor.gif")
    await ctx.send(embed=smaembed)

@client.command()
async def slap(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    slambed = discord.Embed(title = f"{ctx.author.name} megpofozta {member.name} (e)t ", description = "", color = discord.Colour.green())
    slambed.set_image(url="https://cdn.discordapp.com/attachments/541982855639859201/776935679791202304/tenor_1.gif")
    await ctx.send(embed=slambed)


@client.command()
async def fuck(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    fembed = discord.Embed(title = f"{ctx.author.name} az gecire horny", description = "", color = discord.Colour.green())
    fembed.set_image(url="https://i.imgur.com/LxG1qGl.gif")
    await ctx.send(embed=fembed)


@client.command()
async def blush(ctx):
    blembed = discord.Embed(title = f"{ctx.author.name} elpirult", description = "", color = discord.Colour.green())
    blembed.set_image(url="https://i.pinimg.com/originals/ac/2f/1f/ac2f1f727d4d96a6a7c4fb5ae5a41cf0.gif")
    await ctx.send(embed=blembed)

#client run cuccos
client.run(os.environ['token'])