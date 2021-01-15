import os
import time

#colors from:twiiter@Xcodeone1
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray

print(G+"[+]Start now")

def logo():
    os.system("clear")

    print(G+'''
             _nnnn_                      
            dGGGGMMb     ,"""""""""""""".
           @p~qp~~qMb    | Kali  Linux! |
           M|@||@) M|   _;..............'
           @,----.JM| -'
          JS^\__/  qKL
         dZP        qKRb
        dZP          qKKb
       fZP            SMMb
       HZM            MMMM
       FqM            MMMM
     __| ".        |\dS"qML
     |    `.       | `' \Zq
    _)      \.___.,|     .'
    \____   )MMMMMM|   .'
         `-'       `--' 
        twitter:@ip_274  
    ''')
    print("\n")

logo()

print("Options:")
print(G + "[01]- update sources.list")
print(G + "[02]- update kali linux")
print(G + "[03]- upgrade kali linux")
print(G + "[04]- all the above")
print(G + "[05]- update to kali linux 2020.4")
print(G + "[06]- get info about kali linux")
print(R + "[00]- Exit")
print("\n")
what_you_wnat = str(input(C+"The service you want is? "))





def update_sources_list():
    
    logo()
    print(G+"--------------------------")
    print(G+"[+]Start update sources.list now")
    print(G+"--------------------------")
    print("\n")
    
    print(GR)
    os.system("echo ''deb http://http.kali.org/kali kali-rolling main non-free contrib'' | sudo tee /etc/apt/sources.list")
    os.system("echo ''deb http://http.kali.org/kali kali-last-snapshot main non-free contrib'' | sudo tee /etc/apt/sources.list")
    os.system("echo ''deb http://http.kali.org/kali kali-experimental main non-free contrib'' | sudo tee -a /etc/apt/sources.list")
    os.system("echo ''deb-src http://http.kali.org/kali kali-rolling main non-free contrib'' | sudo tee -a /etc/apt/sources.list")

    #print("\n")
    #print(G+"--------------------------")
    #print(G+"[+]check sources.list")
    #print(G+"--------------------------")
    #os.system("sudo cat /etc/apt/sources.list")

    print("\n")
    print(G+"Done,Enjoy")

def update_kali_linux():
    logo()

    print(G+"--------------------------")
    print(G+"[+]Start update kali linux now")
    print(G+"--------------------------")
    print("\n")

    print(GR)
    os.system("sudo apt-get update")

    print("\n")
    print(G+"Done,Enjoy")

def upgrade_kali_linux():
    logo()

    print(G+"--------------------------")
    print(G+"[+]Start upgrade kali linux now")
    print(G+"--------------------------")
    print("\n")

    print(GR)
    os.system("sudo apt -y full-upgrade")

    print("\n")
    print(G+"Done,Enjoy")

def all():
    logo()

    print(G+"--------------------------")
    print(G+"[+]Start update now")
    print(G+"--------------------------")
    print("\n")

    print(G+"[+]Start update sources.list now","\n")
    print(GR)
    os.system("echo ''deb http://http.kali.org/kali kali-rolling main non-free contrib'' | sudo tee /etc/apt/sources.list")
    os.system("echo ''deb http://http.kali.org/kali kali-last-snapshot main non-free contrib'' | sudo tee /etc/apt/sources.list")
    os.system("echo ''deb http://http.kali.org/kali kali-experimental main non-free contrib'' | sudo tee -a /etc/apt/sources.list")
    os.system("echo ''deb-src http://http.kali.org/kali kali-rolling main non-free contrib'' | sudo tee -a /etc/apt/sources.list")
    print("\n")

    print(G+"[+]Start update kali linux now","\n")
    print(GR)
    os.system("sudo apt-get update")
    print("\n")

    print(G+"[+]Start upgrade kali linux now","\n")
    print(GR)
    os.system("sudo apt -y full-upgrade")

    print("\n")
    print(G+"Done,Enjoy")

def update_to_kali_linux_2020_4():
    logo()


    print(G+"------------------------------------------")
    print(G+"[+]Start update kali linux to 2020.4 now")
    print(G+"------------------------------------------")
    print("\n") 

    print(GR)
    #make kali linux ready for upgrade
    all()

    #for 2020.4
    os.system("echo ''deb http://http.kali.org/kali kali-rolling main non-free contrib'' | sudo tee /etc/apt/sources.list")
    os.system("sudo apt update && sudo apt -y full-upgrade")
    os.system("cp -i /etc/skel/.bashrc ~/")
    os.system("cp -i /etc/skel/.zshrc ~/")
    os.system("chsh -s /bin/zsh")
    os.system("[ -f /var/run/reboot-required ]")
    os.system("sudo reboot -f")

    print("\n")
    print(G+"Done,Enjoy")

def info_about_kali():
    logo()

    print(G+"--------------------------")
    print(G+"[+]Start get info now")
    print(G+"--------------------------")
    print("\n") 
    time.sleep(0.5)
    print(GR)
    os.system("grep VERSION /etc/os-release")

    print("\n")
    print(G+"Done,Enjoy")


if what_you_wnat == "01" or what_you_wnat == "1":
    print("\n")
    update_sources_list()
elif  what_you_wnat == "02" or what_you_wnat == "2":
    print("\n")
    update_kali_linux()
elif  what_you_wnat == "03" or what_you_wnat == "3":
    print("\n")
    upgrade_kali_linux()
elif  what_you_wnat == "04" or what_you_wnat == "4":
    print("\n")
    all()
elif  what_you_wnat == "05" or what_you_wnat == "5":
    print("\n")
    update_to_kali_linux_2020_4()
elif  what_you_wnat == "06" or what_you_wnat == "6":
    print("\n")
    info_about_kali()
elif  what_you_wnat == "00" or what_you_wnat == "0":
    print("\n")
    print(G+"GoodBye")
else:
    print("\n")
    print(R+"Sorry, there is a problem. Make sure to enter the correct number")


time.sleep(0.5)
