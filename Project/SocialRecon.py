import requests
import time
from pyfiglet import figlet_format


def recon():

    title = figlet_format("Social Name Recon")
    print(title)
    username = input('Enter username to Search: ')

    # INSTAGRAM
    instagram = f'https://www.instagram.com/{username}'

    # FACEBOOK
    facebook = f'https://www.facebook.com/{username}'

    # TWITTER
    twitter = f'https://www.twitter.com/{username}'

    # YOUTUBE
    youtube = f'https://www.youtube.com/{username}'

    # BLOGGER
    blogger = f'https://{username}.blogspot.com'

    # GOOGLE+
    google_plus = f'https://plus.google.com/s/{username}/top'

    # REDDIT
    reddit = f'https://www.reddit.com/user/{username}'

    # WORDPRESS
    wordpress = f'https://{username}.wordpress.com'

    # PINTEREST
    pinterest = f'https://www.pinterest.com/{username}'

    # GITHUB
    github = f'https://www.github.com/{username}'

    # TUMBLR
    tumblr = f'https://{username}.tumblr.com'

    # FLICKR
    flickr = f'https://www.flickr.com/people/{username}'

    # STEAM
    steam = f'https://steamcommunity.com/id/{username}'

    # SLIDESHARE
    slideshare = f'https://slideshare.net/{username}'

    # SPOTIFY
    spotify = f'https://open.spotify.com/user/{username}'

    # SCRIBD
    scribd = f'https://www.scribd.com/{username}'

    # DAILYMOTION
    dailymotion = f'https://www.dailymotion.com/{username}'

    # WIKIPEDIA
    wikipedia = f'https://www.wikipedia.org/wiki/User{username}'

    # HACKERNEWS
    hackernews = f'https://news.ycombinator.com/user?id={username}'

    # EBAY
    ebay = f'https://www.ebay.com/usr/{username}'

    websites = [instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
                wordpress, pinterest, github, tumblr, flickr, steam, slideshare,
                spotify, scribd, dailymotion, wikipedia, hackernews, ebay]

    print("xx-Searching for User-xx :-"+username)
    time.sleep(0.5)
    print('-'*174)
    time.sleep(0.5)
    print('-'*174, '\n')
    time.sleep(0.5)

    print("Processing...!!!\n")
    time.sleep(0.5)
    print('-' * 174)
    time.sleep(0.5)
    print('-' * 174, '\n')
    time.sleep(0.5)

    count = 0
    for sites in websites:
        r = requests.get(sites)
        if r.status_code == 200:
            if username in r.text:
                print(f'Username:{username} - has been detected in url.{sites}')
            count += 1
        else:
            print(f'Username:{username} - has NOT been detected in url:{sites}, Match Not Found.')
    total = len(websites)
    print(f'FINISHED: A total of {count} MATCHES found out of {total} websites.')


if __name__ == '__main__':
    recon()
