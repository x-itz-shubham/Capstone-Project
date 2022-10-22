from pyfiglet import figlet_format
from IPlocator import iptrack
from IMDB import scrap
from portscanner import pscan
from MD5 import crypto
from Phonenumber import numberinfo
from speechtest import speech
from snif import sniffing
from logkey import key
from SocialRecon import recon

Title = figlet_format("-x-DeAd EyEs-x-")
print(Title)
while True:
    print("----Choose from the below given options-----")
    print("1.Scrapping\n2.Speech Recognition\n3.Key Logger\n4.Cryptography\n5.Port Scanner\n"
          "6.PhoneNumber Information \n7.Ip Tracker\n8.Social Name Recon\n9.Sniffing\n10.EXIT")
    choice = int(input("Choose one from above:-"))
    if choice == 1:
        scrap()
        break
    elif choice == 2:
        speech()
        break
    elif choice == 3:
        key()
        break
    elif choice == 4:
        crypto()
        break
    elif choice == 5:
        pscan()
        break
    elif choice == 6:
        numberinfo()
        break
    elif choice == 7:
        iptrack()
        break
    elif choice == 8:
        recon()
        break
    elif choice == 9:
        sniffing('Wi-Fi')
        break
    elif choice == 10:
        cont = input("Do you want to continue:?(y/n):")
        cont = cont.lower()
        if cont != 'y':
            print("Exiting Program...")
            break
