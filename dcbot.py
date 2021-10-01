# 초대링크 : https//discord.com/api/oauth2/authorize?client_id=871343528821784646&permissions=8&scope=bot

#if isinstance(message.channel, discord.abc.PrivateChannel) and message.author.id != "봇ID":
#
#        await client.get_user("자신아이디").send(message.author.name + "(" + str(message.author.id) + "): " + message.content)

"[[[[[[[[[[ 시스템 설정 ]]]]]]]]]]"

import discord
import asyncio
import random
import string
from discord import flags
from discord import channel
from discord import member
from discord import role
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from bs4 import BeautifulSoup
import requests
import urllib
import time
from datetime import datetime
import os
import json 
#from pymongo import MongoClient
#from dislash import SelectMenu, SelectOption
import os.path                                         # 메소드 call을 위한 module불러오기


접두 = '글린아 '


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=[접두], intents=intents)

#token = 

#token = 

admin = [760688241447141395, 824243275975360562]

piglin = 824243275975360562

피글린 = client.get_user(824243275975360562)

print(피글린)

뮤트 = []

useguild = [868175022953463868]

빨강 = 0xFF0000
주황 = 0xFF8C00
노랑 = 0xFFDC37
초록 = 0x00FC08
파랑 = 0x006AFF
보라 = 0x9932CC
분홍 = 0xFF00FF
검정 = 0x000000
민트 = 0x00FFDD
하늘 = 0x3CFBFF
갈색 = 0x8B4F1D
회색 = 0x828282
남색 = 0x3700FF

file_path = "D:/python/discordbot/출첵.json"

#open_file = open("C:/doit/새파일.txt", 'w')

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 시작됨')
    game = discord.Game('피글린 봇이 켜졌습니다!')
    await client.change_presence(status=discord.Status.online, activity=game)
    for i in range(0, 50):
        time.sleep(0.1)
    game = discord.Game('"' + 접두 + '도움말" 이라고 말해주세요!')
    await client.change_presence(status=discord.Status.online, activity=game)
    client.remove_command('help')

"[[[[[[[[[[ 기본 기능 ]]]]]]]]]]"

Location = 'D:/python/discordbot/log/' #파일 위치

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("잉? 뭔말이에요?")
    today = datetime.today().strftime("%Y_%m_%d")
    now = datetime.now()
    file = Location + today + '.txt'
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if os.path.isfile(file):
            f = open(file, 'a', encoding='utf-8')
            f.write(f'\n[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 {ctx.guild}에서 알수없는 명령어를 사용했습니다.')
            f.close()
        else:
            f = open(file, 'w', encoding='utf-8')
            f.write(f'[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 {ctx.guild}에서 알수없는 명령어를 사용했습니다.')
            f.close()
    else:
        if os.path.isfile(file):
            f = open(file, 'a', encoding='utf-8')
            f.write(f'\n[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 DM에서 알수없는 명령어를 사용했습니다.')
            f.close()
        else:
            f = open(file, 'w', encoding='utf-8')
            f.write(f'[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 DM에서 알수없는 명령어를 사용했습니다.')
            f.close()

    raise error
    

@client.event
async def on_command(ctx):
    today = datetime.today().strftime("%Y_%m_%d")
    now = datetime.now()
    file = Location + today + '.txt'
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if os.path.isfile(file):
            f = open(file, 'a', encoding='utf-8')
            f.write(f'\n[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 {ctx.guild}에서 {ctx.command} 명령어를 사용했습니다.')
            f.close()
        else:
            f = open(file, 'w', encoding='utf-8')
            f.write(f'[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 {ctx.guild}에서 {ctx.command} 명령어를 사용했습니다.')
            f.close()
    else:
        if os.path.isfile(file):
            f = open(file, 'a', encoding='utf-8')
            f.write(f'\n[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 DM에서 {ctx.command} 명령어를 사용했습니다.')
            f.close()
        else:
            f = open(file, 'w', encoding='utf-8')
            f.write(f'[ {now.hour}:{now.minute}:{now.second} ] {ctx.author}님이 DM에서 {ctx.command} 명령어를 사용했습니다.')
            f.close()


"[[[[[[[[[[ 자유 기능 ]]]]]]]]]]"


@client.event
async def on_message(message):
    await client.process_commands(message)
    if isinstance(message.channel, discord.abc.PrivateChannel) != True:
        if True:
            if message.content == "피글린":
                await message.channel.send("일해라!!")
            if message.content == "LOL":
                await message.channel.send("왜 뭐가 웃긴데 나도 좀 보자;;")
            if message.content == "임베드 생성":
                embed=discord.Embed(title="title", url="https://www.naver.com/", description="description", color=빨강)
                embed.set_author(name="author name", url="https://www.naver.com/", icon_url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
                embed.add_field(name="First Field name", value="First Field value", inline=True)
                embed.add_field(name="Second Field name", value="Second Field value", inline=True)
                embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
                msg = '''```py
embed=discord.Embed(title="title", url="https://www.naver.com/", description="description", color=0xFF0000)
embed.set_author(name="author name", url="https://www.naver.com/", icon_url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
embed.add_field(name="First Field name", value="First Field value", inline=True)
embed.add_field(name="Second Field name", value="Second Field value", inline=True)
embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/attachments/868200965826805760/875342659630288906/image.webp")
await ctx.send(embed=embed)
```'''
                await message.channel.send(embed=embed, content = msg)
            if message.content == '글린아':
                await message.channel.send("넹? 부르셨어요? 혹시 도움이 필요하신거면,\n`글린아 도움말` 이라고 말해보세요!")
            if message.content == "여가부":
                await message.channel.send("여성개좆부")
            if message.content == "냥냥":
                await message.delete()
                await message.channel.send("😺")
            if message.content == "돼지새끼":
                await message.add_reaction("🤔")
            if check_bad_word(message.content):
                if isinstance(message.channel, discord.abc.PrivateChannel) != True:
                    if message.guild.id in useguild:
                        if message.author != client.user:
                            await message.delete()
                            return
            if message.author.id in 뮤트:
                await message.delete()
            if message.content == "릴마":
                await message.channel.send("지구 최강 멍청이")
            if message.content == "샍":
                await message.add_reaction("<:sandz:875738701089632266>")
                await message.add_reaction("<a:sandz:875741528516079616>")
                #await message.channel.send("<:sandz:875738701089632266> <a:sandz:875741528516079616> ")

def check_bad_word(c):
    bad = ['><<>', '><']
    for i in bad:
        if i in c:
            return True
    return False


        
@client.command()
async def 핑(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            await ctx.send('퐁! {0}'.format(round(client.latency, 1)))

@client.command(aliases=['골라줘', 'choise'])
async def 골라(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            await ctx.send('퐁! {0}'.format(round(client.latency, 1)))

@client.command(aliases=['Hi'])
async def 안녕(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send('안녕하세요! 오늘 기분이 좋아보이네요!')

@client.command(aliases=['꿀', '짖어', 'Rnf'])
async def 울어(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            await ctx.send('내가 울으라고 해서 울거 같ㄴ...꿀')

@client.command()
async def 빵켓(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            await ctx.channel.send("천재(가 아니고 바보 멍청이 Rust, Ts 망해라)")

###############################################

list1 = ["기능", "대화", "기타"]
list2 = ["도움말", "따라해", "~~코로나19~~\n( 오류로 인해 임시 중단 )", "랜덤사람대가리", "핑"]
list3 = ["안녕", "뭐해", "사랑해", "울어"]
list4 = ["빵켓",  "얼애", "초대",  "릴마", "카그", "크레파스", "크리", "금이", "디온", "개발자", "피글린"]

@client.command(aliases=['ehdnaakf', '헬프', '도움'])
async def 도움말(ctx, num1 = '0', num2 = '0'):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            if num1 == '0':
                help = discord.Embed(title="피글린 봇 사용 설명서", description="", color=파랑)
                co = 0
                for i in list1:
                    co = co + 1
                    출력 = ''
                    if co == 1:
                        for l2 in list2:
                            출력 = 출력 + 접두 + l2 + '\n\n'
                        help.add_field(name=i + '\n', value=출력, inline=False)
                    elif co == 2:
                        for l2 in list3:
                            출력 = 출력 + 접두 + l2 + '\n\n'
                        help.add_field(name=i + '\n', value=출력, inline=False)
                    elif co == 3:
                        for l2 in list4:
                            출력 = 출력 + 접두 + l2 + '\n\n'
                        help.add_field(name=i + '\n', value=출력, inline=False)
                
                help.set_footer(text="\n'" + 접두 + " 도움말 명령어' 로 상세 설명을 보세요!")
                await ctx.channel.send(embed=help)

            elif num1 == '자동응답':
                embed = discord.Embed(title="1. 자동 응답 기능", description="""
                1. 피글린
                
                2. LOL
                
                3. 여가부
                
                4. 냥냥
                
                5. 돼지새끼
                
                6. 샍
                """, color=파랑)
                embed.set_footer(text="앞에 접두어 `" + 접두 + "` 를 붙이지 않고 그냥 나오는데로 쓰세요!")
                await ctx.channel.send(embed=embed)

            elif num1 == '명령어':
                if num2 == '0':
                    embed = discord.Embed(title="2. 명령어", description="", color=파랑)
                    cmdl = ""
                    cnt = 0
                    foot1 = ''
                    for i in list1:
                        cnt = cnt + 1
                        ctn출력 = str(cnt)
                        msg4 = ctn출력 + ". " + i
                        embed.add_field(name=msg4, value="ㅤ", inline=False)
                        foot1 = foot1 + i + ", "
                    embed.set_footer(text="'" + 접두 + "도움말 명령어 [" + foot1 + "]' 로 상세 설명을 보세요!")
                    await ctx.channel.send(embed=embed)
                elif num2 == '기능':
                    embed = discord.Embed(title="2. 명령어 > 기능", description="", color=파랑)
                    cnt = 0
                    for i in list2:
                        cnt = cnt + 1
                        ctn출력 = str(cnt)
                        msg4 = ctn출력 + ". " + 접두 + i
                        embed.add_field(name=msg4, value="ㅤ", inline=False)
                    embed.set_footer(text="명령어 > 기능")
                    await ctx.channel.send(embed=embed)
                elif num2 == '대화':
                    embed = discord.Embed(title="2. 명령어 > 대화", description="", color=파랑)
                    cnt = 0
                    for i in list3:
                        cnt = cnt + 1
                        ctn출력 = str(cnt)
                        msg4 = ctn출력 + ". " + 접두 + i
                        embed.add_field(name=msg4, value="ㅤ", inline=False)
                    embed.set_footer(text="명령어 > 대화")
                    await ctx.channel.send(embed=embed)
                elif num2 == '기타':
                    embed = discord.Embed(title="2. 명령어 > 기타", description="", color=파랑)
                    cnt = 0
                    for i in list4:
                        cnt = cnt + 1
                        ctn출력 = str(cnt)
                        msg4 = ctn출력 + ". " + 접두 + i
                        embed.add_field(name=msg4, value="ㅤ", inline=False)
                    embed.set_footer(text="명령어 > 기타")
                    await ctx.channel.send(embed=embed)


###############################################

@client.command(aliases=['믿어조', '좀_믿어조', 'please believe me'])
async def please_believe_me(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send('`"`')

@client.command(aliases=['피글린', '글린', '피1234글5린'])
async def pig_lin(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send('개발자')

@client.command(aliases=['개발', '개발자', '개빌언어'])
async def making(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send('개발자 : 피글린\n개발 언어 : discord.py')

"""
@client.command(aliases=['씨티캡', '윤재준', '고자준', '고자', '도시모자', '시티캡', '맞춤법', '패드립', '씨발티캡', '하이서율', '하이서율TV', '서율', '서율이'])
async def citycap(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        
        with open('고자준1.jpg', 'rb') as f:
            picture1 = discord.File(f)
        
        with open('고자준2.jpg', 'rb') as f:
            picture2 = discord.File(f)
             
        with open('고자준3.jpg', 'rb') as f:
            picture3 = discord.File(f)
        
        await ctx.send(content='패드립 겁나 많이 하면서 야||동||도 지 친구 수보다 더 많이 보고 맞춤법 겁나 못하는 잼민이 https://youtu.be/di2Eveaevz8', file=picture1)
        await ctx.send(file=picture2)
        await ctx.send(file=picture3)
"""

@client.command()
async def 따라해(ctx, *, arg):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            if check_bad_word(arg): return
            embed = discord.Embed(title=arg, description="따라하라고 해서 따라한것 뿐이에요!", color=파랑)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)
            return

@client.command(aliases=['링크', '초대링크', 'invite'])
async def 초대(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=871343528821784646&permissions=8&scope=bot")

@client.command(aliases=['lilmas', '리일마아', '민재'])
async def 릴마(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("귀요미><")

        with open('D:/python/img/릴마1.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

@client.command(aliases=['KAG', '캌', 'kag'])
async def 카그(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("카그랑 안놀아 ;-;")

bbang_cat = False

뭐해_사용중 = ""

뭐해_마지막 = 0

@client.command(aliases=['뭐행', '뭐행?', '뭐해?'])
async def 뭐해(ctx):
    global bbang_cat
    global 뭐해_사용중
    global 뭐해_마지막
    if bbang_cat == False:
        if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
            print(str(ctx.author) + '님이 `' + 접두 + '뭐해` 명령어를 사용했어요!')
            뭐해_사용중 = str(ctx.author)
            bbang_cat = True
            대답리스트 = ["얼불춤 하고있어요! (미더덕)", "전 게임 커뮤니티를 성장시킬 방법을 생각하고 있어요! (미더덕)", "그걸 왜 물어봐;-; (키위)", "그냥 폰해 (키위)", "아니 (키위)", "몰라 (키위)", "뭔소리야;-; (키위)", "뭐 이 놈아 (얼애)", "흠 (신비)", "널 생각하고 있어 (카그)", "너의 얼굴 (카그)", "피글린이 업그레이드 시키는 중이야 (캐롤조아)", "대답하는중이야 (캐롤조아)", "식사중 (하선)", "똥싸는중 (하선)", "릴마랑 놀고있어요! (릴마)", "크레파스 욕하고 있어요 '글린아 크레파스' 를 쳐보세요! (릴마)"]
            대답리스트1 = ["크레파스 욕하고 있어요 '글린아 크레파스' 를 쳐보세요! (릴마)"]
            c = 0
            for i in 대답리스트:
                c = c + 1
            
            a = random.randrange(1,c)
            if a == 뭐해_마지막:
                while a == 뭐해_마지막:
                    a = random.randrange(1,c)
            else:
                pass
            출력 = ""
            count1 = 0
            for i in 대답리스트:
                count1 = count1 + 1
                if count1 == a:
                    출력 = await ctx.send(i + " (30초 후에 상태메시지가 리셋됩니다)")
                    game = discord.Game(i)
                    await client.change_presence(status=discord.Status.online, activity=game)
                    for l in range(0, 30):
                        time.sleep(1)
                        t = 30-l
                        timere = str(t)
                        await 출력.edit(content = i + " (" + timere + "초 후에 상태메시지가 리셋됩니다)")
                    game = discord.Game('"' + 접두 + '도움말" 이라고 말해주세요!')
                    await client.change_presence(status=discord.Status.online, activity=game)
                    await 출력.edit(content = i)
                    bbang_cat = False
                else:
                    pass
            
            bbang_cat = False
    
    else:
        await ctx.send("이 명령어를 " + 뭐해_사용중 + "님이 사용중입니다. (계속 이런 오류가 지속된다면, piglin#7071로 문의주세요!)")
        pass



#            await ctx.author.send("E")
#            game = discord.Game('식사중')
#            await client.change_presence(status=discord.Status.online, activity=game)
#            time.sleep(10)
#            game = discord.Game('"' + 접두 + '도움말" 이라고 말해주세요!')
#            await client.change_presence(status=discord.Status.online, activity=gam
        

@client.command()
async def 코로나19(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.author.send("`" + 접두 + "코로나19` 명령어는 오류로 인해 사용이 불가능합니다!")

@client.command(aliases=['얼음애플', '얼플', '얼음사과'])
async def 얼애(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("얼애 구독자 100명 축하해\nhttps://www.youtube.com/channel/UCOEwyeWz_rle_1rVqWD8SxQ")

#============================================#

@client.command(aliases=['콜라', '육회', '케잌으'])
async def cola(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == True:
        await ctx.send("당신은 이스터 에그를 발견하셨습니다! 이 메시지를 피글린에게 DM으로 전송하면 GC서버 `20 GCM`을 드립니다.\nhttps://discord.gg/m6hbgyFx98")
        #await 피글린.send(str(ctx.author) + ' 님이 이스터 에그 발견!')
    else:
        await ctx.send("잉? 뭔말이에요?")

#============================================#

@client.command()
async def 디온(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("노란안경쓴 민트머리")

@client.command()
async def 크리(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("스탈\n||엌||\nhttp://watermelon.dcserv.kro.kr/")

@client.command()
async def 금이(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send("골드이에!! <a:gold:884785105804087327> ")

@client.command()
async def 크레파스(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        await ctx.send('패드립 잼민이')

        with open('D:/python/img/크레파스_패드립.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

@client.command()
async def 불코로나19불(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, "html.parser")

            datecr = soup.find('span', {'class': 't_date'}) #기준날짜
            #print(f'기준일: {datecr.string}')

            totalcovid = soup.select('dd.ca_value')[0].text #누적 확진자수
            #print(f'누적 확진자: {totalcovid} 명')

            todaytotalcovid = soup.select('p.inner_value')[0].text #당일 확진자수 소계
            #print(f'확진자 소계: {todaytotalcovid} 명')

            todaydomecovid = soup.select('p.inner_value')[1].text #당일 국내발생 확진자수
            #print(f'국내발생: {todaydomecovid} 명')

            todayforecovid = soup.select('p.inner_value')[2].text #당일 해외유입 확진자수
            #print(f'해외유입: {todayforecovid} 명')

            totalca = soup.select('dd.ca_value')[2].text #누적 격리해제
            #print(f'누적 격리해제: {totalca} 명')

            todayca = soup.select('span.txt_ntc')[0].text #당일 격리해제
            #print(f'격리해제: {todayca} 명')

            totalcaing = soup.select('dd.ca_value')[4].text #누적 격리중
            #print(f'누적 격리중: {totalcaing}')

            todaycaing = soup.select('span.txt_ntc')[1].text #당일 격리중
            #print(f'격리중: {todaycaing} 명')

            totaldead = soup.select('dd.ca_value')[6].text #누적 사망자
            #print(f'누적 사망자: {totaldead} 명')

            todaydead = soup.select('span.txt_ntc')[2].text #당일 사망자
            #print(f'사망자: {todaydead} 명')

            covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=회색)
            covidembed.add_field(name='🚑 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                        f'\n\n⛩ 국내발생: {todaydomecovid} 명\n✈ 해외유입: {todayforecovid} 명', inline=False)
            covidembed.add_field(name='🏠 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
            covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
            covidembed.set_footer(text=datecr.string)
            await ctx.channel.send(embed=covidembed)


@client.command()
async def 사랑해(ctx):
    await ctx.send("헋 저두요..!")

@client.command()
async def 랜덤사람대가리(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if True:
            embed = discord.Embed(title="랜덤한 사람 대가리", description="초상권이 없는 합성 사진입니다", color=파랑)
            embed.set_thumbnail(url="http://www.thispersondoesnotexist.com/image")
            await ctx.send(embed=embed)

@client.command()
async def 불니트로불(ctx, count = 10):
    await ctx.message.delete()
    for l in range(0, count):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            Nitro = 'https://discord.gift/' + ranNitro
        await ctx.author.send(Nitro)
    await ctx.author.send('혹시 진짜 선물이 나왔나요?')


"[[[[[[[[[[ GC서버 관리자 기능 ]]]]]]]]]]"


@client.command(aliases=['만들어', '제작', 'make'])
@commands.has_guild_permissions(kick_members=True)
async def create(ctx, *, name):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            #if ctx.guild_permissions.kick_members:
            #if ctx.author.id in admin:
            await ctx.send('만드는중입니다!')
            await ctx.guild.create_category(name)
            category = discord.utils.get(ctx.guild.categories, name=name)
            await ctx.guild.create_text_channel('💬ㅣ채팅ㅣchatting', category=category)
            await ctx.guild.create_text_channel('🌐ㅣ같이해요ㅣtogether', category=category)
            await ctx.guild.create_voice_channel('📞ㅣ보이스채팅ㅣvoice', category=category)
            ch1n = '💬ㅣ채팅ㅣchatting'
            ch1 = discord.utils.get(ctx.guild.text_channels, name=ch1n, category=category)
            ch2n = '🌐ㅣ같이해요ㅣtogether'
            ch2 = discord.utils.get(ctx.guild.text_channels, name=ch2n, category=category)
            ch3n = '📞ㅣ보이스채팅ㅣvoice'
            ch3 = discord.utils.get(ctx.guild.voice_channels, name=ch3n, category=category)
            ro1 = ctx.guild.get_role(868175381230944267)
            ro2 = ctx.guild.get_role(868175984422191157)
            ro3 = ctx.guild.get_role(868177254730051654)
            await ch1.set_permissions(ctx.guild.default_role, read_messages=False)
            await ch1.set_permissions(ro1, read_messages=True)
            await ch1.set_permissions(ro2, read_messages=True)
            await ch1.set_permissions(ro3, read_messages=True)
            await ch2.set_permissions(ctx.guild.default_role, read_messages=False)
            await ch2.set_permissions(ro1, read_messages=True)
            await ch2.set_permissions(ro2, read_messages=True)
            await ch2.set_permissions(ro3, read_messages=True)
            await ch3.set_permissions(ctx.guild.default_role, read_messages=False)
            await ch3.set_permissions(ro1, read_messages=True)
            await ch3.set_permissions(ro2, read_messages=True)
            await ch3.set_permissions(ro3, read_messages=True)
            text_channel = client.get_channel(ch1.id)
            msg = '만들었습니다 ( 바로가기 : {0.mention} )'.format(text_channel)
            await ctx.send(msg)

@client.command(aliases=['연합', '연합제작', '연합생성'])
@commands.has_guild_permissions(kick_members=True)
async def unite(ctx, user : discord.Member, *, name):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            await ctx.send('만드는중입니다!')
            category = discord.utils.get(ctx.guild.categories, name='연합서버ㅣServer Unite')
            ch = await ctx.guild.create_text_channel(name, category=category)
            ro1 = ctx.guild.get_role(868175381230944267)
            ro2 = ctx.guild.get_role(868175984422191157)
            ro3 = ctx.guild.get_role(868177254730051654)
            await ch.set_permissions(ctx.guild.default_role, read_messages=False)
            await ch.set_permissions(ro1, read_messages=True, send_messages=False)
            await ch.set_permissions(ro2, read_messages=True, send_messages=True)
            await ch.set_permissions(ro3, read_messages=True, send_messages=True)
            await ch.set_permissions(user, read_messages=True, send_messages=True)
            text_channel = client.get_channel(ch.id)
            msg = '만들었습니다 ( 바로가기 : {0.mention} )'.format(text_channel)
            await ctx.send(msg)


@client.command()
@commands.has_guild_permissions(kick_members=True)
async def 삭제(ctx, id):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            await ctx.send('삭제중입니다!')
            id=int(id)
            category = discord.utils.get(ctx.guild.categories, id=id)
            ch1n = '💬ㅣ채팅ㅣchatting'
            ch1 = discord.utils.get(ctx.guild.text_channels, name=ch1n, category=category)
            ch2n = '🌐ㅣ같이해요ㅣtogether'
            ch2 = discord.utils.get(ctx.guild.text_channels, name=ch2n, category=category)
            ch3n = '📞ㅣ보이스채팅ㅣvoice'
            ch3 = discord.utils.get(ctx.guild.voice_channels, name=ch3n, category=category)
            await ch1.delete()
            await ch2.delete()
            await ch3.delete()
            await category.delete()
            await ctx.send('삭제 완료했습니다!')

@client.command(aliases=['불영어로불'])
@commands.has_guild_permissions(kick_members=True)
async def TO_ENGLISH(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            a = [868175304454197269, 868201526773035080, 868200757046951937, 868564704384139274, 875041000060489768, 882140550692745266, 884035758372044850]
            for i in ctx.guild.categories:
                if i.id in a:
                    pass
                else:
                    try:
                        ch1n = '💬ㅣ채팅'
                        ch1 = discord.utils.get(ctx.guild.text_channels, name=ch1n, category=i)
                        await ch1.edit(name='💬ㅣ채팅ㅣchatting',reason='영어로 번역')
                        ch2n = '🌐ㅣ같이해요'
                        ch2 = discord.utils.get(ctx.guild.text_channels, name=ch2n, category=i)
                        await ch2.edit(name='🌐ㅣ같이해요ㅣtogether',reason='영어로 번역')
                        ch3n = '📞ㅣ보이스채팅'
                        ch3 = discord.utils.get(ctx.guild.voice_channels, name=ch3n, category=i)
                        await ch3.edit(name='📞ㅣ보이스채팅ㅣvoice',reason='영어로 번역')
                    except:
                        pass


@client.command()
@commands.has_guild_permissions(kick_members=True)
async def 링크정리(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            await ctx.send('OK')
            #await ctx.channel.purge(limit=10000)
            ctgr = discord.utils.get(ctx.guild.categories, name="공지")
            ch1 = discord.utils.get(ctx.guild.text_channels, name="🔗ㅣ바로가기", category=ctgr)
            a = [868175304454197269, 868201526773035080, 868200757046951937, 868564704384139274, 875041000060489768, 882140550692745266, 884035758372044850]
            출력 = ""
            for i in ctx.guild.categories:
                if i.id in a:
                    pass
                else:
                    ch11n = '💬ㅣ채팅ㅣchatting'
                    ch11 = discord.utils.get(ctx.guild.text_channels, name=ch11n, category=i)
                    text_channel = client.get_channel(ch11.id)
                    출력 = 출력 + '> {0} : {1.mention} \n\n'.format(i, text_channel)
            await ctx.send(출력)

@client.command()
@commands.has_guild_permissions(kick_members=True)
async def 클리어(ctx, count = 10):
    if True:
        await ctx.channel.purge(limit=count)

@client.command()
@commands.has_guild_permissions(kick_members=True)
async def 공지역할지급(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            role = ctx.guild.get_role(878588753143267358)
            for i in ctx.guild.members:
                try:
                    await i.add_roles(role)
                    await ctx.author.send(i)
                except:
                    pass

@client.command(aliases=['슬로우모드'])
@commands.has_guild_permissions(kick_members=True)
async def slow_mode(ctx, seconds: int):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
        #if True:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"이제 이 채널은 슬로우 모드 딜레이가 {seconds} 초입니다\nSet the slowmode delay in this channel to {seconds} seconds!")

@client.command()
@commands.has_guild_permissions(kick_members=True)
async def 공지(ctx, *, msg):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
        if ctx.guild.id in useguild:
            await ctx.message.delete()
            await ctx.send(embed=discord.Embed(title="공지", description=msg, color=0x396CEC).set_footer(text=ctx.author, icon_url=ctx.author.avatar_url))


"[[[[[[[[[[ 봇 관리자 기능 ]]]]]]]]]]"

@client.command()
async def 글린공지(ctx, *, msg = "(내용없음)"):
    if ctx.author.id in admin:
        if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
            if ctx.guild.id in useguild:
                for guild in client.guilds:
                    for channel in guild.text_channels:
                        if channel.topic == "-글린공지":
                            await channel.send(embed=discord.Embed(title="공지", description=msg, color=0x396CEC).set_footer(text=ctx.author, icon_url=ctx.author.avatar_url))

@client.command()
async def send(ctx, channel_id, *, msg):
    if ctx.author.id in admin:
        c = await client.fetch_channel(channel_id)
        await c.send(msg)

@client.command()
async def delete(ctx, chid, msgid):
    if ctx.author.id in admin:
            #ch = discord.utils.get(ctx.guild.text_channels, id=chid)
            #msg = await ch.fetch_message(msgid)
            #await msg.delete()
            await ctx.author.send("준비중인 기능입니다!")
        #try:
        #    ch = discord.utils.get(ctx.guild.text_channels, id=chid)
        #    msg = await ch.fetch_message(msgid)
        #    await msg.delete()
        #    await ctx.author.send("테스트중")
        #except:
        #    await ctx.author.send("당신이 사용한 `글린아/delete " + chid + " " + msgid + "` 명령어가 잘못되었습니다. piglin#7071 에 문의해주세요!")

@client.command()
async def 멘션(ctx, wid):
    if ctx.author.id in admin:
        if isinstance(ctx.channel, discord.abc.PrivateChannel) != True:
            if ctx.guild.id in useguild:
                widd = int(wid)
                my_name = discord.utils.get(ctx.guild.members, id=widd)
                #
                await ctx.message.delete()
                for o in range(0, 4):
                    for i in range(0, 5):
                        msg = await ctx.channel.send("{} :)".format(my_name.mention))
                        await msg.delete()
                    time.sleep(1.2)


"[[[[[[[[[[ 피글린 전용 ]]]]]]]]]]"


@client.command()
async def clear(ctx, count = 10):
    if ctx.author.id == 824243275975360562:
        await ctx.channel.purge(limit=count)

# for guild in client.guilds:

owner = 824243275975360562 # 봇 주인이 아닌 다른 사람이 이 명령어를 사용 시 TOS위반이라네요

@client.command(aliases=['접속서버', '서버', '접속중'])
async def join_server(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == True: 
        if ctx.author.id == owner:
            send1 = await ctx.send("서버를 찾는중이에요! [ 0개 서버를 찾음 ]")
            send = ""
            count = 0
            for guild in client.guilds:
                guildid = str(guild.id)
                try:
                    ch = random.choice(guild.text_channels)
                    link = await ch.create_invite(max_age = 600, max_uses = 1)
                    link = str(link)
                    send = send + guild.name + "  |  " + link + "  |  아이디 : " + guildid + "\n"
                except:
                    send = send + guild.name + "  |  (링크 제작 불가)  |  아이디 : " + guildid + "\n"
                
                count = count + 1
                str_count = str(count)
                await send1.edit(content = "서버를 찾는중이에요! [ " + str_count + "개 서버를 찾음 ]")
            
            await send1.edit(content = "서버를 다 찾았어요!")
            
            await ctx.send(send)
    else:
        await ctx.send('이 명령어는 디스코드 정책상 DM에서 작동돼요')

@client.command(aliases=['나와', '나가' '탈퇴'])
async def get_out(ctx, guild_id: int):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == True:
        if ctx.author.id == owner:
            msg2 = await ctx.send('서버 찾는중 ( ' + '0' + ' )')
            count = 0
            for guild in client.guilds:
                if guild.id == guild_id:
                    await guild.leave()
                    await ctx.send('`' + str(guild.name) + '` 에서 나왔어요!')
                    print(str(guild.name))
                else:
                    pass
                
                count = count+1
                show_count = str(count)
                await msg2.edit(content = '서버 찾는중 ( ' + show_count + ' )')

@client.command(aliases=['역할지급'])
async def give_role(ctx, ROLE: int):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == False:
        if ctx.author.id == owner:
            await ctx.message.delete()
            await ctx.author.add_roles(ctx.guild.get_role(ROLE))


"[[[[[[[[[[ 기타 ]]]]]]]]]]"


@client.command()
async def hongbo(ctx, type = 'None', count = 1):
    if ctx.author.id in admin:
        await ctx.message.delete()
        for i in range(0, count):
            embed = discord.Embed(title='게임 커뮤니티 서버(GC)', description="", color=파랑, url='https://discord.gg/m6hbgyFx98')
            embed.add_field(name='Q. 무엇을 하는 서버인가요?', value='A. 저희 서버는 2021년 7월에 만들어진 여러 게임 정보를 공유하고 대화하는 서버입니다!', inline=False)
            embed.add_field(name='Q. 게임 하면서 외로운 느낌이 들어요ㅜ', value='''A. 게임을 하면서 외로운 느낌이 들으셨다면 저희 서버로 오세요!
저희 서버는 수많은 게임들을 같이 할 수 있는 게임별로 채팅채널, 음성채널이 카테고리별로 나누어져서 마련되어있으니까요!''', inline=False)
            embed.add_field(name='Q. 제가 원하는 게임 카테고리에 찾아가기 힘들어요ㅜ', value='A. 괜찮아요 바로가기 채널에 게임별 카테고리로 가는 링크가 마련되어있어서 여러분은 클릭 한번만 하시면 된답니다!', inline=False)
            embed.add_field(name='Q. 제가 원하는 게임 카테고리가 없어요ㅜ', value='A. 건의 채널에 건의해주세요! 온라인 상태인 모더레이터 또는 서버장이 만들어줄꺼에요! 또 모더레이터 또는 서버장이 힘들지 않도록 모더레이터 또는 서버장이 명령어만 입력하면 자동으로 만들어져서 권한 설정까지 됩니다!', inline=False)
            embed.add_field(name='여기까지!', value='여기까지 저희 서버 소개였습니다! 감사합니다!\n\n링크 : https://discord.gg/m6hbgyFx98', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            if type == 'here':
                await ctx.channel.send('@here')
            elif type == 'every':
                await ctx.channel.send('@everyone')
            elif type == 'None':
                pass
            else:
                await ctx.channel.send('{접두}홍보 [here / every / None]')
            await ctx.channel.send(embed=embed)

"""
@client.command()
async def 테스트(ctx, 액수: int):
    data = {}
    data[str(ctx.author.id)] = []
    data[str(ctx.author.id)].append({
        "user_name": str(ctx.author),
        "user_id": int(ctx.author.id),
        "money": 액수
    })
    print(data)

    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)

@client.command()
async def 테스트1(ctx):
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)
        print(json_data)
        print("")
        print(json_data[str(ctx.author.id)])
        print("")
        print(json_data[str(ctx.author.id)][0]['money'])      
"""

#@client.command()
#async def 다삭제(ctx):
#    a = [878842432136048650, 878842432136048654, 878842432593219614, 878842433033605121, 878842433415295027]
#    for i in ctx.guild.categories:
#        if i.id in a:
#            pass
#        else:
#            ch1n = '💬ㅣ채팅'
#            ch1 = discord.utils.get(ctx.guild.text_channels, name=ch1n, category=i)
#            ch2n = '🌐ㅣ같이해요'
#            ch2 = discord.utils.get(ctx.guild.text_channels, name=ch2n, category=i)
#            ch3n = '📞ㅣ보이스채팅'
#            ch3 = discord.utils.get(ctx.guild.voice_channels, name=ch3n, category=i)
#            await ch1.delete()
#            await ch2.delete()
#            await ch3.delete()
#            await i.delete()

#@client.command()
#async def hongbo(ctx, type = 'None', count = 1):
#    if ctx.author.id in admin:
#        await ctx.message.delete()
#        for i in range(0, count):
#            embed = discord.Embed(title='게임 커뮤니티 서버(GC)', description="", color=파랑, url='https//discord.gg/m6hbgyFx98')
#            embed.add_field(name='Q. 무엇을 하는 서버인가요?', value='A. 저희 서버는 2021년 7월에 만들어진 여러 게임 정보를 공유하고 대화하는 서버입니다!', inline=False)
#            embed.add_field(name='Q. 게임 하면서 외로운 느낌이 들어요ㅜ', value='''A. 게임을 하면서 외로운 느낌이 들으셨다면 저희 서버로 오세요!
#저희 서버는 수많은 게임들을 같이 할 수 있는 게임별로 채팅채널, 음성채널이 카테고리별로 나누어져서 마련되어있으니까요!''', inline=False)
#            embed.add_field(name='Q. 제가 원하는 게임 카테고리에 찾아가기 힘들어요ㅜ', value='A. 괜찮아요 바로가기 채널에 게임별 카테고리로 가는 링크가 마련되어있어서 여러분은 클릭 한번만 하시면 된답니다!', inline=False)
#            embed.add_field(name='Q. 제가 원하는 게임 카테고리가 없어요ㅜ', value='A. 건의 채널에 건의해주세요! 온라인 상태인 모더레이터 또는 서버장이 만들어줄꺼에요! 또 모더레이터 또는 서버장이 힘들지 않도록 모더레이터 또는 서버장이 명령어만 입력하면 자동으로 만들어져서 권한 설정까지 됩니다!', inline=False)
#            embed.add_field(name='여기까지!', value='여기까지 저희 서버 소개였습니다! 감사합니다!\n\n링크 : https//discord.gg/m6hbgyFx98', inline=False)
#            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
#            if type == 'here':
#                await ctx.channel.send('@here')
#            elif type == 'every':
#                await ctx.channel.send('@everyone')
#            elif type == 'None':
#                pass
#            else:
#                await ctx.channel.send('글린아/홍보 [here / every / None]')
#            await ctx.channel.send(embed=embed)
#

#@client.event
#async def on_message_delete(message):
#    if os.path.isfile("C:/piglin/discordbot/" + now.year + "." + now.month + "." + now.day + ".txt"):
#        fileread = open("C:/piglin/discordbot/" + now.year + "." + now.month + "." + now.day + ".txt", 'r')
#        line = len(fileread.readlines())
#        fileadd = open("C:/piglin/discordbot/" + now.year + "." + now.month + "." + now.day + ".txt", 'a')
#        w = "[" + now.year + "년 " + now.month + "월 " + now.day + "일 " + now.hour + "시 " + now.minute + "분" + now.second + "초" + "]" + str(message.author) + "님이 ``" + message.content + "`` 라고 말했는데 지워졌습니다." % line
#        fileadd.write(w)
#        #await message.channel.send("[" + now.year + "년 " + now.month + "월 " + now.day + "일 " + now.hour + "시 " + now.minute + "분" + now.second + "초" + "]" + str(message.author) + "님이 ``" + message.content + "`` 라고 말했는데 지워졌습니다.")
#        fileadd.close()
#    else:

#if ctx.author.id in admin:
#embed = discord.Embed(title=arg, description="따라하라고 해서 따라한것 뿐이에요!", color=0x351C75)
#embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
#await ctx.channel.send(embed=embed)

#@client.command(name='도움말')
#async def hello(ctx):
#    await ctx.send('안녕하세요')

client.run(os.environ['token'])