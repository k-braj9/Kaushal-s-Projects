import requests

api_key = '25c22997'
Movie = input('Enter a movie: ')
movie_data = requests.get(f'http://www.omdbapi.com/?t={Movie}&apikey={api_key}')


Title = movie_data.json()['Title']

Date = movie_data.json()['Released']

Rating = movie_data.json()['Rated']

Director = movie_data.json()['Director']

Cast = movie_data.json()['Actors']

IMDB_Rating = movie_data.json()['imdbRating']

print(Title)
print(Date)
print(Rating)
print(Director)
print(Cast)