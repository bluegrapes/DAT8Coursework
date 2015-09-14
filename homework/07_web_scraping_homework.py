'''
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.

Finally, convert that list into a DataFrame.
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pdb

def get_movie_info(imdb_id):
    r = requests.get('http://www.imdb.com/title/' + imdb_id)
    b = BeautifulSoup(r.text)
    assert len(r.text) > 0, "no text"
    dict = {}
    dict["content_rating"] = b.find(name='meta', attrs={'itemprop':'contentRating'})['content']
    dict["description"] = b.find(name='p', attrs={'itemprop':'description'}).text.strip()
    dict["duration"] = int(b.find(name='time', attrs={'itemprop':'duration'}).text.strip()[:-4])
    dict["start_rating"] = float(b.find(name='span', attrs={'itemprop':'ratingValue'}).text)
    dict["title"] = b.find(name='h1').find(name='span', attrs={'class':'itemprop', 'itemprop':'name'}).text
    return dict

if __name__ == "__main__":
    lst = []
    with open('data/imdb_ids.txt', 'r') as f:
        lst = [get_movie_info(line) for line in f.readlines()]
        df = pd.DataFrame(lst)
    print df


