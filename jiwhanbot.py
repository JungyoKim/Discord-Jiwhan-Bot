from urllib.request import urlopen
from bs4 import BeautifulSoup
import discord
import asyncio

client = discord.Client()

token = "ODg0OTY4MjY4NjM5NjQxNjMw.YTgM7Q.wvVkkeI8YwcMdFHw5hk8DTR0T0s"

html = urlopen("https://api.hangang.msub.kr/")
print (html)

@client.event
async def on_ready():

    print(client.user.name)
    print('지환봇이 작동중입니다')
    game = discord.Game("흠흠")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "뭐하고싶어?":
        await message.channel.send("https://bit.ly/2WXW5eq")
        await message.channel.send("를 보고싶어")
    if message.content == "나랑친해?":
        await message.channel.send("XX",tts=True)
    if message.content == "가장좋아하는 숫자는?":
        await message.channel.send("13",tts=True)
    if message.content == "시간표":
        await message.channel.send("https://bit.ly/3kXYL3U")

@client.event
async def on_message_delete(message):
	await message.channel.send("메세지 삭제 감지(" + str(message.author) + "): " + message.content)
	return

client.run(token)
