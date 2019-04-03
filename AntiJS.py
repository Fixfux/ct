import ARIFISTIFIK
from ARIFISTIFIK import *
from akad.ttypes import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
#import pyimgflip
from googletrans import Translator
import youtube_dl


cl = LineClient()
#cl = LineClient(authToken='Tokwn Luu')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

k1 = LineClient()
#k1 = LineClient(authToken='Token Luu')
k1.log("Auth Token : " + str(k1.authToken))
channel1 = LineChannel(k1)
k1.log("Channel Access Token : " + str(channel1.channelAccessToken))

k2 = LineClient()
#k2 = LineClient(authToken='Token Luu')
k2.log("Auth Token : " + str(k2.authToken))
channel2 = LineChannel(k2)
k2.log("Channel Access Token : " + str(channel2.channelAccessToken))

k3= LineClient()
#k3 = LineClient(authToken='Token Luu')
k3.log("Auth Token : " + str(k3.authToken))
channel3 = LineChannel(k3)
k3.log("Channel Access Token : " + str(channel3.channelAccessToken))


k4 = LineClient()
#k4 = LineClient(authToken='Token Luu')
k4.log("Auth Token : " + str(k4.authToken))
channel4 = LineChannel(k4)
k4.log("Channel Access Token : " + str(channel4.channelAccessToken))

k5 = LineClient()
#k5 = LineClient(authToken='Token Luu')
k5.log("Auth Token : " + str(k5.authToken))
channel5 = LineChannel(k5)
k5.log("Channel Access Token : " + str(channel5.channelAccessToken))

k6= LineClient()
#k6 = LineClient(authToken='Token Luu')
k6.log("Auth Token : " + str(k6.authToken))
channel6 = LineChannel(k6)
k6.log("Channel Access Token : " + str(channel6.channelAccessToken))

k7 = LineClient()
#k7 = LineClient(authToken='Token Luu')
k7.log("Auth Token : " + str(k7.authToken))
channel7 = LineChannel(k7)
k7.log("Channel Access Token : " + str(channel8.channelAccessToken))

k8 = LineClient()
#k8 = LineClient(authToken='Token Luu')
k8.log("Auth Token : " + str(k8.authToken))
channel8 = LineChannel(k8)
kk.log("Channel Access Token : " + str(channel8.channelAccessToken))

sw= LineClient()
#sw = LineClient(authToken='Token Luu')
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))

print ("SUCCES LOGIN")

poll = LinePoll(cl)
call = cl
creator = [""]
mid = cl.getProfile().mid
Amid = k1.getProfile().mid
Bmid = k2.getProfile().mid
Cmid = k3.getProfile().mid
Dmid = k4.getProfile().mid
Emid = k5.getProfile().mid
Fmid = k6.getProfile().mid
Gmid = k7.getProfile().mid
Hmid = k8.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,k1,k2,k3,k4,k5,k6,k7,k8,sw]
ABC = [k1,k2,k3,k4,k5,k6,k7,k8]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Zmid]
Dpk = creator + owner + admin + staff

responsename1 = k1.getProfile().displayName
responsename2 = k2.getProfile().displayName
responsename3 = k3.getProfile().displayName
responsename4 = k4.getProfile().displayName
responsename5 = k5.getProfile().displayName
responsename6 = k6.getProfile().displayName
responsename7 = k7.getProfile().displayName
responsename8 = k8.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 5,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoRead':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "mention":"Wooooyyyy Ngintip² Baee Sini Gabung Chat Biar Rame...!!!",
    "Respontag":"Ngapain Ngetag² Aim ??? Nakal Yah Sini Tak Cubit...!!!",
    "welcome":"Selamat datang, Salken & semoga betah",
    "comment":"Like like & like by Abi ♡ Riny",
    "message":"Terimakasih sudah add saya 😃",
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

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    owner = json.load(fp)

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

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
        textx = "{}\n\n  [ Mention ]\n1. ".format(str(len(mid)))
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

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Nih Yang Suka Ngintip {} \nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
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
        textx = "{} \nHaii  ".format(str(len(mid)))
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
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
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

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n⏩ Group : "+str(len(gid))+"\n⏩ Teman : "+str(len(teman))+"\n⏩ Expired : In "+hari+"\n⏩ Version : ANTIJS2\n⏩ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n⏩ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "❧MENU HELP❧\n" + \
                  "❧" + key + "Me\n" + \
                  "❧" + key + "Mid「@」\n" + \
                  "❧" + key + "Info「@」\n" + \
                  "❧" + key + "Nk「@」\n" + \
                  "❧" + key + "Kick1「@」\n" + \
                  "❧" + key + "Mybot\n" + \
                  "❧" + key + "Status\n" + \
                  "❧" + key + "About\n" + \
                  "❧" + key + "Restart\n" + \
                  "❧" + key + "Runtime\n" + \
                  "❧" + key + "Creator\n" + \
                  "❧" + key + "Speed/Sp\n" + \
                  "❧" + key + "Sprespon\n" + \
                  "❧" + key + "Tagall\n" + \
                  "❧" + key + "Joinall\n" + \
                  "❧" + key + "Byeall\n" + \
                  "❧" + key + "Byeme\n" + \
                  "❧" + key + "Leave「Namagrup」\n" + \
                  "❧" + key + "Ginfo\n" + \
                  "❧" + key + "Open\n" + \
                  "❧" + key + "Close\n" + \
                  "❧" + key + "Url grup\n" + \
                  "❧" + key + "Gruplist\n" + \
                  "❧" + key + "Infogrup「angka」\n" + \
                  "❧" + key + "Infomem「angka」\n" + \
                  "❧" + key + "Remove chat\n" + \
                  "❧" + key + "Lurking「on/off」\n" + \
                  "❧" + key + "Lurkers\n" + \
                  "❧" + key + "Sider「on/off」\n" + \
                  "❧" + key + "Updatefoto\n" + \
                  "❧" + key + "Updategrup\n" + \
                  "❧" + key + "Updatebot\n" + \
                  "❧" + key + "Broadcast:「Text」\n" + \
                  "❧" + key + "Setkey「New Key」\n" + \
                  "❧" + key + "Mykey\n" + \
                  "❧" + key + "Resetkey\n" + \
                  "❧" + key + "ID line:「Id Line nya」\n" + \
                  "❧" + key + "Sholat:「Nama Kota」\n" + \
                  "❧" + key + "Cuaca:「Nama Kota」\n" + \
                  "❧" + key + "Lokasi:「Nama Kota」\n" + \
                  "❧" + key + "Music:「Judul Lagu」\n" + \
                  "❧" + key + "Lirik:「Judul Lagu」\n" + \
                  "❧" + key + "Ytmp3:「Judul Lagu」\n" + \
                  "❧" + key + "Ytmp4:「Judul Video」\n" + \
                  "❧" + key + "Profileig:「Nama IG」\n" + \
                  "❧" + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "❧" + key + "Jumlah:「angka」\n" + \
                  "❧" + key + "Spamtag「@」\n" + \
                  "❧" + key + "Spamcall:「jumlahnya」\n" + \
                  "❧" + key + "Spamcall\n" + \
                  "❧" + key + "Notag「on/off」\n" + \
                  "❧" + key + "Allpro「on/off」\n" + \
                  "❧" + key + "Protecturl「on/off」\n" + \
                  "❧" + key + "Protectjoin「on/off」\n" + \
                  "❧" + key + "Protectkick「on/off」\n" + \
                  "❧" + key + "Protectcancel「on/off」\n" + \
                  "❧" + key + "Antijs「on/off」\n" + \
                  "❧" + key + "Antijs stay\n" + \
                  "❧" + key + "Ghost「on/off」\n" + \
                  "❧" + key + "Sticker「on/off」\n" + \
                  "❧" + key + "Respon「on/off」\n" + \
                  "❧" + key + "Contact「on/off」\n" + \
                  "❧" + key + "Autojoin「on/off」\n" + \
                  "❧" + key + "Autoadd「on/off」\n" + \
                  "❧" + key + "Welcome「on/off」\n" + \
                  "❧" + key + "Autoleave「on/off」\n" + \
                  "❧" + key + "Admin:on\n" + \
                  "❧" + key + "Admin:repeat\n" + \
                  "❧" + key + "Staff:on\n" + \
                  "❧" + key + "Staff:repeat\n" + \
                  "❧" + key + "Bot:on\n" + \
                  "❧" + key + "Bot:repeat\n" + \
                  "❧" + key + "Adminadd「@」\n" + \
                  "❧" + key + "Admindell「@」\n" + \
                  "❧" + key + "Staffadd「@」\n" + \
                  "❧" + key + "Staffdell「@」\n" + \
                  "❧" + key + "Botadd「@」\n" + \
                  "❧" + key + "Botdell「@」\n" + \
                  "❧" + key + "Refresh\n" + \
                  "❧" + key + "Listbot\n" + \
                  "❧" + key + "Listadmin\n" + \
                  "❧" + key + "Listprotect\n" + \
                  "❧JANGAN TYPO❧"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "❧HELP BOT❧\n" + \
                  "❧" + key + "Blc\n" + \
                  "❧" + key + "Ban:on\n" + \
                  "❧" + key + "Unban:on\n" + \
                  "❧" + key + "Ban「@」\n" + \
                  "❧" + key + "Unban「@」\n" + \
                  "❧" + key + "Talkban「@」\n" + \
                  "❧" + key + "Untalkban「@」\n" + \
                  "❧" + key + "Talkban:on\n" + \
                  "❧" + key + "Untalkban:on\n" + \
                  "❧" + key + "Banlist\n" + \
                  "❧" + key + "Talkbanlist\n" + \
                  "❧" + key + "Clearban\n" + \
                  "❧" + key + "Refresh\n" + \
                  "❧" + key + "Cek sider\n" + \
                  "❧" + key + "Cek spam\n" + \
                  "❧" + key + "Cek pesan \n" + \
                  "❧" + key + "Cek respon \n" + \
                  "❧" + key + "Cek welcome\n" + \
                  "❧" + key + "Set sider:「Text」\n" + \
                  "❧" + key + "Set spam:「Text」\n" + \
                  "❧" + key + "Set pesan:「Text」\n" + \
                  "❧" + key + "Set respon:「Text」\n" + \
                  "❧" + key + "Set welcome:「Text」\n" + \
                  "❧" + key + "Myname:「Nama」\n" + \
                  "❧" + key + "Bot1name:「Nama」\n" + \
                  "❧" + key + "Bot2name:「Nama」\n" + \
                  "❧" + key + "Bot3name:「Nama」\n" + \
                  "❧" + key + "Bot1up「Kirim fotonya」\n" + \
                  "❧" + key + "Bot2up「Kirim fotonya」\n" + \
                  "❧" + key + "Bot3up「Kirim fotonya」\n" + \
                  "❧" + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "❧" + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "❧ANTI JS V-2❧"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in Setmain["pro"]["qr"]:
                try:
                    if k6.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                            k6.reissueGroupTicket(op.param1)
                            X = k6.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            k6.updateGroup(X)
                            random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                            Setmain["daftar"]["blacklist"][op.param2] = True
                            f = codecs.open("setting.json","w","utf-8")
                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                            k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if k1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                                k1.reissueGroupTicket(op.param1)
                                X = k1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                k1.updateGroup(X)
                                random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                                Setmain["daftar"]["blacklist"][op.param2] = True
                                f = codecs.open("setting.json","w","utf-8")
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if k2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                                    k2.reissueGroupTicket(op.param1)
                                    X = k2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    k2.updateGroup(X)
                                    random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                                    Setmain["daftar"]["blacklist"][op.param2] = True
                                    f = codecs.open("setting.json","w","utf-8")
                                    k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if k3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                                        k3.reissueGroupTicket(op.param1)
                                        X = k3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        k3.updateGroup(X)
                                        random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                                        Setmain["daftar"]["blacklist"][op.param2] = True
                                        f = codecs.open("setting.json","w","utf-8")
                                        k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if k4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                                            k4.reissueGroupTicket(op.param1)
                                            X = k4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            k4.updateGroup(X)
                                            random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                                            Setmain["daftar"]["blacklist"][op.param2] = True
                                            f = codecs.open("setting.json","w","utf-8")
                                            k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if k5.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                                                k5.reissueGroupTicket(op.param1)
                                                X = k5.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                k5.updateGroup(X)
                                                random.choice(ABC).kickoutFromFoup(op.param1,[op.param2])
                                                Setmain["daftar"]["blacklist"][op.param2] = True
                                                f = codecs.open("setting.json","w","utf-8")
                                                k1.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k1.acceptGroupInvitation(op.param1)
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k2.acceptGroupInvitation(op.param1)
                        k2.leaveGroup(op.param1)
                    else:
                        k2.acceptGroupInvitation(op.param1)
                        
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k3.acceptGroupInvitation(op.param1)
                        k3.leaveGroup(op.param1)
                    else:
                        k3.acceptGroupInvitation(op.param1)
                        
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k4.acceptGroupInvitation(op.param1)
                        k4.leaveGroup(op.param1)
                    else:
                        k4.acceptGroupInvitation(op.param1)
                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k5.acceptGroupInvitation(op.param1)
                        k5.leaveGroup(op.param1)
                    else:
                        k5.acceptGroupInvitation(op.param1)
                        
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k6.acceptGroupInvitation(op.param1)
                        k6.leaveGroup(op.param1)
                    else:
                        k6.acceptGroupInvitation(op.param1)
                        
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k7.acceptGroupInvitation(op.param1)
                        k7.leaveGroup(op.param1)
                    else:
                        k7.acceptGroupInvitation(op.param1)
                        

            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k8.acceptGroupInvitation(op.param1)
                        k8.leaveGroup(op.param1)
                    else:
                        k8.acceptGroupInvitation(op.param1)
                        
        if op.type == 13:
            if op.param1 in Setmain["pro"]["invite"]:
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    try:
                        group = k2.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            k2.cancelGroupInvitation(op.param1,[_mid])
                        Setmain["daftar"]["blacklist"][op.param2] = True
                        f = codecs.open("setting.json","w","utf-8")
                        json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    except:
                        try:
                            group = k3.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                k3.cancelGroupInvitation(op.param1,[_mid])
                            Setmain["daftar"]["blacklist"][op.param2] = True
                            f = codecs.open("setting.json","w","utf-8")
                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                        except:
                            try:
                                group = k4.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    k4.cancelGroupInvitation(op.param1,[_mid])
                                Setmain["daftar"]["blacklist"][op.param2] = True
                                f = codecs.open("setting.json","w","utf-8")
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                            except:
                                try:
                                    group = k5.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        k5.cancelGroupInvitation(op.param1,[_mid])
                                    Setmain["daftar"]["blacklist"][op.param2] = True
                                    f = codecs.open("setting.json","w","utf-8")
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                except:
                                    try:
                                        group = k6.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            k6.cancelGroupInvitation(op.param1,[_mid])
                                        Setmain["daftar"]["blacklist"][op.param2] = True
                                        f = codecs.open("setting.json","w","utf-8")
                                        json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    except:
                                        try:
                                            group = k7.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                k7.cancelGroupInvitation(op.param1,[_mid])
                                            Setmain["daftar"]["blacklist"][op.param2] = True
                                            f = codecs.open("setting.json","w","utf-8")
                                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        except:
                                            try:
                                                group = k8.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    k8.cancelGroupInvitation(op.param1,[_mid])
                                                Setmain["daftar"]["blacklist"][op.param2] = True
                                                f = codecs.open("setting.json","w","utf-8")
                                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            except:
                                                try:
                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                    Setmain["daftar"]["blacklist"][op.param2] = True
                                                    f = codecs.open("setting.json","w","utf-8")
                                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                                except:
                                                    pass

        if op.type == 17:
            if op.param2 in Setmain["daftar"]["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in Setmain["pro"]["join"]:
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        if op.param3 not in Setmain["daftar"]["blacklist"]:
                        	k1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Setmain["daftar"]["blacklist"]:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Setmain["daftar"]["blacklist"]:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Setmain["daftar"]["blacklist"]:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in Setmain["daftar"]["blacklist"]:
                                            k5.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in Setmain["daftar"]["blacklist"]:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in Setmain["daftar"]["blacklist"]:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in Setmain["daftar"]["blacklist"]:
                                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in Setmain["pro"]["kick"]:
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in Setmain["pro"]["js"]:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)                   
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        Setmain["daftar"]["blacklist"][op.param2] = True
                        f = codecs.open("setting.json","w","utf-8")
                        json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[Zmid])
                        #ki.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                      #  k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[Zmid])
                        #k1.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    if op.param3 in Setmain["daftar"]["admin"]:
                        if op.param1 in Setmain["daftar"]["antijs"]:
                            Setmain["daftar"]["blacklist"][op.param2] = True
                            f = codecs.open("setting.json","w","utf-8")
                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.findAndAddContactsByMid(op.param3)
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            #cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in Setmain["pro"]["cancel"]:
                if op.param2 not in Bots and op.param2 not in Setmain["daftar"]["bot"] and op.param2 not in Setmain["daftar"]["admin"]:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        if op.param3 not in Setmain["daftar"]["blacklist"]:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Setmain["daftar"]["blacklist"]:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Setmain["daftar"]["blacklist"]:
                                    k6.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Setmain["daftar"]["blacklist"]:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in Setmain["daftar"]["blacklist"]:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in Setmain["daftar"]["blacklist"]:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.inviteIntoGroup(op.param1,[op.param3])
                            k1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    k1.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        k1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            k1.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k8.kickoutFromGroup(op.param1,[op.param2])
                                                k8.inviteIntoGroup(op.param1,[op.param3])
                                                k1.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                                    k1.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k6.kickoutFromGroup(op.param1,[op.param2])
                        k6.inviteIntoGroup(op.param1,[op.param3])
                        k2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k5.kickoutFromGroup(op.param1,[op.param2])
                            k5.inviteIntoGroup(op.param1,[op.param3])
                            k2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k4.kickoutFromGroup(op.param1,[op.param2])
                                k4.inviteIntoGroup(op.param1,[op.param3])
                                k2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                    k2.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k1.kickoutFromGroup(op.param1,[op.param2])
                                        k1.inviteIntoGroup(op.param1,[op.param3])
                                        k2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k8.kickoutFromGroup(op.param1,[op.param2])
                                            k8.inviteIntoGroup(op.param1,[op.param3])
                                            k2.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                                k7.inviteIntoGroup(op.param1,[op.param3])
                                                k2.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k6.kickoutFromGroup(op.param1,[op.param2])
                                                    k6.inviteIntoGroup(op.param1,[op.param3])
                                                    k2.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k5.kickoutFromGroup(op.param1,[op.param2])
                        k5.inviteIntoGroup(op.param1,[op.param3])
                        k3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k4.kickoutFromGroup(op.param1,[op.param2])
                            k4.inviteIntoGroup(op.param1,[op.param3])
                            k3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    k3.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        k3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[op.param3])
                                            k3.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                k6.inviteIntoGroup(op.param1,[op.param3])
                                                k3.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                                    k3.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k3.kickoutFromGroup(op.param1,[op.param2])
                        k3.inviteIntoGroup(op.param1,[op.param3])
                        k4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k2.kickoutFromGroup(op.param1,[op.param2])
                            k2.inviteIntoGroup(op.param1,[op.param3])
                            k4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k1.kickoutFromGroup(op.param1,[op.param2])
                                k1.inviteIntoGroup(op.param1,[op.param3])
                                k4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k8.kickoutFromGroup(op.param1,[op.param2])
                                    k8.inviteIntoGroup(op.param1,[op.param3])
                                    k4.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,[op.param3])
                                        k4.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k6.kickoutFromGroup(op.param1,[op.param2])
                                            k6.inviteIntoGroup(op.param1,[op.param3])
                                            k4.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k5.kickoutFromGroup(op.param1,[op.param2])
                                                k5.inviteIntoGroup(op.param1,[op.param3])
                                                k4.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k3.kickoutFromGroup(op.param1,[op.param2])
                                                    k3.inviteIntoGroup(op.param1,[op.param3])
                                                    k4.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                        k4.inviteIntoGroup(op.param1,[op.param3])
                        k5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                            k3.inviteIntoGroup(op.param1,[op.param3])
                            k5.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                                k2.inviteIntoGroup(op.param1,[op.param3])
                                k5.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                    k5.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k8.kickoutFromGroup(op.param1,[op.param2])
                                        k8.inviteIntoGroup(op.param1,[op.param3])
                                        k5.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,[op.param3])
                                            k5.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k6.kickoutFromGroup(op.param1,[op.param2])
                                                k6.inviteIntoGroup(op.param1,[op.param3])
                                                k5.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                                    k5.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        k2.inviteIntoGroup(op.param1,[op.param3])
                        k6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k1.kickoutFromGroup(op.param1,[op.param2])
                            k1.inviteIntoGroup(op.param1,[op.param3])
                            k6.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k8.kickoutFromGroup(op.param1,[op.param2])
                                k8.inviteIntoGroup(op.param1,[op.param3])
                                k6.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                    k6.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k5.kickoutFromGroup(op.param1,[op.param2])
                                        k5.inviteIntoGroup(op.param1,[op.param3])
                                        k6.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k4.kickoutFromGroup(op.param1,[op.param2])
                                            k4.inviteIntoGroup(op.param1,[op.param3])
                                            k6.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k3.kickoutFromGroup(op.param1,[op.param2])
                                                k3.inviteIntoGroup(op.param1,[op.param3])
                                                k6.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k2.kickoutFromGroup(op.param1,[op.param2])
                                                    k2.inviteIntoGroup(op.param1,[op.param3])
                                                    k6.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        k7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k8.kickoutFromGroup(op.param1,[op.param2])
                            k8.inviteIntoGroup(op.param1,[op.param3])
                            k7.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                                k7.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                    k7.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                        k7.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                            k7.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                                k7.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                                    k7.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,[op.param3])
                        k8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            k6.kickoutFromGroup(op.param1,[op.param2])
                            k6.inviteIntoGroup(op.param1,[op.param3])
                            k8.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                k5.kickoutFromGroup(op.param1,[op.param2])
                                k5.inviteIntoGroup(op.param1,[op.param3])
                                k8.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    k4.kickoutFromGroup(op.param1,[op.param2])
                                    k4.inviteIntoGroup(op.param1,[op.param3])
                                    k8.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        k3.kickoutFromGroup(op.param1,[op.param2])
                                        k3.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            k2.kickoutFromGroup(op.param1,[op.param2])
                                            k2.inviteIntoGroup(op.param1,[op.param3])
                                            k8.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                k1.kickoutFromGroup(op.param1,[op.param2])
                                                k1.inviteIntoGroup(op.param1,[op.param3])
                                                k8.acceptGroupInvitation(op.param1)
                                            except:
                                                try:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                                    k8.acceptGroupInvitation(op.param1)
                                                except:
                                                    pass
                return
            if Setmain["daftar"]["admin"] in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                return
            if Setmain["daftar"]["bot"] in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in Setmain["daftar"]["admin"]:
                    pass
                if op.param2 in Setmain["daftar"]["bot"]:
                    pass
                else:
                    Setmain["daftar"]["blacklist"][op.param2] = True
                    f = codecs.open("setting.json","w","utf-8")
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        k8.kickoutFromGroup(op.param1,[op.param2])
                        k8.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                k6.kickoutFromGroup(op.param1,[op.param2])
                                k6.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    k5.kickoutFromGroup(op.param1,[op.param2])
                                    k5.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        k4.kickoutFromGroup(op.param1,[op.param2])
                                        k4.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            k3.kickoutFromGroup(op.param1,[op.param2])
                                            k3.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                k2.kickoutFromGroup(op.param1,[op.param2])
                                                k2.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)


        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)               
                        
        if op.type == 55:
            if op.param2 in Setmain["daftar"]["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"12842266","STKPKGID":"1318245","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan Pernah Ngetag² Aim...!!!")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n❧STKID : " + msg.contentMetadata["STKID"] + "\n❧STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n❧STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"❧Nama : " + msg.contentMetadata["displayName"] + "\n❧MID : " + msg.contentMetadata["mid"] + "\n❧Status Msg : " + contact.statusMessage + "\n❧Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                   if msg.to in Setmain["kirim"]["idadmin"]:
                     if msg.contentMetadata["mid"] in Setmain["daftar"]["admin"]:
                         cl.sendMessage(msg.to,"{} sudah menjadi admin".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                     else:
                         Setmain["daftar"]["admin"][msg.contentMetadata["mid"]] = True
                         f = codecs.open("setting.json","w","utf-8")
                         json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                         cl.sendMessage(msg.to,"{} diangkat menjadi admin".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                   if msg.to in Setmain["kirim"]["idcadmin"]:
                     if msg.contentMetadata["mid"] not in Setmain["daftar"]["admin"]:
                         cl.sendMessage(msg.to,"{} tidak pernah menjadi admin".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                     else:
                         del Setmain["daftar"]["admin"][msg.contentMetadata["mid"]] = True
                         f = codecs.open("setting.json","w","utf-8")
                         json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                         cl.sendMessage(msg.to,"{} di copot menjadi admin".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                 if msg._from in admin:
                   if msg.to in Setmain["kirim"]["idbot"]:
                     if msg.contentMetadata["mid"] in Setmain["daftar"]["bot"]:
                         cl.sendMessage(msg.to,"{} sudah masuk daftar bot".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                     else:
                         Setmain["daftar"]["bot"][msg.contentMetadata["mid"]] = True
                         f = codecs.open("setting.json","w","utf-8")
                         json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                         cl.sendMessage(msg.to,"{} diangkat menjadi bots".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                   if msg.to in Setmain["kirim"]["idcbot"]:
                     if msg.contentMetadata["mid"] not in Setmain["daftar"]["daftar"]:
                         cl.sendMessage(msg.to,"{} tidak pernah menjadi bots".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
                     else:
                         del Setmain["daftar"]["bot"][msg.contentMetadata["mid"]] = True
                         f = codecs.open("setting.json","w","utf-8")
                         json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                         cl.sendMessage(msg.to,"{} di copot menjadi bots".format(str(cl.getContact(msg.contentMetadata["mid"]).displayName)))
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = k1.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            k1.updateProfilePicture(path)
                            k1.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = k2.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            k2.updateProfilePicture(path)
                            k2.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = k3.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            k3.updateProfilePicture(path)
                            k3.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = k4.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            k4.updateProfilePicture(path)
                            k4.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ARfoto"]:
                            path = k5.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            k5.updateProfilePicture(path)
                            k5.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["ARfoto"]:
                            path = k6.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            k6.updateProfilePicture(path)
                            k6.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["ARfoto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            k7.updateProfilePicture(path)
                            k7.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["ARfoto"]:
                            path = s8.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            s8.updateProfilePicture(path)
                            s8.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "stat":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "❧ĐPĶ PŘØŤĘČŤÎØŇ❧\n"
                                if wait["sticker"] == True: md+="❧Sticker「ON」\n"
                                else: md+="❧Sticker「OFF」\n"
                                if wait["contact"] == True: md+="❧Contact「ON」\n"
                                else: md+="❧Contact「OFF」\n"
                                if wait["talkban"] == True: md+="❧Talkban「ON」\n"
                                else: md+="❧Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="❧Notag「ON」\n"
                                else: md+="❧Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="❧Respon「ON」\n"
                                else: md+="❧Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="❧Autojoin「ON」\n"
                                else: md+="❧Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="❧Autoadd「ON」\n"
                                else: md+="❧Autoadd「OFF」\n"
                                if msg.to in welcome: md+="❧Welcome「ON」\n"
                                else: md+="❧Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="❧Autoleave「ON」\n"
                                else: md+="❧Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="❧Protecturl「ON」\n"
                                else: md+="❧Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="❧Protectjoin「ON」\n"
                                else: md+="❧Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="❧Protectkick「ON」\n"
                                else: md+="❧Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="❧Protectcancel「ON」\n"
                                else: md+="❧Protectcancel「OFF」\n"
                                if msg.to in protectantijs: md+="❧Antijs「ON」\n"
                                else: md+="❧Antijs「OFF」\n"  
                                if msg.to in ghost: md+="❧Ghost「ON」\n"
                                else: md+="❧Ghost「OFF」\n"                                   
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                cl.sendText(msg.to,"Creator Bot Abi ♡ Riny") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               cl.sendMessage1(msg)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "❧Nama : "+str(mi.displayName)+"\n❧Mid : " +key1+"\n❧Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mb":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hc":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "rc":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("bc: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "seger":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "run":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "gi":
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
                                cl.sendMessage(msg.to, "❧ĐPĶ Fams Grup Info\n\n❧Nama Group : {}".format(G.name)+ "\n❧ID Group : {}".format(G.id)+ "\n❧Pembuat : {}".format(G.creator.displayName)+ "\n❧Waktu Dibuat : {}".format(str(timeCreated))+ "\n❧Jumlah Member : {}".format(str(len(G.members)))+ "\n❧Jumlah Pending : {}".format(gPending)+ "\n❧Group Qr : {}".format(gQr)+ "\n❧Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("ig "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
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
                                ret_ += "❧ĐPĶ Fams Grup Info\n"
                                ret_ += "\n❧Nama Group : {}".format(G.name)
                                ret_ += "\n❧ID Group : {}".format(G.id)
                                ret_ += "\n❧Pembuat : {}".format(gCreator)
                                ret_ += "\n❧Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n❧Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n❧Jumlah Pending : {}".format(gPending)
                                ret_ += "\n❧Group Qr : {}".format(gQr)
                                ret_ += "\n❧Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("im "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "❧"+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"❧Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gl":
                          if wait["selfbot"] == True:
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

                        elif cmd == "gl1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gl2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "op":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "cl":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "b1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "b2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "b4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("mn: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b1n: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b2n: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bk: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "jones" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "lb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"❧ĐPĶ  bot\n\n"+ma+"\nTotal「%s」 Bots" %(str(len(Bots))))

                        elif cmd == "la":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"❧ĐPĶ  admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」 Dpk" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "lp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"❧ĐPĶ Fams Protection\n\n❧PROTECT URL :\n"+ma+"\n❧PROTECT KICK :\n"+mb+"\n❧PROTECT JOIN :\n"+md+"\n❧PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "ap":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)

                        elif cmd == "jb":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                try:
                                    anggota = [Bmid,Cmid,Amid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "as":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass
    
                        elif cmd == "jp":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "boo":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                G = cl.getGroup(msg.to)
                                ki.sendText(msg.to, "Bye bye fams "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                
                        elif cmd == "by":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "a1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "a2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "a3":
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

                        elif cmd == "kj":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kb":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sr":
                          if wait["selfbot"] == True:
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
                                cl.sendMessage(msg.to, "❧ĐPĶ Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in Setmain["daftar"]["admin"]::
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lu on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lu":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
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
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "si on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "si off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        
                        
                        elif cmd.startswith("ju: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("sc: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("st "):
                          if wait["selfbot"] == True:
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
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "sc":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Wl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Wl ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pu ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pu ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pk ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pk ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pj ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pj ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Pc ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Pc ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Ap ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ap ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'G ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('G ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'A ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('A ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("N " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("K " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Aad " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
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
                          if wait["selfbot"] == True:
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

                        elif ("Adl " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
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
                                   if target not in Dpk:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
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
                                   if target not in Dpk:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "a:on" or text.lower() == 'a:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "a:re" or text.lower() == 'a:re':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "fr" or text.lower() == 'fr':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "ca" or text.lower() == 'ca':
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
                        elif cmd == "nt on" or text.lower() == 'nt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "nt off" or text.lower() == 'nt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "c on" or text.lower() == 'c on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "c off" or text.lower() == 'c off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "re on" or text.lower() == 're on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "re off" or text.lower() == 're off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "aj on" or text.lower() == 'aj on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "aj off" or text.lower() == 'aj off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "al on" or text.lower() == 'al on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "al off" or text.lower() == 'al off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "aa on" or text.lower() == 'aa on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "aa off" or text.lower() == 'aa off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "ar on" or text.lower() == 'ar on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "ar off" or text.lower() == 'ar off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "str on" or text.lower() == 'str on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "str off" or text.lower() == 'str off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jt on" or text.lower() == 'jt on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jt off" or text.lower() == 'jt off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Autojoin Tiket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"❧ĐPĶ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"❧ĐPĶ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cb" or text.lower() == 'cb':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Sp: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sp: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sw: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sw: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sr: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sr: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ss: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ss: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Si: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Si: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cw":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cr":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cs":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "ci":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
