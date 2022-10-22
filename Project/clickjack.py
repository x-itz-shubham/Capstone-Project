from urllib.request import urlopen
from pyfiglet import figlet_format
import requests


def clckjack():
    banner = figlet_format(".x.Click JaCk.x.")
    print(banner)
    domain = input("Enter full url of the Website to be scanned :- ")
    # for testing
    r = requests.get(domain)
    # test = r.url
    # if test == domain:
    # print("Continuing.....")
    # else:
    # print("Try this "+test)
    # test code end here
    details = urlopen(domain)
    headers = details.info()
    if "X-Frame-Options" in headers:
        print("Website is not vulnerable!!!")
    else:
        print("Website is vulnerable!!!")


if __name__ == "__main__":
    clckjack()
