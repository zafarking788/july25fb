try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bxin
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bxin')
    os.system('pkg install nodejs')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'})
os.system('clear')

##### LOGO #####
logo='''
\033[91m
\033[91m  _____           _        _ _         _____ _         
\033[92m / ____|         | |      | (_)       |_   _| |        
\033[95m | |     __ _ ___| |_ __ _| |_  __ _    | | | | __ ____
\033[95m | |    / _` / __| __/ _` | | |/ _` |   | | | |/ /|_  /
\033[92m | |___| (_| \__ \ || (_| | | | (_| |_ _| |_|   <  / / 
\033[91m  \_____\__,_|___/\__\__,_|_|_|\__,_(_)_____|_|\_\/___|
\033[92m  XamppGangstaTeam>_/Kagurazaga_ikz
--------------------------------------------------

\033[94m*Auther   : Castalia.Ikz
\033[91m*Facebook : Bagaskurniawan EX
\033[92m*Github   : github.com/Castalia
\033[93m*Website  : xampp-cyber.my.id

