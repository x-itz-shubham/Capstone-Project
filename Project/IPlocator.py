import requests
import webbrowser
from pyfiglet import figlet_format


def iptrack():

    title = figlet_format("IP Tracker")
    print(title)

    ip = input("Ip address:-")
    url = ('https://ipinfo.io/' + ip)
    res = requests.get(url)
    ipinfo = res.json()

    location = ipinfo['loc'].split(',')
    lat = location[0]
    long = location[1]

    print('')
    print("City : " + ipinfo['city'])
    print("Region : " + ipinfo['region'])
    print("Country : " + ipinfo['country'])
    print("Organisation : " + ipinfo['org'])
    print("Timezone : " + ipinfo['timezone'])
    print("Latitude : " + lat)
    print("Longitude : " + long)
    print("Opening location in Browser")
    mapurl = "https://maps.google.com/maps?q=%s,%s" % (lat, long)
    webbrowser.open(mapurl, new=2)
    print('')


if __name__ == "__main__":
    iptrack()
