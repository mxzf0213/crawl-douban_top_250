import requests
from bs4 import BeautifulSoup
import datetime

def get_movies():
   movies = []
   url = "https://movie.douban.com/top250"
   headers = \
   {
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
       'Host': 'movie.douban.com'
   }
   for i in range(0,10):
       link = url + "?start=" + str(i*25)
       reader = requests.get(link, headers = headers, timeout=10)
       soup = BeautifulSoup(reader.text,"lxml")
       div_list = soup.find_all('div',class_ = 'hd')
       for each in div_list:
           movie = each.a.span.text.strip()
           movies.append(movie)
   return movies
if __name__ == '__main__':
    movie_list = get_movies()
    f = open('douban.txt','w')
    f.write(str(datetime.datetime.now()) + '\n豆瓣电影 Top 250:' + '\n')
    for movie in movie_list:
        f.write(movie+'\n')
    f.close()