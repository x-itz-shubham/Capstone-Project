import socket
import sys
from datetime import datetime

# for ASCII Banner include this package
import pyfiglet


def pscan():
    def userdefscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, port)):
            print("The Port {} is open".format(port))
        else:
            print("The Port {} is closed".format(port))

    # scan every port on the target ip
    def scanwhole():
        try:
            for p in range(1, 65535):  # 65535 valid port range
                s = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)  # socket is the class, AF_INET is specifing that we are working with IPv4, SOCK_Stream specifies type of connection like tcp udp
                s.settimeout(0.5)
                result = s.connect_ex((host, p))  # connect_ex used for preventing raising exception
                if result == 0:  # successful connection
                    print("Port {} is open".format(p))
                else:
                    print("Port {} are closed".format(p))
                s.close()
        except KeyboardInterrupt:
            print("\n Exiting...")
            sys.exit()
        except socket.error:
            print("Host not responding...")
            sys.exit()

    banner = pyfiglet.figlet_format("Port Scanner")
    print(banner)

    host = str(input("Target IP:"))
    print("\n")
    print("x-" * 50 + "\n")
    print("Scanning Target:" + host)
    print("Scanning Started at:" + str(datetime.now()) + "\n")
    print("x-" * 50 + "\n\n")
    while True:
        print("----Choose from the below given options-----")
        print("1.Specific Port(User Defined)\n2.Full Scan\n3.EXIT")
        choice = int(input("Enter which scan do you want to perform:-"))
        if choice == 1:
            port = int(input("Enter the Port you want to Scan:"))
            userdefscan(port)
            cont = input("Do you want to continue:?(y/n):")
            cont = cont.lower()
            if cont != 'y':
                print("Exiting Program...")
                break
        elif choice == 2:
            scanwhole()
            cont = input("Do you want to continue:?(y/n):")
            cont = cont.lower()
            if cont != 'y':
                print("Exiting Program...")
                break
        elif choice == 3:
            print("Exiting Program...")
            break


if __name__ == "__main__":
    pscan()
