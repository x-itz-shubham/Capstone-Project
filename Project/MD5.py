import hashlib
import os
from time import sleep
from pyfiglet import figlet_format
#from os import system
import subprocess


def crypto():
    def ceaser():
        sleep(1)
        subprocess.call("cls", shell=True)

        def encrypt():
            # get input from the user
            plaintxt = input("Enter the text to be encrypted:")

            # empty string to manipulate the original text
            ciphertxt = ""

            # main logic
            for alpha in plaintxt:
                alpha_code = ord(alpha)  # put the character code of the particular character in alpha_code
                enc_alpha_code = alpha_code + 3 % 26  # encryption is done by adding +3 in the character code and taking modulus of that character
                new_alpha = chr(enc_alpha_code)  # whatever the character code we will get we use the char() to determine the character of which it holds the value
                ciphertxt += new_alpha  # stores the complete cipher text of the plain text we entered

            print(ciphertxt + "\n\n")

        # decryption
        def decrypt():
            # get input from the user
            ciphertxt = input("Enter the text to be decrypted:")

            # empty string to manipulate the original text
            plaintxt = ""

            # main logic
            for alpha in ciphertxt:
                alpha_code = ord(alpha)  # put the character code of the particular character in alpha_code
                enc_alpha_code = alpha_code - 3 % 26  # encryption is done by adding +3 in the character code and taking modulus of that character
                new_alpha = chr(enc_alpha_code)  # whatever the character code we will get we use the char() to determine the character of which it holds the value
                plaintxt += new_alpha  # stores the complete cipher text of the plain text we entered

            print(plaintxt + "\n")

        banner = figlet_format("Ceaser Cipher")
        print(banner)
        while True:
            print("1.Encrypt a message\n2.Decrypt a message\n3.Main Menu")
            select = int(input("Choose one from above:-"))
            if select == 1:
                encrypt()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning To Main Menu")
                    crypto()
            elif select == 2:
                decrypt()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning To Main Menu")
                    crypto()
            elif select == 3:
                print("Returning to Main Menu")
                sleep(1)
                os.system('cls')
                crypto()

    def md5():
        sleep(1)
        subprocess.call("clear", shell=True)

        def md5encryption():
            plain_text = input("Enter String to be MD5 Hashed:- ")
            encrypt = hashlib.md5()
            encrypt.update(plain_text.encode())
            cipher = encrypt.hexdigest()
            print(f'{plain_text} to MD5 hash:- {cipher}')

        def md5decryption():
            count = 0
            hash = input("Paste MD5 hash:- ")
            with open('rockyou.txt', 'r', errors='ignore') as wordlist:
                for word in wordlist:
                    key_encrypt = word.encode('utf-8')
                    key_hash = hashlib.md5(key_encrypt.strip())     # make hash of all the words present in the text file
                    key_hash = key_hash.hexdigest()
                    count += 1
                    if key_hash == hash:                            # compare all the hashes made from the wordlist with the actual hash we provide
                        print(" ")
                        print("Hash Found!")
                        print(f'Hash Cracked:- {word}')
                        print(f'After Analyzing {str(count)} passwords from your file')
                        break
                    else:
                        print('%s %s Not Matched with' % (str(count), word))

        #banner1 = figlet_format("MD 5")
        #print(banner1)
        while True:
            print("1.Encrypt a message\n2.Decrypt a message\n3.Main Menu")
            select = int(input("Choose one from above:-"))
            if select == 1:
                md5encryption()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning To Main Menu")
                    crypto()
            elif select == 2:
                md5decryption()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning To Main Menu")
                    crypto()
            elif select == 3:
                print("Returning to Main Menu")
                sleep(1)
                os.system('cls')
                crypto()

    def sha1():
        sleep(1)
        subprocess.call("clear", shell=True)

        def sha1encryption():
            plain_text = input("Enter String to be Hashed in SHA1:- ")
            encrypt = hashlib.sha1()
            encrypt.update(plain_text.encode())
            cipher = encrypt.hexdigest()
            print(f'{plain_text} to SHA1 hash:- {cipher}')

        def sha1decryption():
            count = 0
            hash = input("Paste SHA1 hash:- ")
            with open('rockyou.txt', 'r', errors='ignore') as wordlist:
                for word in wordlist:
                    key_encrypt = word.encode('utf-8')
                    key_hash = hashlib.sha1(key_encrypt.strip())     # make hash of all the words present in the text file
                    key_hash = key_hash.hexdigest()
                    count += 1
                    if key_hash == hash:                            # compare all the hashes made from the wordlist with the actual hash we provide
                        print(" ")
                        print("Hash Found!")
                        print(f'Hash Cracked:- {word}')
                        print(f'After Analyzing {str(count)} passwords from your file')
                        break
                    else:
                        print('%s %s Not Matched with' % (str(count), word))

        banner2 = figlet_format("SHA 1")
        print(banner2)
        while True:
            print("1.Encrypt a message\n2.Decrypt a message\n3.Main Menu")
            select = int(input("Choose one from above:-"))
            if select == 1:
                sha1encryption()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning to Main Menu")
                    crypto()
            elif select == 2:
                sha1decryption()
                conti = input("Do you want to continue:?(y/n):")
                conti = conti.lower()
                if conti != 'y':
                    print("Returning to Main Menu")
                    crypto()
            elif select == 3:
                print("Returning to Main Menu")
                sleep(1)
                subprocess.call("clear", shell=True)
                crypto()

    title = figlet_format("CyPhEr SuItE☺")
    print(title)
    while True:
        print("1.Ceaser Cipher\n2.MD5\n3.SHA1\n4.EXIT")
        choice = int(input("Choose one from above:-"))
        if choice == 1:
            ceaser()
            print("Returning to Main Menu")
            crypto()
        elif choice == 2:
            md5()
            print("Returning to Main Menu")
            crypto()
        elif choice == 3:
            sha1()
            print("Returning to Main Menu")
            crypto()
        elif choice == 4:
            cont = input("Are you sure you want to Exit:?(y/n):")
            cont = cont.lower()
            if cont != 'n':
                print("Exiting Program...")
                break


if __name__ == "__main__":
    crypto()
