import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrap():
    # url of that particular of which we want to scrap the data
    url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    heading = soup.find('h1', class_='header')
    print(heading.string)

    sub_head = soup.find('div', class_='byline')
    print(sub_head.string)

    result = soup.find('div', class_='desc')
    print(result.text)

    # For Movie Name
    name = []
    for d in soup.find_all('td', {'class': 'titleColumn'}):
        title = d.find('a')
        name.append(title.string)
    print(*name, sep='\n')

    # For Movie Year
    years = []
    for d in soup.find_all('td', {'class': 'titleColumn'}):
        year = d.find('span', {'class': 'secondaryInfo'})
        years.append(year.string)
    print(*years, sep='\n')

    # For Movie Rating
    ratings = []
    for d in soup.find_all('td', {'class': 'ratingColumn imdbRating'}):
        if d.find('strong.is_empty_element'):
            print("NA")
        else:
            d.find('strong')
            ratings.append(d.text)
    print(*ratings, sep='\n')

    # For Movie Ranking
    ranking = []
    for d in soup.find_all('td', {'class': 'titleColumn'}):
        rank = d.find('div', {'class': 'velocity'})
        ranking.append(rank.text.replace('\n', ''))
    print(*ranking, sep='\n')

    # club all the details we fetched into a new list
    data = {'Movie Name': name, 'Year': years, 'Rating': ratings, 'Ranking': ranking}

    # store all the data present in the data list
    df = pd.DataFrame(data)

    # store in the excel
    df.to_excel('Imdb_Data.xlsx')


if __name__ == "__main__":
    scrap()
