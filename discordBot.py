
import discord
from character import ObJ
import youtube_dl
from discord.ext import commands, tasks
from itertools import cycle
import webbrowser

import pafy
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import random



import random

import numpy as np

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


# cogs = [musiC]

checkVar=""
adminRequester=""


bot_status = (["Status 1", "Status 2", "Status 3", "Status 4"])
users = {"jessi": 561940809809657858,
         "lizzie": 633853113794822173,
         "elijah": 859430234956234782,
         "connor": 564974969767854100,
         "eades": 538892372029865984,
         "braedon": 729832718057078814,
         "aria": 1142317341141647400}

userAdminStatus=[]
#test
token = "token"

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
testOrder = []
orderHold = []
guild = client.get_guild(1130919348941365320)
Xlist=[]
Ylist=[]
xLen=0
yLen=0

def searchUsers(target):
    for i in users:
        if (users[i] == target.id):
            return(i)
    return "Not found"
def checkAdmin(target):
    global userAdminStatus
    hold = searchUsers(target)
    if(hold not in userAdminStatus):
        return False
    else:
        return True


@client.event
async def on_ready():
    global initiativeTracker
    global turnN
    global userAdminStatus
    initiativeTracker = []
    turnN = [0]
    channel = client.get_channel(1130930600006647878)
    name = "python.programmer#1616"

    f=open("testFile.txt", "r")
    holdListf=[]
    for i,char in enumerate(f):
        holdListf.append(char.strip())
    userAdminStatus=holdListf
    f.close()

    print(f'{client.user} is now running!')
    await channel.send("bot online")
    guild = client.get_guild(1130919348941365320)
    save = guild.get_member(729832718057078814)
    print(client.get_guild(1130919348941365320))
    print(guild.get_member(729832718057078814))
    # vc = await client.get_channel(1130919349511798794).connect(timeout=20, reconnect=True)
    # source = FFmpegPCMAudio("https://www.youtube.com/watch?v=xvFZjo5PgG0", executable="ffmpeg")
    # vc.voice_client.play(source, after=None)

    print("check")

    # await save.send("test")


@client.command(pass_context=True, help="says hello in meowl")
async def hello(ctx):
    await ctx.send("Meowhoo!")


@client.command(aliases=["hello?"], pass_context=True, help="you type hello? and meowl does a sam jackson impression")
async def hewlo(ctx):
    await ctx.send("Hoot hoot muthafucka!")


@client.command(aliases=["hello:"], pass_context=True,
                help="type in hello: and meowl sends you a message. Command structure: !hello: <target name.")
async def Hello(ctx, member: str):
    guild = client.get_guild(1130919348941365320)
    print(member)
    if (not (member in users)):
        await ctx.send("not found")
    else:
        for i in users:
            if (i == member):
                san = users[i]
                print(san)

                await guild.get_member(san).send("Hoot hoot muthafucka")

    # await ctx.send("Hoot hoot muthafucka!")


@client.command(pass_context=True, help="joins the vc the user is in")
async def join(ctx):
    guild = client.get_guild(1130919348941365320)
    member_voice = ctx.author.voice
    print(ctx.author.voice)

    voice = await guild.get_channel(1130919349511798794).connect()

    #source =  FFmpegPCMAudio("")



    """
    if(not(member_voice==None) and member_voice.channel):
        try:
            print("test")
            await ctx.author.voice.channel.connect()
        except:
            print("no")
            await ctx.send("nah")
    """
    # print(member_voice)


@client.command(pass_context=True, help="disconnects from current vc")
async def leave(ctx):
    print(ctx.voice_client)
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Hoo?")
    else:
        print("nope")

"""
@client.command(help="rolls a d4")
async def roll4(ctx):
    await ctx.send(random.randint(1, 4))


@client.command(help="rolls a d6")
async def roll6(ctx):
    await ctx.send(random.randint(1, 6))
"""

@client.command(
    help="rolls a d6. Command structure: !Roll6 <number of rolls>. Optional command structure: !Roll6 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll6(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 6)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 6)
            else:
                for i in range(amount):
                    hold = random.randint(1, 6)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))


@client.command(
    help="rolls a d8. Command structure: !roll8 <number of rolls>. Optional command structure: !Roll8 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll8(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 8)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 8)
            else:
                for i in range(amount):
                    hold = random.randint(1, 8)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))


@client.command(help="rolls a d20")
async def roll20(ctx):
    await ctx.send(random.randint(1, 20))


@client.command(
    help="rolls a d20. Command structure: !Roll20 <number of rolls>. Optional command structure: !Roll20 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll20(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 20)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 20)
            else:
                for i in range(amount):
                    hold = random.randint(1, 20)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))


@client.command(
    help="rolls a d10. Command structure: !Roll10 <number of rolls>. Optional command structure: !Roll10 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll10(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 10)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 10)
            else:
                for i in range(amount):
                    hold = random.randint(1, 10)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))

@client.command(
    help="rolls a d4. Command structure: !Roll4 <number of rolls>. Optional command structure: !Roll4 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll4(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 4)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 4)
            else:
                for i in range(amount):
                    hold = random.randint(1, 4)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))


@client.command(
    help="rolls a d12. Command structure: !Roll12 <number of rolls>. Optional command structure: !Roll12 <number of rolls>:proficiency:<advantage>x<amount> or <disadvantage>x<amount> or <none>")
async def Roll12(ctx, param: str):
    numHold = ""
    if (":" not in param):
        total = 0
        param = int(param)
        for i in range(param):
            hold = random.randint(1, 12)
            numHold += str(hold) + " "
            total += hold
            # print(numHold)
        await ctx.channel.send((numHold, "Total:" + str(total)))
    else:
        saver = 0
        number, prof, add = param.split(":")
        if (add != "none"):
            dec, amount = add.split("x")
            amount = int(amount)
        # print(amount)

        total = 0
        number = int(number)
        prof = int(prof)
        for i in range(number):
            saver = 0
            if (add == "none"):
                saver = random.randint(1, 12)
            else:
                for i in range(amount):
                    hold = random.randint(1, 12)
                    await ctx.send(hold)
                    if (dec == "advantage"):
                        if (hold > saver):
                            saver = hold

                    else:

                        if (i == 0):
                            saver = hold

                        else:
                            if (hold < saver):
                                saver = hold

            numHold += str(saver) + "+" + str(prof) + " "
            total += saver + prof
        await ctx.channel.send((numHold, "Total:" + str(total)))


@client.command(help="returns the current initiative order")
async def order(ctx):
    holder="["
    for i in orderHold:
        holder+=i.getName() + ", "
    holder+="]"
    await ctx.send(str(holder))
    


@client.command(pass_context=True,
                help="adds an inputed name to the initiative. Command structure: !add: <name to be added>")
async def add(ctx, param: str):
    ob=ObJ(param)
    if(len(orderHold)!=0):    
        ob.setInit((orderHold[len(orderHold)-1].getInit()-1))
        
    else:
        ob.setInit(90)
    orderHold.append(ob)
    await ctx.send("added")


@client.command(help="clears the initiative order and resets the turn number")
async def clear(ctx):
    orderHold = []
    turnN[0] = 0
    await ctx.send("cleared")


@client.command(pass_context=True,
                help="removes the inputed character from the initiative order, and returns not found if not found. Command structure: !remove: <name to be removed>")
async def remove(ctx, param: str):
    # print(param)
    
    for i, char in enumerate(orderHold):
        if (char.getName() == param):
            orderHold.pop(i)
            if (i > (len(orderHold) - 1)):
                turnN[0] = 0
            await ctx.send("found and removed")
        elif(i==len(orderHold)):
            await ctx.send("not found")


@client.command(help="tells you whose turn it is")
async def turn(ctx):
    await ctx.send(orderHold[turnN[0]].getName())


@client.command(help="tells what turn number it is")
async def turnNum(ctx):
    await ctx.send(turnN[0])


@client.command(help="moves to the next persons turn and tells you whose turn it is")
async def proceed(ctx):
    if (turn[0] >= (len(orderHold) - 1)):
        print("test")
        turn[0] = 0
    else:
        turn[0] += 1
    await ctx.send("confirmed. Next turn is: " + orderHold[turnN[0]].getName())


@client.command(pass_context=True,
                help="has meowl send a message to the desired person. Command structure: !message \"<message recipient>:<message>\"")
async def message(ctx, param: str):
    target, mes = param.split(":")
    # print(param)

    guild = client.get_guild(1130919348941365320)
    print(target)
    if (not (target in users)):
        await ctx.send("not found")
    else:
        for i in users:
            if (i == target):
                san = users[i]
                # print(san)

                await guild.get_member(san).send(mes)


@client.command(aliases=["setNextSesh:"], pass_context=True,
                help="sets the next session date. command structure: !setNextSesh: \" \"")
async def setNextSesh(ctx, param: str):
    f = open("saveFile.txt", "w")
    # print(f.read())
    f.write(param)
    f.close()

    f = open("saveFile.txt", "r")
    await ctx.send("Confirmed. Next session is: " + f.read())


@client.command(aliases=["getNextSesh:"], pass_context=True,
                help="gets the next session date. command structure: !getNextSesh")
async def getNextSesh(ctx):
    f = open("saveFile.txt", "r")
    await ctx.send("Next session is: " + f.read())
    f.close()


@client.command(pass_context=True,help="rolls for initiative, adds in the initiative bonus, and then adds that to the order. Command structure: !insert: <name>:<init bonus>")
async def Insert(ctx, param: str):
    name, save= param.split(":")
    save=int(save)

    hold=random.randint(1,20)
    hold2=hold+save
    ob=ObJ(name)
    ob.setInit(hold2)
    ob.setInitBonus(save)
    await ctx.send(ob.getInit())
    if(len(orderHold)==0):
        orderHold.append(ob)
        await ctx.send(orderHold[0].getInit())
    else:
        print("test")
        for i, char in enumerate(orderHold):
            print(char.getInit())
            print(ob.getInit())
            if(int(char.getInit())<ob.getInit()):
                #print("ey")
                orderHold.insert(i, ob)
                break
                
            elif(int(char.getInit())==ob.getInit()):
                hold=random.randint(1,20)
                hold2=random.randint(1,20)

                hold3=hold+char.getInitBonus()
                hold4=hold2+ob.getInitBonus()
                if(hold3>hold4):
                    orderHold.insert(i+1, ob)
                    break
                else:
                    orderHold.insert(i,ob)
                    break

            elif((int(char.getInit())>ob.getInit()) and i==(len(orderHold)-1)):
                #print("case 2")
                orderHold.insert(i+1, ob)
                break

    holder="["
    for i in orderHold:
        holder+=i.getName() + ", "
    holder+="]"
    await ctx.send(str(holder))



@client.command(pass_context=True, help="Auth command")
async def admin(ctx):
    global adminRequester
    global checkVar
    await ctx.message.author.send("Insert auth code now")
    adminRequester=ctx.message.author
    checkVar=True
@client.command(pass_context=True)
async def adminCode(ctx, param: int):
    global adminRequester
    global checkVar
    if(ctx.message.author==adminRequester and checkVar==True):
        if(param==1101):
            await ctx.send("Admin approved")
            adminRequester=""
            checkVar=False
            hold3=0
            name=""
            for i in users:
                #print(ctx.message.author.id)
                if(users[i] == ctx.message.author.id):
                    userAdminStatus.append(i)
            f = open("testFile.txt", "w")
            for i in userAdminStatus:
                f.writelines(i + "\n")
            f.close()
@client.command(pass_context=True)
async def adminList(ctx):
    await ctx.send(userAdminStatus)

@client.command(pass_context=True)
async def wipeList(ctx):
    global userAdminStatus
    save = searchUsers(ctx.author)
    if(save in userAdminStatus):
        userAdminStatus=[]
        f = open("testFile.txt", "w")
        for i in userAdminStatus:
            #make sure to split at " : " to get the "key" and the "value"
            i, i1=i.split(" : ")
            f.writelines(i + " : " + i1 + "\n")
        f.close()
        await ctx.send("admins wiped")
    else:
        await ctx.send("request denied")

@client.command(pass_context=True)
async def giveAdmin(ctx, param: str):
    await ctx.send("Admin approved")
    
    status=userAdminStatus[param]
    if(status==0):
        userAdminStatus[param]=1

@client.command(pass_context=True)
async def remoteTest(ctx, param: int):
    channel = client.get_channel(1130930600006647878)
    global adminRequester
    global checkVar
    if(ctx.message.author==adminRequester and checkVar==True):
        if(param==1102):
            await ctx.send("Google command approved")
            c=webbrowser.get("chrome")
            c.open("https://www.google.co.uk/")
        else:
            await ctx.send("password rejected. Get fucked")
            await channel.send("Someone tried a wrong password")

        adminRequester=""
        checkVar = False

@client.command(pass_context=True)
async def bomb(ctx, code: int, param: str):
    global users
    if code==1001:
        users






client.run(token)
