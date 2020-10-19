import random
import datetime

class Picture:
  def __init__(self, title, release_year, genre, played):
    self.title = title
    self.release_year = release_year
    self.genre = genre
    self.played = played

  def play(self):
      self.played += 1

  def show(self):
      print(f"{self.title} {self.played}")

class Movie(Picture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self):
      return f'{self.title} ({self.release_year})'

def twoDigits(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)

class Serie(Picture):
  def __init__(self,title, release_year,genre,played, season, episode):
    super().__init__(title, release_year, genre,played)
    self.episode = episode
    self.season = season
  def __str__(self):
    if self.episode < 10:
      return f'{self.title}({self.release_year}),S0{twoDigits(self.episode)}{twoDigits(self.season)}'

pictures = [
               Movie("Titanic", 1996, "drama", 0),
               Movie("Annie", 2014, "musical", 0),
               Movie("Amelia", 2008, "drama", 0),
               Movie("Rocky", 1987, "drama", 0),
               Serie("Friends", 2000, "comedy", 0,6,6),
               Serie("Wilfred", 2011, "drama", 0,6,9),
               Serie("Suits", 2011, "drama", 0,6,9),
               Serie("Dexter", 2005, "drama", 0,6,9),
           ]
print("Available:")
for p in pictures:
    print(p)
print("----------------------------------")
def get_movies(pict):
    movies = []
    for p in pict:
        if isinstance(p, Movie):
            movies.append(p)
    return movies

get_movies(pictures)

def get_series(pict):
    series = []
    for p in pict:
        if isinstance(p, Serie):
            series.append(p)
    return series

get_series(pictures)

def search(title):
    for x in pictures:
      if str(x.title) == title:
        print(f'We have {title}')
      elif str(x.title) == title:
        break

def generate_views(pict):
    n = len(pict)
    r = random.randint(0, n-1)
    p = pict[r]
    r = random.randint(1, 100)
    p.played += r

def gen_10(pict):
    for _ in range(10):
        generate_views(pictures)
        pict.sort(key=lambda x: x.played, reverse=True)

print("----------------------------------")
print ("Sorten by views on:")
dzis=datetime.datetime.now()
print (dzis)
gen_10(pictures)
for p in pictures:
    p.show()

print("----------------------------------")
def top_titles(picts):
   picts.sort(key=lambda x: x.played, reverse=True)
   print("Top titles are:")
   print("1.",picts[0])
   print("2.",picts[1])
   print("3.",picts[2])

top_titles(pictures)
print("----------------------------------")
search("Annie")




