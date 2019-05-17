from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from thrift import transport, protocol, server
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift.Thrift import *
import IDBOTS
from IDBOTS import *
from dit.ttypes import *
from akad.ttypes import *
from threading import Thread
from datetime import datetime
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from googletrans import Translator
from multiprocessing import Pool, Process
from subprocess import check_output
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
import youtube_dl
import pyimgflip
import pytz, pafy, livejson, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, traceback, shutil, unicodedata
#=============
#ID SELFBOT V-2.0
#SPEED TERGANTUNG VPS KALIAN 
#CREATOR  line.me/ti/p/~idbots_ku1
#=============
marker = "u72c90df8bd693cc7599875942d3b4318"
print("Login                          SB")
cl = LINE("bayu1@nopemail.me","Bayu123")
cl.log("Auth Token : " + str(cl.authToken))
lineProfile = cl.getProfile()
lineSettings = cl.getSettings()
mid = cl.getProfile().mid
responsename1 = cl.getProfile().displayName
cl.findAndAddContactsByMid(marker)
cl.sendMessage(marker, "create new bot induk")
print("\nLogin                          Bot 1")
ka = LINE("bayu2@nopemail.me","Bayu123")
ka.log("Auth Token : " + str(ka.authToken))
lineProfile = ka.getProfile()
lineSettings = ka.getSettings()
Amid = ka.getProfile().mid
responsename2 = ka.getProfile().displayName
ka.findAndAddContactsByMid(marker)
ka.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 2")
kb = LINE("bayu3@nopemail.me","Bayu123")
kb.log("Auth Token : " + str(kb.authToken))
lineProfile = kb.getProfile()
lineSettings = kb.getSettings()
Bmid = kb.getProfile().mid
responsename3 = kb.getProfile().displayName
kb.findAndAddContactsByMid(marker)
kb.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 3")
kc = LINE("bayu4@nopemail.me","Bayu123")
kc.log("Auth Token : " + str(kc.authToken))
lineProfile = kc.getProfile()
lineSettings = kc.getSettings()
Cmid = kc.getProfile().mid
responsename4 = kc.getProfile().displayName
kc.findAndAddContactsByMid(marker)
kc.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 4")
kd = LINE("bayu5@nopemail.me","Bayu123")
kd.log("Auth Token : " + str(kd.authToken))
lineProfile = kd.getProfile()
lineSettings = kd.getSettings()
Dmid = kd.getProfile().mid
responsename5 = kd.getProfile().displayName
kd.findAndAddContactsByMid(marker)
kd.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 5")
ke = LINE("bayu6@nopemail.me","Bayu123")
ke.log("Auth Token : " + str(ke.authToken))
lineProfile = ke.getProfile()
lineSettings = ke.getSettings()
Emid = ke.getProfile().mid
responsename6 = ke.getProfile().displayName
ke.findAndAddContactsByMid(marker)
ke.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 6")
kf = LINE("bayu7@nopemail.me","Bayu123")
kf.log("Auth Token : " + str(kf.authToken))
lineProfile = kf.getProfile()
lineSettings = kf.getSettings()
Fmid = kf.getProfile().mid
responsename7 = kf.getProfile().displayName
kf.findAndAddContactsByMid(marker)
kf.sendMessage(marker, "create new bot")
print("\nLogin                          Bot 7")
kg = LINE("bayu8@nopemail.me","Bayu123")
kg.log("Auth Token : " + str(kg.authToken))
lineProfile = kg.getProfile()
lineSettings = kg.getSettings()
Gmid = kg.getProfile().mid
responsename8 = kg.getProfile().displayName
kg.findAndAddContactsByMid(marker)
kg.sendMessage(marker, "create new bot")
print("\nLogin                          Bot JS")
js = LINE("bayu1@nopemail.me","Bayu123")
js.log("Auth Token : " + str(js.authToken))
lineProfile = js.getProfile()
lineSettings = js.getSettings()
Xmid = js.getProfile().mid
responsename9 = js.getProfile().displayName
js.findAndAddContactsByMid(marker)
js.sendMessage(marker, "create new bot")

print("RUNING IN ID SELFBOT V-2.0 \nOPEN ORDER SELFBOT & BOT CL\n\n1. SELFBOT ASSIST+ANTIJS\n2. BOT CL\n3. BOT WAR\n.4 BOT PROTECT ROOM\n\nJUAL SCRIP BOT CL/BOT WAR\ncreator line.me/ti/p/~idbots_ku1\n\nLOGIN SUCCES")

call = cl
oepoll = OEPoll(cl)
#TAMBAHIN MID KALIAN
creator = ["u72c90df8bd693cc7599875942d3b4318"]
owner = ["u72c90df8bd693cc7599875942d3b4318"]
admin = ["u72c90df8bd693cc7599875942d3b4318","u727933583f8830a3fc254fb1b906b174"]
staff = ["u72c90df8bd693cc7599875942d3b4318"]

KAC = [cl,ka,kb,kc,kd,ke,kf,kg,]
ABC = [ka,kb,kc,kd,ke,kf,kg]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Xmid]
Mbut = admin + staff

welcome = []
protectjs = []
protectjoin = []
protectqr = []
protectkick = []
protectinvite = []
protectcancel = []
msg_dict = {}
msg_dict1 = {}

IdKu = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "pqr":True,
    "pjoin":True,
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "invite":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoBlock':False,
    'Timeline':False,
    'autoLeave':False,
    'autoLeave1':False,
    "arespon":True,
    "detectMention":False,
    "Mentionkick":False,
    "Mentiongift":False,
    "welcomeOn":False,
    "stickerOn":False,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "unsend":False,
    "mention":"ᴋᴀʟᴏ ɴɢɪɴᴛɪᴘ ᴛᴇʀᴜs ᴅᴀᴘᴇᴛ ɢᴇʟᴀs ᴘᴇᴄᴀʜ ᴅɪ ᴋᴇᴘᴀʟᴀ...",
    "Respontag":"ɴɢᴇтᴀɢ ɢuᴇ sᴇᴋᴀʟɪ ʟᴀɢɪ, ᴅᴀᴘᴇᴛ ʜᴀᴅɪᴀʜ ᴘɪʀɪɴɢ ᴘᴇᴄᴀʜ...!!!",
    "Responpm":"ᴀᴅᴀ ᴀᴘᴀ ᴋᴀᴋ ᴛᴀᴅɪ ᴛᴀɢ sᴀʏᴀ ᴅɪ ɢʀᴜᴘ?",
    "welcome":"丂乇ㄥ卂爪卂ㄒ 乃乇尺Ꮆ卂乃ㄩ几Ꮆ Ҝ卂Ҝ,,, 丂乇爪ㄖᎶ卂 乃乇ㄒ卂卄",
    "leave":"See you next time again ...",
    "comment":"ᴀᴜᴛᴏ ʟɪᴋᴇ ɴ ᴄᴏᴍᴍᴇɴᴛ ᴅᴏɴᴇ\nвʏ.ᴛᴇᴀᴍ ɪᴅ ʙᴏᴛs\nline.me/ti/p/~idbots_ku1",
    "message":"тᴇяıмᴀ кᴀsıн suᴅᴀн ᴀᴅᴅ sᴀʏᴀ \nвʏ.ᴛᴇᴀᴍ ɪᴅ ʙᴏᴛs\nline.me/ti/p/~idbots_ku1",
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus

with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Idbot = codecs.open("settings.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
Idbots = json.load(Idbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━─────────────────━╮\n│╭━───────────────━╮\n││             \n│├━───────────────━╯\n││ 1."
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "││ %i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx+"│├━───────────────━╮\n││             \n│╰━───────────────━╯\n╰━─────────────────━╯", {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        #cl.sendMessage(to,"ᴛᴏᴛᴀʟ : {} ᴍᴇᴍʙᴇʀs".format(str(len(mid))))
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionV3(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@InexBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "nah kan \n  kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+IdKu["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nHallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+IdKu["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    print("RESPON MEMBER LEAVE")
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+IdKu["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ka.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kb.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kc.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kd.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ke.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kf.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kg.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "Asist Diluar ...")

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    cl.sendMessage(to, '', contentMetadata, 7)
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
#SEMUA BACKUP & PROTECT MENGUNAKAN, DEF

# DEF KICK

def kick(grup, target):
    print("DEP KICK MEMBER")
    try:
        asd= ka.idbotsKick(grup, [target])
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kb.idbotsKick(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kc.idbotsKick(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kd.idbotsKick(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= ke.idbotsKick(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        try:
                            asd= kf.idbotsKick(grup, [target])
                            if asd != None:
                                mbutfaild
                        except:
                            try:
                                asd= kg.idbotsKick(grup, [target])
                                if asd != None:
                                    mbutfaild
                            except:
                                pass
#DEF CANCEL

def cancel(grup, target):
    print("DEP KICK MEMBER")
    try:
        asd= ka.idbotsCancel(grup, [target])
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kb.idbotsCancel(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kc.idbotsCancel(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kd.idbotsCancel(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= ke.idbotsCancel(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        try:
                            asd= kf.idbotsCancel(grup, [target])
                            if asd != None:
                                mbutfaild
                        except:
                            try:
                                asd= kg.idbotsCancel(grup, [target])
                                if asd != None:
                                    mbutfaild
                            except:
                                pass

#DEF CANCEL

def cancel(grup, target):
    print("DEP KICK MEMBER")
    try:
        asd= ka.idbotsCancel(grup, [target])
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kb.idbotsCancel(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kc.idbotsCancel(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kd.idbotsCancel(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= ke.idbotsCancel(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        try:
                            asd= kf.idbotsCancel(grup, [target])
                            if asd != None:
                                mbutfaild
                        except:
                            try:
                                asd= kg.idbotsCancel(grup, [target])
                                if asd != None:
                                    mbutfaild
                            except:
                                pass

#DEFF ACCEPTGROUPINVITATION

def clacc(grup):
    try:
        asd= cl.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kaacc(grup):
    try:
        asd= ka.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kbacc(grup):
    try:
        asd= kb.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kcacc(grup):
    try:
        asd= kc.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kdacc(grup):
    try:
        asd= kd.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def keacc(grup):
    try:
        asd= ke.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kfacc(grup):
    try:
        asd= kf.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

def kgacc(grup):
    try:
        asd= kg.idbotsMasuk(grup)
        if asd != None:
            mbutfaild
    except:
        pass

#DEF TUTUP QR

def lockqr(grup):
    G = ka.getGroup(grup)
    G.preventedJoinByTicket = True
    print("DEP LOCKQR MEMBER")
    try:
        asd= kb.updateGroup(G)
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kc.updateGroup(G)
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kd.updateGroup(G)
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= ke.updateGroup(G)
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= kf.updateGroup(G)
                        if asd != None:
                            mbutfaild
                    except:
                        try:
                            asd= kg.updateGroup(G)
                            if asd != None:
                                mbutfaild
                        except:
                            pass

#DEF INVITE

def invite(grup, target):
    print("DEP KICK MEMBER")
    try:
        asd= ka.idbotsInvite(grup, [target])
        if asd != None:
            mbutfaild
    except:
        try:
            asd= kb.idbotsInvite(grup, [target])
            if asd != None:
                mbutfaild
        except:
            try:
                asd= kc.idbotsInvite(grup, [target])
                if asd != None:
                    mbutfaild
            except:
                try:
                    asd= kd.idbotsInvite(grup, [target])
                    if asd != None:
                        mbutfaild
                except:
                    try:
                        asd= ke.idbotsInvite(grup, [target])
                        if asd != None:
                            mbutfaild
                    except:
                        try:
                            asd= kf.idbotsInvite(grup, [target])
                            if asd != None:
                                mbutfaild
                        except:
                            try:
                                asd= kg.idbotsInvite(grup, [target])
                                if asd != None:
                                    mbutfaild
                            except:
                                pass

def backp(grup, target):
    try:
        ka.idbotsInvite(grup, [target])
        if target == [Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Xmid]:
            kb.idbotsMasuk(grup)
            kc.idbotsMasuk(grup)
            kd.idbotsMasuk(grup)
            ke.idbotsMasuk(grup)
            kf.idbotsMasuk(grup)
            kg.idbotsMasuk(grup)
    except:
        try:
            kb.idbotsInvite(grup, [target])
            if target == [Cmid,Dmid,Emid,Fmid,Gmid,Amid,Xmid]:
                kc.idbotsMasuk(grup)
                kd.idbotsMasuk(grup)
                ke.idbotsMasuk(grup)
                kf.idbotsMasuk(grup)
                kg.idbotsMasuk(grup)
                ka.idbotsMasuk(grup)
        except:
            try:
                kc.idbotsInvite(grup, [target])
                if target == [Dmid,Emid,Fmid,Gmid,Amid,Bmid,Xmid]:
                    kd.idbotsMasuk(grup)
                    ke.idbotsMasuk(grup)
                    kf.idbotsMasuk(grup)
                    kg.idbotsMasuk(grup)
                    ka.idbotsMasuk(grup)
                    kb.idbotsMasuk(grup)
            except:
                try:
                    kd.idbotsInvite(grup, [target])
                    if target == [Emid,Fmid,Gmid,Amid,Bmid,Cmid,Xmid]:
                        ke.idbotsMasuk(grup)
                        kf.idbotsMasuk(grup)
                        kg.idbotsMasuk(grup)
                        ka.idbotsMasuk(grup)
                        kb.idbotsMasuk(grup)
                        kc.idbotsMasuk(grup)
                except:
                    try:
                        ke.idbotsInvite(grup, [target])
                        if target == [Fmid,Gmid,Amid,Bmid,Cmid,Dmid,Xmid]:
                            kf.idbotsMasuk(grup)
                            kg.idbotsMasuk(grup)
                            ka.idbotsMasuk(grup)
                            kb.idbotsMasuk(grup)
                            kc.idbotsMasuk(grup)
                            kd.idbotsMasuk(grup)
                    except:
                        try:
                            kf.idbotsInvite(grup, [target])
                            if target == [Gmid,Amid,Bmid,Cmid,Dmid,Emid,Xmid]:
                                kg.idbotsMasuk(grup)
                                ka.idbotsMasuk(grup)
                                kb.idbotsMasuk(grup)
                                kc.idbotsMasuk(grup)
                                kd.idbotsMasuk(grup)
                                ke.idbotsMasuk(grup)
                        except:
                            try:
                                kg.idbotsInvite(grup, [target])
                                if target == [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Xmid]:
                                    ka.idbotsMasuk(grup)
                                    kb.idbotsMasuk(grup)
                                    kc.idbotsMasuk(grup)
                                    kd.idbotsMasuk(grup)
                                    ke.idbotsMasuk(grup)
                                    kf.idbotsMasuk(grup)
                            except:
                                pass

def black(target):
    Idbots["blacklist"][target] = True


def menu():
    key = Setmain["keyCommand"]
    key = key.title()
    menuMessage = "╭━──────────────━╮\n│    ɪᴅ sᴇʟғʙᴏᴛ ᴠ-2.0\n╰━──────────────━╯\n╭━──────────────━╮\n" + \
                               "│ ᴍᴇ\n" + \
                               "│ ᴍʏʙᴏᴛ\n" + \
                               "│ ʙᴀᴄᴋᴜᴘ\n" + \
                               "│ sᴘᴇᴇᴅ-sᴘ\n" + \
                               "│ /ɪɴ/ᴏᴜᴛ\n" + \
                               "│ ᴋᴇʟᴜᴀʀ/ᴍᴀsᴜᴋ\n" + \
                               "│ ᴛᴀɢ\n" + \
                               "│ ʀᴇsᴘᴏɴ\n" + \
                               "│ ᴄᴇᴋ/ᴄᴇᴋ ᴊs\n" + \
                               "│ go' @\n" + \
                               "│ ᴘʀᴀɴᴋ ɴ ᴄʟɪɴɢ\n" + \
                               "│ ʀᴇᴍᴏᴠᴇ ᴄʜᴀᴛ\n" + \
                               "│ 1ᴜᴘ-7ᴜᴘ/ᴊs ᴜᴘ\n" + \
                               "│ 1ɴᴀᴍᴇ-7ɴᴀᴍᴇ/ ᴊs ɴᴀᴍᴇ\n"+ \
                               "│ ʙᴀɴʟɪsᴛ\n" + \
                               "│ ᴄʟᴇᴀʀʙᴀɴ\n" + \
                               "│ ʀᴇғʀᴇsʜ\n" + \
                               "╰━──────────────━╯"
    return menuMessage

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param2 in Idbots["blacklist"]:
                t1 = Thread(target=attck, args=(op.param1, op.param2))
                t1.start()
                t2 = Thread(target=lockqr, args=(op.param1,))
                t2.start()
                t3 = Thread(target=black, args=(op.param2,))
                t3.start()
            if op.param1 in protectqr:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t5 = Thread(target=attck, args=(op.param1, op.param2))
                    t5.start()
                    t6 = Thread(target=lockqr, args=(op.param1,))
                    t6.start()
                    t7 = Thread(target=black, args=(op.param2,))
                    t7.start()
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t8 = Thread(target=cancl, args=(op.param1, op.param3))
                    t8.start()
                    t9 = Thread(target=attck, args=(op.param1, op.param2))
                    t9.start()
                    t10 = Thread(target=black, args=(op.param2,))
                    t10.start()
            if op.param2 in Idbots["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t11 = Thread(target=cancl, args=(op.param1, op.param3))
                    t11.start()
                    t12 = Thread(target=attck, args=(op.param1, op.param2))
                    t12.start()
                    t13 = Thread(target=black, args=(op.param2,))
                    t13.start()
            if op.param3 in Idbots["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t15 = Thread(target=cancl, args=(op.param1, op.param3))
                    t15.start()
                    t16 = Thread(target=attck, args=(op.param1, op.param2))
                    t16.start()
                    t17 = Thread(target=black, args=(op.param2,))
                    t17.start()
        if op.type ==19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t19 = Thread(target=invt, args=(op.param1, op.param3))
                    t19.start()
                    t20 = Thread(target=attck, args=(op.param1, op.param2))
                    t20.start()
                    t21 = Thread(target=black, args=(op.param2,))
                    t21.start()
            if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    Idbots["blacklist"][op.param2] = True
                    t22 = Thread(target=backp, args=(op.param1, op.param3))
                    t22.start()
                    t23 = Thread(target=attck, args=(op.param1, op.param2))
                    t23.start()
                    t24 = Thread(target=black, args=(op.param2,))
                    t24.start()
            if op.param3 in admin:
                if op.param2 not in Bots and op.param2 not in owner:
                    t25 = Thread(target=invt, args=(op.param1, op.param3))
                    t25.start()
                    t26 = Thread(target=attck, args=(op.param1, op.param2))
                    t26.start()
                    t27 = Thread(target=black, args=(op.param2,))
                    t27.start()

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t28 = Thread(target=attck, args=(op.param1, op.param2))
                    t28.start()
                    t29 = Thread(target=black, args=(op.param2,))
                    t29.start()
            if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t30 = Thread(target=invt, args=(op.param1, op.param3))
                    t30.start()
                    t31 = Thread(target=attck, args=(op.param1, op.param2))
                    t31.start()
                    t32 = Thread(target=black, args=(op.param2,))
                    t32.start()
            if op.param3 in admin:
                if op.param2 not in Bots and op.param2 not in owner:
                    t33 = Thread(target=invt, args=(op.param1, op.param3))
                    t33.start()
                    t34 = Thread(target=attck, args=(op.param1, op.param2))
                    t34.start()
                    t35 = Thread(target=black, args=(op.param2,))
                    t35.start()
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    t36 = Thread(target=attck, args=(op.param1, op.param2))
                    t36.start()
                    t37 = Thread(target=black, args=(op.param2,))
                    t37.start()
            if op.param2 in Idbots["blacklist"]:
                t38 = Thread(target=lockqr, args=(op.param1,))
                t38.start()
            if op.param2 in Idbots["blacklist"]:
                G = cl.getGroup(op.param1)
                if G is None:
                    pass
                else:
                    gMembMids = [contact.mid for contact in G.members]
                    matched_list = []
                    for tag in Idbots["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                            pass
                    for jj in matched_list:
                        try:
                            ka.idbotsKick(op.param1,[jj])
                        except:
                            try:
                                kb.idbotsKick(op.param1,[jj])
                            except:
                                try:
                                    kc.idbotsKick(op.param1,[jj])	
                                except:
                                    try:
                                        kd.idbotsKick(op.param1,[jj])
                                    except:
                                        try:
                                            ke.idbotsKick(op.param1,[jj])
                                        except:
                                            try:
                                                kg.idbotsKick(op.param1,[jj])
                                            except:
                                                try:
                                                    kf.idbotsKick(op.param1,[jj])
                                                except:
                                                    pass
        if op.type == 18:
            kickcount += 1
            
        if op.type == 31:
            cancelcount += 1
        if op.type == 19 or op.type == 32:
            if op.param1 in protectjs:
                print("PROTECT ANTIJS ON")
                try:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        js.idbotsMasuk(op.param1)
                        X = js.getGroup(op.param1)
                        js.idbotsInvite(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid])
                        cl.idbotsMasuk(op.param1)
                        ka.idbotsMasuk(op.param1)
                        kb.idbotsMasuk(op.param1)
                        kc.idbotsMasuk(op.param1)
                        kd.idbotsMasuk(op.param1)
                        ke.idbotsMasuk(op.param1)
                        kf.idbotsMasuk(op.param1)
                        kg.idbotsMasuk(op.param1)
                        js.idbotsKick(op.param1,[op.param2])
                        js.idbotsKeluar(op.param1)
                        X = ka.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        ka.updateGroup(X)
                        ka.idbotsInvite(op.param1,[Xmid])
                except:
                    pass

        if op.type == 13:
            if mid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=clacc, args=(op.param1)
                        t36.start()
                        ginfo = cl.getGroup(op.param1)
                        cl.idbotsInvite(op.param1,[Xmid])
                    else:
                        t2 = Thread(target=clacc, args=(op.param1)
                        t36.start()
                        ginfo = cl.getGroup(op.param1)
                        cl.idbotsInvite(op.param1,[Xmid])
            if Amid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kaacc, args=(op.param1)
                        t36.start()
                        ginfo = ka.getGroup(op.param1)
                        ka.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=kaacc, args=(op.param1)
                        t36.start()
                        ginfo = ka.getGroup(op.param1)
            if Bmid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kbacc, args=(op.param1)
                        t36.start()
                        ginfo = kb.getGroup(op.param1)
                        kb.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=kbacc, args=(op.param1)
                        t36.start()
                        ginfo = kb.getGroup(op.param1)
            if Cmid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kcacc, args=(op.param1)
                        t36.start()
                        ginfo = kc.getGroup(op.param1)
                        kc.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=kcacc, args=(op.param1)
                        t36.start()
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kdacc, args=(op.param1)
                        t36.start()
                        ginfo = kd.getGroup(op.param1)
                        kd.idbotKeluar(op.param1)
                    else:
                        t2 = Thread(target=kdacc, args=(op.param1)
                        t36.start()
                        ginfo = kd.getGroup(op.param1)
            if Emid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=keacc, args=(op.param1)
                        t36.start()
                        ginfo = ke.getGroup(op.param1)
                        ke.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=keacc, args=(op.param1)
                        ginfo = ke.getGroup(op.param1)
            if Fmid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kfacc, args=(op.param1)
                        t36.start()
                        ginfo = kf.getGroup(op.param1)
                        kf.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=kfacc, args=(op.param1)
                        t36.start()
                        ginfo = kf.getGroup(op.param1)
            if Gmid in op.param3:
                if IdKu["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        t2 = Thread(target=kgacc, args=(op.param1)
                        t36.start()
                        ginfo = kg.getGroup(op.param1)
                        kg.idbotsKeluar(op.param1)
                    else:
                        t2 = Thread(target=kgacc, args=(op.param1)
                        t36.start()
                        ginfo = kg.getGroup(op.param1)


        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])

        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if IdKu["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 65:
            if IdKu["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if IdKu["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 55:
            if op.param2 in Idbots["blacklist"]:
                if op.param2 in Bots and op.param2 in owner and op.param2 in admin and op.param2 in staff:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

            if op.param1 in Setmain["SKreadPoint"]:
                if op.param2 in Setmain["SKreadMember"][op.param1]:
                    pass
                else:
                    Setmain["SKreadMember"][op.param1][op.param2] = True
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        sider = cl.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+sider
                        cl.sendImageWithURL(op.param1, image)

        if op.type == 26:
           if IdKu["selfbot"] == True:
               msg = op.message
               if msg._from in Bots:
                   if msg._from in Idbots["blacklist"]:
                      try:
                          random.choice(ABC).idbotsKick(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).idbotsKick(msg.to, [msg._from])
                          except:
                              random.choice(ABC).idbotsKick(msg.to, [msg._from])
               if msg._from in Bots:
                 if IdKu["talkban"] == True:
                   if msg._from in IdKu["Talkblacklist"]:
                      try:
                          random.choice(ABC).idbotsKick(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).idbotsKick(msg.to, [msg._from])
                          except:
                              random.choice(ABC).idbotsKick(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if IdKu["arespon"] == True: 
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           contact = cl.getContact(msg._from)
                           sendMentionV3(msg._from, "@!  "+ IdKu["Responpm"], [msg._from])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if IdKu["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   print("RESPON DI TAG MEMBER")
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, IdKu["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"518","STKPKGID":"2","STKVER":"100"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if IdKu["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   print("RESPON DI TAG GIFT MEMBER PM")
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           cl.sendMessage(msg.to, "ᴘᴍ ɢᴀᴇs")
                           cl.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if IdKu["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, "Im so sorry....")
                           cl.idbotsKick(msg.to, [msg._from])
                           break
               
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if IdKu["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            channel.like(url[25:58], url[66:], likeType=1006)
                            channel.comment(url[25:58], url[66:], IdKu["message"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if IdKu["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if IdKu["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 「 Contact Info 」\n۞ Nama : " + msg.contentMetadata["displayName"] + "\n۞ MID : " + msg.contentMetadata["mid"] + "\n۞ Status Msg : " + contact.statusMessage + "\n۞ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if IdKu["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in Idbots["blacklist"]:
                            cl.sendMessage(msg.to, "「Dia ke bl kak... hpus bl dulu lalu invite lagi」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.idbotsInvite(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  IdKu["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"ʟɪᴍɪᴛ")
                                  IdKu["invite"] = False
                                  break
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if IdKu["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        IdKu["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        IdKu["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if IdKu["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        IdKu["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if IdKu["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        IdKu["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        IdKu["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if IdKu["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        IdKu["dellstaff"] = True
                    else:
                        IdKu["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if IdKu["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        IdKu["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        IdKu["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if IdKu["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        IdKu["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if IdKu["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in Idbots["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        IdKu["wblacklist"] = True
                    else:
                        Idbots["blacklist"][msg.contentMetadata["mid"]] = True
                        IdKu["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if IdKu["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in Idbots["blacklist"]:
                        del Idbots["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        IdKu["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if IdKu["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in IdKu["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        IdKu["Talkwblacklist"] = True
                    else:
                        IdKu["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        IdKu["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if IdKu["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in IdKu["Talkblacklist"]:
                        del IdKu["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        IdKu["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if IdKu["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[IdKu["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(InexWar["Addimage"]["name"])))
                        IdKu["Addimage"]["status"] = False                
                        IdKu["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if IdKu["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[IdKu["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(InexWar["Addvideo"]["name"])))
                        IdKu["Addvideo"]["status"] = False                
                        IdKu["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if IdKu["Addsticker"]["status"] == True:
                        stickers[IdKu["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(InexWar["Addsticker"]["name"])))
                        IdKu["Addsticker"]["status"] = False                
                        IdKu["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if IdKu["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[IdKu["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(InexWar["Addaudio"]["name"])))
                        IdKu["Addaudio"]["status"] = False                
                        IdKu["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if Idbots["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     Idbots["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["SKfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["video"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["video"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah jadi video")
               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["SKfoto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Amid]
                            ka.updateProfilePicture(path)
                            ka.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["SKfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Bmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["SKfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["SKfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Dmid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["SKfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Emid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["SKfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Fmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["SKfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Gmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Xmid in Setmain["SKfoto"]:
                            path = js.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Xmid]
                            js.updateProfilePicture(path)
                            js.sendMessage(msg.to,"Foto berhasil dirubah")


               if msg.contentType == 1:
                 if msg._from in admin:
                   if Idbots["changePicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kd.downloadObjectMsg(msg_id)
                     path5 = ke.downloadObjectMsg(msg_id)
                     path6 = kf.downloadObjectMsg(msg_id)
                     path7 = kg.downloadObjectMsg(msg_id)
                     path8 = js.downloadObjectMsg(msg_id)
                     Idbots["changePicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path6)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path7)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     js.updateProfilePicture(path8)
                     js.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     cl.sendChatChecked(msg.to, msg_id)
                     ka.sendChatChecked(msg.to, msg_id)
                     kb.sendChatChecked(msg.to, msg_id)
                     kc.sendChatChecked(msg.to, msg_id)
                     kd.sendChatChecked(msg.to, msg_id)
                     ke.sendChatChecked(msg.to, msg_id)
                     kf.sendChatChecked(msg.to, msg_id)
                     kg.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)

                        if cmd == "self on":
                            if msg._from in admin:
                                IdKu["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                IdKu["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "menu":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                menuMessage = menu()
                                gans = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "  "
                                ret_ = str(menuMessage)
                                gn = str(gans.displayName)
                                pesan = ''
                                pesan2 = pesan+""
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':gans.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, str(menuMessage))

                        if cmd == "backup":
                            if msg._from in admin or msg._from in Bots:
                                try:
                                    cl.findAndAddContactsByMid(Amid)
                                    cl.findAndAddContactsByMid(Bmid)
                                    cl.findAndAddContactsByMid(Cmid)
                                    cl.findAndAddContactsByMid(Dmid)
                                    cl.findAndAddContactsByMid(Emid)
                                    cl.findAndAddContactsByMid(Fmid)
                                    cl.findAndAddContactsByMid(Gmid)
                                    cl.findAndAddContactsByMid(Xmid)
                                    ka.findAndAddContactsByMid(mid)
                                    ka.findAndAddContactsByMid(Bmid)
                                    ka.findAndAddContactsByMid(Cmid)
                                    ka.findAndAddContactsByMid(Dmid)
                                    ka.findAndAddContactsByMid(Emid)
                                    ka.findAndAddContactsByMid(Fmid)
                                    ka.findAndAddContactsByMid(Gmid)
                                    ka.findAndAddContactsByMid(Xmid)
                                    kb.findAndAddContactsByMid(mid)
                                    kb.findAndAddContactsByMid(Amid)
                                    kb.findAndAddContactsByMid(Cmid)
                                    kb.findAndAddContactsByMid(Dmid)
                                    kb.findAndAddContactsByMid(Emid)
                                    kb.findAndAddContactsByMid(Fmid)
                                    kb.findAndAddContactsByMid(Gmid)
                                    kb.findAndAddContactsByMid(Xmid)
                                    kc.findAndAddContactsByMid(mid)
                                    kc.findAndAddContactsByMid(Amid)
                                    kc.findAndAddContactsByMid(Bmid)
                                    kc.findAndAddContactsByMid(Dmid)
                                    kc.findAndAddContactsByMid(Emid)
                                    kc.findAndAddContactsByMid(Fmid)
                                    kc.findAndAddContactsByMid(Gmid)
                                    kc.findAndAddContactsByMid(Xmid)
                                    kd.findAndAddContactsByMid(mid)
                                    kd.findAndAddContactsByMid(Amid)
                                    kd.findAndAddContactsByMid(Bmid)
                                    kd.findAndAddContactsByMid(Cmid)
                                    kd.findAndAddContactsByMid(Emid)
                                    kd.findAndAddContactsByMid(Fmid)
                                    kd.findAndAddContactsByMid(Gmid)
                                    kd.findAndAddContactsByMid(Xmid)
                                    ke.findAndAddContactsByMid(mid)
                                    ke.findAndAddContactsByMid(Amid)
                                    ke.findAndAddContactsByMid(Bmid)
                                    ke.findAndAddContactsByMid(Cmid)
                                    ke.findAndAddContactsByMid(Dmid)
                                    ke.findAndAddContactsByMid(Fmid)
                                    ke.findAndAddContactsByMid(Gmid)
                                    ke.findAndAddContactsByMid(Xmid)
                                    kf.findAndAddContactsByMid(mid)
                                    kf.findAndAddContactsByMid(Amid)
                                    kf.findAndAddContactsByMid(Bmid)
                                    kf.findAndAddContactsByMid(Cmid)
                                    kf.findAndAddContactsByMid(Dmid)
                                    kf.findAndAddContactsByMid(Emid)
                                    kf.findAndAddContactsByMid(Gmid)
                                    kf.findAndAddContactsByMid(Xmid)
                                    kg.findAndAddContactsByMid(mid)
                                    kg.findAndAddContactsByMid(Amid)
                                    kg.findAndAddContactsByMid(Bmid)
                                    kg.findAndAddContactsByMid(Cmid)
                                    kg.findAndAddContactsByMid(Dmid)
                                    kg.findAndAddContactsByMid(Emid)
                                    kg.findAndAddContactsByMid(Fmid)
                                    kg.findAndAddContactsByMid(Xmid)
                                    js.findAndAddContactsByMid(mid)
                                    js.findAndAddContactsByMid(Amid)
                                    js.findAndAddContactsByMid(Bmid)
                                    js.findAndAddContactsByMid(Cmid)
                                    js.findAndAddContactsByMid(Dmid)
                                    js.findAndAddContactsByMid(Emid)
                                    js.findAndAddContactsByMid(Fmid)
                                    js.findAndAddContactsByMid(Gmid)
                                    cl.sendMessage(to,"Sukses ...")
                                except:
                                    cl.sendMessage(to,"Sukses ...")
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"ɪᴅ sᴇʟғʙᴏᴛ ᴠ-2.0") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd.startswith('about'):
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2025
                                bln = 12    #isi bulannya yg sewa
                                hr = 11    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = cl.getContact(mid)
                                favoritelist = cl.getFavoriteMids()
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                cl.sendText("u727933583f8830a3fc254fb1b906b174", 'haiii')
                                elapsed_time = time.time() - start
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Informasi Selfbot 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「Self Bots 」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendContact(to, "u727933583f8830a3fc254fb1b906b174")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "me" or text.lower() == 'me':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
#                               sendMention(msg.to, sender, "「 User Selfbot 」\n", "")
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendContact(to, mid)

                        elif ("Steal " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               a = cl.getProfileCoverURL(mid=key1)
                               cl.sendMessage(msg.to, "「 Contact Info 」\n• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   cl.sendImageWithURL(receiver, a)
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   cl.sendImageWithURL(receiver, a)

                        elif ("Cover " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))

                        elif ("Sticker: " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower():
                           if msg._from in admin:
                             if Idbots["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.inviteIntoGroup(op.param1,[Xmid])
                                    cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group1 = ka.findGroupByTicket(ticket_id)
                                    ka.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                    ka.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group2 = kb.findGroupByTicket(ticket_id)
                                    kb.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                    kb.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group3 = kc.findGroupByTicket(ticket_id)
                                    kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                    kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group4 = kd.findGroupByTicket(ticket_id)
                                    kd.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                    kd.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group5 = ke.findGroupByTicket(ticket_id)
                                    ke.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                    ke.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group6 = kf.findGroupByTicket(ticket_id)
                                    kf.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                    kf.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                    group7 = kg.findGroupByTicket(ticket_id)
                                    kg.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                    kg.sendMessage(msg.to, "Masuk : %s" % str(group.name))

                        elif cmd == "mybot" or cmd == "mymbut":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendContact(to, Amid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendContact(to, Bmid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendContact(to, Cmid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendContact(to, Dmid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendContact(to, Emid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendContact(to, Fmid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendContact(to, Gmid)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Xmid}
                               cl.sendContact(to, Xmid)

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["autoRead"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["autoRead"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "reject":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

                        elif text.lower() == "hapus chat":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ᴄʜᴀᴛ")
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ka.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ᴄʜᴀᴛ")
                               except:
                                   pass
                        elif cmd.startswith("invite "):
                           if msg._from in admin:
                             ext = text.split()
                             number = ext[2]
                             if number.isdigit():
                                 groups = cl.getGroupIdsJoined()
                                 if int(number) < len(groups) and int(number) >= 0:
                                     groupid = groups[int(number)]
                                     try:
                                         cl.findAndAddContactsByMid(sender)
                                         cl.inviteIntoGroup(groupid,[sender])
                                         groupname = cl.getGroup(groupid).name
                                         cl.sendMessage(receiver,"Success invite group! %s"%groupname)
                                     except:
                                         cl.sendMessage(receiver," Permission denied contact in banlist")

                        elif cmd.startswith("leave "):
                           if msg._from in admin:
                             ext = text.split()
                             number = ext[2]
                             if number.isdigit():
                                 groups = cl.getGroupIdsJoined()
                                 if int(number) < len(groups) and int(number) >= 0:
                                     groupid = groups[int(number)]
                                     groupname = cl.getGroup(groupid).name
                                     if not silent:cl.sendMessage(groupid,"!Bye~bye %s"%groupname)
                                     cl.leaveGroup(groupid)
                                     cl.sendMessage(receiver,"Success leave group! %s"%groupname)
#==================================

                        elif cmd.startswith("broadcast: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = cl.getGroupIdsJoined()
                             for group in saya:
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Broadcast 」\nBroadcast by "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif text.lower() == "mykey":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Setkey 」\nSetkey saat ini「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「 Resetkey 」\nSetkey mu telah direset")

                        elif cmd == "restart":
                          if IdKu["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "ᴘʀᴏsᴇsɪɴɢ")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "sᴛᴀʀᴛ")
                            
                        elif cmd == "runtime":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "sᴇʟғʙᴏᴛ: "
                                ret_ = "• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "「 Group Info 」\n۞ Nama Group : {}".format(G.name)+ "\n۞ ID Group : {}".format(G.id)+ "\n۞ Pembuat : {}".format(G.creator.displayName)+ "\n۞ Waktu Dibuat : {}".format(str(timeCreated))+ "\n۞ Jumlah Member : {}".format(str(len(G.members)))+ "\n۞  Jumlah Pending : {}".format(gPending)+ "\n۞ Group Qr : {}".format(gQr)+ "\n۞ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "gruplist":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Grup "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                Idbots["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Idbots["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["SKfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if IIdKu["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["video"][mid] = True
                                cl.sendText(msg.to,"Kirim videonya.....")
                                
                        elif cmd == "1up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Amid] = True
                                ka.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Bmid] = True
                                kb.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "3up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")                                

                        elif cmd == "4up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Dmid] = True
                                kd.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "5up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Emid] = True
                                ke.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "6up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Fmid] = True
                                ke.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "7up":
                            if msg._from in admin:
                                Setmain["SKfoto"][Gmid] = True
                                ke.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "jsup":
                            if msg._from in admin:
                                Setmain["SKfoto"][Xmid] = True
                                js.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("1name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("2name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("3name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("4name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("5name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("6name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("7name "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("jsname "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = js.getProfile()
                                profile.displayName = string
                                js.updateProfile(profile)
                                js.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "sepi" or text.lower() == "tag":
                           if IdKu["selfbot"] == True:
                            if msg._from in admin:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append(i.mid)
                                mentionMembers(msg.to, b)

                        elif cmd.startswith("tag room: "):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                            	separate = msg.text.split(":")
                            	number = msg.text.replace(separate[0] + ":"," ")
                            	groups = cl.getGroupIdsJoined()
                            	gid = groups[int(number)-1]                                                            
                            	group = cl.getGroup(gid)                                                            
                            	nama = [contact.mid for contact in group.members]
                            	k = len(nama)//20
                    	        for a in range(k+1):
                            		txt = u''
                    		        s=0
                            		b=[]
                            		for i in group.members[a*20 : (a+1)*20]:
                            			b.append(i.mid)
                            		mentionMembers(gid, b)                            
                    		        cl.sendMessage(msg.to, "Berhasil Mention Member di Group: \n " + str(group.name))

                        elif cmd == "status":
                          if IdKu["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  SETTING MENU \n\n"
                                if IdKu["detectMention"] == True: md+="R1 On\n"
                                else: md+="R1 Off\n"
                                if IdKu["arespon"] == True: md+="R2 On\n"
                                else: md+="R2 Off\n"
                                if IdKu["autoJoin"] == True: md+="Autojoin on\n"
                                else: md+="Autojoin off\n"
                                if Idbots["autoJoinTicket"] == True: md+="Jointicket On\n"
                                else: md+="Jointicket Off\n"
                                if IdKu["unsend"] == True: md+="Unsend On\n"
                                else: md+="Unsend Off\n"
                                if IdKu["autoAdd"] == True: md+="Autoadd On\n"
                                else: md+="Autoadd Off\n"
                                if msg.to in welcome: md+="Welcome On\n"
                                else: md+="Welcome Off\n"
                                if IdKu["autoLeave"] == True: md+="Autoleave On\n"
                                else: md+="Autoleave Off\n"
                                if msg.to in protectjs: md+="Antijs on\n"
                                else: md+="Antijs off\n"
                                cl.sendMessage(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")

                        elif cmd == "protectlist":
                          if IdKu["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                a = 0
                                b = 0
                                gid = antijs
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = ghost
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"SETTING PROTECT\n\nAntijs :\n"+ma+"\nGhost:\n"+mb+"\n\nProtectlist %s Grup protect" %(str(len(antijs)+len(ghost))))

                        elif cmd == "listbot":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar User Bot 」\n\n"+ma+"\nTotal「%s」List Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Admin 」\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Pengguna Selfbot" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "respon":
                            print("RESPON BOT")
                            if msg._from in admin or msg._from in Bots:
                                ka.sendText(msg.to,"ʜᴀᴅɪʀ")
                                kb.sendText(msg.to,"ʜᴀᴅɪʀ")
                                kc.sendText(msg.to,"ʜᴀᴅɪʀ")
                                kd.sendText(msg.to,"ʜᴀᴅɪʀ")
                                ke.sendText(msg.to,"ʜᴀᴅɪʀ")
                                kf.sendText(msg.to,"ʜᴀᴅɪʀ")
                                kg.sendText(msg.to,"ʜᴀᴅɪʀ")  

                        if cmd == "/in":
                          if msg._from in admin or msg._from in Bots:
                            print("ALL BOT DI INVITE")
                            try:
                                anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Xmid]
                                cl.idbotsInvite(msg.to, anggota)
                                ka.idbotsMasuk(msg.to)
                                kb.idbotsMasuk(msg.to)
                                kc.idbotsMasuk(msg.to)
                                kd.idbotsMasuk(msg.to)
                                ke.idbotsMasuk(msg.to)
                                kf.idbotsMasuk(msg.to)
                                kg.idbotsMasuk(msg.to)
                            except:
                                try:
                                    G = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = ka.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    ka.updateGroup(G)
                                    ka.inviteIntoGroup(msg.to, [Xmid])
                                except:
                                    pass

                        if cmd == "stay":
                          if msg._from in admin or msg._from in Bots:
                            print("ANTIJS DI INVITE")
                            try:
                                G = cl.getGroup(msg.to)
                                cl.idbotsInvite(msg.to, [Xmid])
                            except:
                                try:
                                    G = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = kg.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    kg.updateGroup(G)
                                    kg.idbotsInvite(msg.to, [Xmid])
                                except:
                                    pass

                        elif cmd == "in":
                            print("ANTIJS MASUK GRUP")
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                js.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = js.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                js.updateGroup(G)

                        elif cmd == "out":
                          print("ANTIJS KELUAR GRUP")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                js.idbotsKeluar(msg.to)

                        elif cmd == "/out":
                          if msg._from in admin:
                            print("ALL BOT KELUAR GRUP")
                            try:
                                G = cl.getGroup(msg.to)
                                cl.idbotsCancel(op.param1,[Xmid])
                                ka.idbotsKeluar(msg.to)
                                kb.idbotsKeluar(msg.to)
                                kc.idbotsKeluar(msg.to)
                                kd.idbotsKeluar(msg.to)
                                ke.idbotsKeluar(msg.to)
                                kf.idbotsKeluar(msg.to)
                                kg.idbotsKeluar(msg.to)
                            except:
                                try:
                                    G = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    js.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    ka.idbotsKeluar(msg.to)
                                    kb.idbotsKeluar(msg.to)
                                    kc.idbotsKeluar(msg.to)
                                    kd.idbotsKeluar(msg.to)
                                    ke.idbotsKeluar(msg.to)
                                    kf.idbotsKeluar(msg.to)
                                    kg.idbotsKeluar(msg.to)
                                    G = js.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    js.updateGroup(G)
                                    js.idbotsKeluar(msg.to)
                                except:
                                    pass

                        elif cmd == ".bye":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.idbotsKeluar(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ka.sendMessage(i, "「Maaf Bot Di Paksa Keluar」")
                                        ka.idbotsKeluar(i)
                                        kb.idbotsKeluar(i)
                                        kc.idbotsKeluar(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "no1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "no2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "no3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "no4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "no7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)

                        elif cmd == "runtime":
                          print("KECEPATAN WAKTU RESPON")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          print("KECEPATAN SPEED BOT")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage("u727933583f8830a3fc254fb1b906b174", 'cek speed')
                               hasil = time.time() - start
                               cl.sendMessage(msg.to,  ' %.5f' % round(hasil,4)+ " detik")
                        elif cmd == "lurking on":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil diaktifkan, selanjutnya ketik lurkers\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurking off":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 cl.sendText(msg.to, "「 Status Lurking 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurkers":
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  「 Daftar Member 」    \n\n 「 Total {} Sider 」\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                              print("SIDER AKTIF")
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil diaktifkan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          print("SIDER DI MATIKAN")
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nDaftar yang terlihat\n"+cctv['sidermem'][msg.to])
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("spamtag: "):
                          print("SPAM TAG JUMLAH")
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["limit"] = num
                                cl.sendText(msg.to,"「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamcall: "):
                          print("SPAM CALL JUMLAH")
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                IdKu["limit"] = num
                                cl.sendText(msg.to,"「 Status Spamcall 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamtag "):
                          print("SPAM TAG MEMBER")
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["SKlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          print("SPAM CALL")
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(InexWar["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd.startswith("spamcall "):
                          print("SPAM CALL GRUP")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jumlah = int(strnum)
                                cl.sendText(msg.to,"Undangan call grup {} sukses".format(str(strnum)))
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           call.acquireGroupCallRoute(to)
                                           call.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              cl.sendText(msg.to,"「 Spam Gift 」\nBerhasil spamgift {} kali".format(str(jumlah)))
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ka.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if IdKu["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["SKmessage1"]))
                                      ka.sendMessage(midd, str(Setmain["SKmessage1"]))
                                      kb.sendMessage(midd, str(Setmain["SKmessage1"]))

#=========== [ Add Image ] ============#
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                IdKu["Addimage"]["status"] = True
                                IdKu["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendText(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendText(to, ret_)
#===========KICKOUT============#
                        elif cmd.startswith('kick '):
                          if msg._from in admin:
                            print("INDUK KICK MEMBER")
                            #if msg.toType != 2: return cl.sendMessage(to, 'Failed vultra kick member, use this command only on group chat')
                            if 'MENTION' in msg.contentMetadata.keys():
                                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                for mention in mentions['MENTIONEES']:
                                    _mid = mention['M']
                                    if _mid == [_mid]:
                                        continue
                                    try:
                                        cl.idbotsKick(to, [_mid])                                        
                                        cl.idbotsInvite(to, [_mid])
                                        cl.idbotsCancel(to, [_mid])
                                    except TalkException as talk_error:
                                        return cl.sendMessage(to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)
                                    time.sleep(0.8)
                                cl.sendMessage(to, 'Success vultra kick members, totals %i members' % len(mentions['MENTIONEES']))
                            else:
                                cl.sendMessage(to, 'Failed vultra kick member, please mention user you want to kick')

                        elif cmd.startswith("go "):
                          print("BOT KICK MEMBER")
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        Idbots["blacklist"][ls] = True
                                        Idbots["rblacklist"][ls] = True
                                        mbut=[ka,kb,kc,kd,ke,kf,kg]
                                        jembut = random.choice(mbut)
                                        jembut.idbotsKick(to,[ls])
                                        print (to,[ls])
                                    except:
                                    	pass
                                           
                        elif "Cling" in msg.text:
                          print("KICK ALL MEMBER")
                          if msg._from in admin:
                            if msg.toType == 2:
                                _name = msg.text.replace("Cling","")
                                gs = cl.getGroup(msg.to)
                                gs = ka.getGroup(msg.to)
                                gs = kb.getGroup(msg.to)
                                gs = kc.getGroup(msg.to)
                                gs = kd.getGroup(msg.to)
                                gs = ke.getGroup(msg.to)
                                gs = kf.getGroup(msg.to)
                                gs = kg.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Not Found")
                                else:
                                    for target in targets:
                                        if not target in Bots:
                                            try:
                                               mbut=[ka,kb,kc,kd,ke,kf,kg]
                               	               jembut=random.choice(mbut)
                                               jembut.idbotsKick(msg.to,[target])
                                               print (msg.to,[g.mid])
                                               print("KICK ALL MEMBER SUCCESS")
                                            except:
                                                pass

                        elif text.lower() == 'prank':
                           print("KICK ALL MEMBER DARI LUAR GRUP")
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('prank','')
                                  gs = ka.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = kd.getGroup(msg.to)
                                  gs = ke.getGroup(msg.to)
                                  gs = kf.getGroup(msg.to)
                                  gs = kg.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "....")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      Bot = [ka,kb,kc,kd,ke,kf,kg]
                                                      Botak = random.choice(Bot)
                                                      Botak.idbotsKick(msg.to, [target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Mbut:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Mbut:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Mbut:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                IdKu["addadmin"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "admin:expell" or text.lower() == 'admin:expell':
                            if msg._from in admin:
                                IdKu["delladmin"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                IdKu["addstaff"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "staff:expell" or text.lower() == 'staff:expell':
                            if msg._from in admin:
                                IdKu["dellstaff"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                IdKu["addbots"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "bot:expell" or text.lower() == 'bot:expell':
                            if msg._from in admin:
                                IdKu["dellbots"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          print("UNSEND AKTIF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["unsend"] = True
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", "\nSilahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          print("UNSEND OFF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["unsend"] = False
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", " \nDeteksi unsend dinonaktifkan")
                                
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          print("CEK TIMELINE ON")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Timeline"] = True
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          print("CEK TIMELINE OFF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Timeline"] = False
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["invite"] = True
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["invite"] = False
                                sendMention(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Mentionkick"] = True
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Mentionkick"] = False
                                cl.sendText(msg.to,"「 Status Notag 」\nNotag telah dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["contact"] = True
                                sendMention(msg.to, sender, "「 Status Contact 」\nUser ", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik contact off")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["contact"] = False
                                cl.sendText(msg.to,"「 Status Contact 」\nDeteksi contact dinonaktifkan")

                        elif cmd == "r1 on" or text.lower() == 'respon1 on':
                          print("RESPON DI GRUP ON")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["detectMention"] = True
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon diaktifkan")

                        elif cmd == "r1 off" or text.lower() == 'respon1 off':
                          print("RESPON DI GRUP OFF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["detectMention"] = False
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon dinonaktifkan")

                        elif cmd == "r2 on" or text.lower() == 'respon1 on':
                          print("RESPON DI GRUP ON")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["arespon"] = True
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon diaktifkan")

                        elif cmd == "r2 off" or text.lower() == 'respon1 off':
                          print("RESPON DI GRUP OFF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["arespon"] = False
                                cl.sendText(msg.to,"「 Status Respon 」\nAuto respon dinonaktifkan")

                        elif cmd == "r3 on" or text.lower() == 'respon2 on':
                          print("RESPON DI PM ON")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Mentiongift"] = True
                                cl.sendText(msg.to,"「 Status Respon Gift 」\nAuto respon1 diaktifkan")

                        elif cmd == "r3 off" or text.lower() == 'respon2 off':
                          print("RESPON DI PM OFF")
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Mentiongift"] = False
                                cl.sendText(msg.to,"「 Status Respon Gift 」\nAuto respon1 dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoJoin"] = True
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoJoin"] = False
                                cl.sendText(msg.to,"「 Status Autojoin 」\nAutojoin telah dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoLeave"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoLeave"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoBlock"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoBlock"] = False
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoAdd"] = True
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["autoAdd"] = False
                                cl.sendText(msg.to,"「 Status Autoadd 」\nAutoadd telah dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["stickerOn"] = True
                                sendMention(msg.to, sender, "「 Status Sticker Check 」\n", " [ ON ]\nSilahkan kirim stickernya,\nJika sudah selesai, ketik sticker off")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["stickerOn"] = False
                                cl.sendText(msg.to,"「 Status Sticker Check 」\nSticker check dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Idbots["autoJoinTicket"] = True
                                sendMention(msg.to, sender, "「 Status Jointicket 」\nUser ", "\nSilahkan kirim link grupnya,\nJika sudah selesai, ketik jointicket off")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                Idbots["autoJoinTicket"] = False
                                cl.sendText(msg.to,"「 Status Jointicket 」\nJointicket telah dinonaktifkan")
                                
                        elif cmd == "kick on":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               IdKu["Kickallmember"] = True
                               cl.sendMessage(msg.to,"Status:\nDiaktifkan")
                                
                        elif cmd == "kick off":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               IdKu["Kickallmember"] = False
                               cl.sendMessage(msg.to,"Status:\nDinonaktifkan")
                                
                        elif cmd == "on":
                           if msg._from in admin:
                              protectqr.append(msg.to)
                              protectkick.append(msg.to)
                              protectinvite.append(msg.to)
                              protectcancel.append(msg.to)
                              protectjs.append(msg.to)
                              cl.sendMessage(msg.to, "Bot aktif")

                        elif cmd == "off":
                           if msg._from in admin:
                              protectqr.remove(msg.to)
                              protectkick.remove(msg.to)
                              protectinvite.remove(msg.to)
                              protectcancel.remove(msg.to)
                              protectjs.remove(msg.to)
                              cl.sendMessage(msg.to, "Bot off")

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in antijs:
                                       msgs = "Protectjs has been active"
                                  else:
                                       antijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti kicker \n\naktif di group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "active\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in antijs:
                                         antijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti kicker off\n\ndi group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti kicker off "
                                    cl.sendMessage(msg.to, "nonactive\n" + msgs)

                        elif cmd == "listprotect":
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = antijs
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"☠•➤Protection\n\n☠•➤PROTECT URL :\n"+ma+"\n☠•➤PROTECT JOIN :\n"+mb+"\n☠•➤ANTIJS :\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectjoin)+len(antijs))))

                        elif 'Ghost ' in msg.text:
                          if msg._from in admin:
                             spl = msg.text.replace('Ghost ','')
                             if spl == 'on':
                                 if msg.to in ghost:
                                      msgs = "Ghost sudah aktif"
                                 else:
                                        ghost.append(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                 cl.sendMessage(msg.to, "Status:\n" + msgs)
                             elif spl == 'off':
                                   if msg.to in ghost:
                                        ghost.remove(msg.to)
                                        ginfo = cl.getGroup(msg.to)
                                        msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                   else:
                                        msgs = "Ghost Sudah Tidak Aktif"
                                   cl.sendMessage(msg.to, "Status:\n" + msgs)

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           IdKu["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan talkban")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del IdKu["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus talkban")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Talkwblacklist"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["Talkdblacklist"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif ("Ban " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Idbots["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Idbots["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["wblacklist"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                                IdKu["dblacklist"] = True
                                sendMention(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              if Idbots["blacklist"] == {}:
                                cl.sendMessage(msg.to,"「 Nothing Blacklist 」")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Idbots["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Blacklist 」\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(Idbots["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              if IdKu["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in IdKu["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Talkban 」\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(InexWar["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              if Idbots["rblacklist"] == {}:
                                    cl.sendMessage(msg.to,"「 Nothing Blacklist 」")
                              else:
                                    ma = ""
                                    for i in Idbots["rblacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if IdKu["selfbot"] == True:
                            if msg._from in admin:
                              Idbots["blacklist"] = {}
                              Idbots["rblacklist"] = {}
                              Idbots["mblacklist"] = {}
                              cl.sendMessage(msg.to,"Succes Clear Blacklist ...")     
                   
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  IdKu["message"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nPesan Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  IdKu["welcome"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nWelcome Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  IdKu["leave"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nLeave Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set r1: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r1: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  IdKu["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nRespon Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set r2: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set r2: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  IdKu["Responpm"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nRespon Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  IdKu["SKmessage1"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSpam Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  IdKu["mention"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSider Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Message 」\nPesan Msg mu :\n\n" + str(InexWar["message"]))

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Welcome 」\nWelcome Msg mu :\n\n" + str(InexWar["welcome"]))

                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Leave 」\nLeave Msg mu :\n\n" + str(InexWar["leave"]))

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Respon 」\nRespon Msg mu :\n\n" + str(InexWar["Respontag"])+str(InexWar["Responpm"]))

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Spam 」\nSpam Msg mu :\n\n" + str(Setmain["SKmessage1"]))

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Sider 」\nSider Msg mu :\n\n" + str(InexWar["mention"]))

    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
