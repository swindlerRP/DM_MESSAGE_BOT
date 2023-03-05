import discord
import sys
from discord.ext import commands
import io
import aiohttp

bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Developed by: swindler#1337"))
    print("BOT ONLINE")

@bot.event
async def on_message(message):
    if message.content.startswith("!swindiv"):
        online_members = [member for member in message.guild.members if member.status == discord.Status.online] # Para mandar para todos os status dnd/idle/inv/off substitua a linha inteira por esse código: ## all_members = message.guild.members ##
        sent_to = []
        not_sent_to = []
        count = 0
        for member in online_members: # Caso tenha alterado o código acima, altere aqui também: ## for member in all_members: ##
            if member == bot.user:
                continue
            try:
                embed = discord.Embed(
                    title="title embed",
                    description=f"descripttion embed",
                    color=discord.Color.blue()
                )
                # ICONE
                embed.set_thumbnail(url="icon embed")
                # IMAGEM
                embed.set_image(url="image embed")
                await member.send("CONTENT MESSAGE", embed=embed)
                sent_to.append(member.name)
                count += 1
            except discord.Forbidden:
                not_sent_to = [name.encode('ascii', 'ignore').decode() for name in not_sent_to]
            except discord.errors.HTTPException as e:
                if e.code == 50007:
                    not_sent_to = [name.encode('ascii', 'ignore').decode() for name in not_sent_to]
                else:
                    raise e
        print(f"Foram enviadas {count} mensagens.")
        gif_url = "https://media.discordapp.net/attachments/973693143830638642/1079277534182654053/giphy.gif"
        async with aiohttp.ClientSession() as session:
             async with session.get(gif_url) as image:
                 await message.channel.send(f"As mensagens foram enviadas com sucesso para {count} pessoa(s)!\nNão foi possível enviar a mensagem para {len(not_sent_to)} usuários.\n**Flash Follow Corp.**\n", file=discord.File(io.BytesIO(await image.read()), 'giphy.gif'))
bot.run("TOKEN_BOT") # PUT YOUR TOKEN BOT
