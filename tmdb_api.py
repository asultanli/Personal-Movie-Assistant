import requests
import os

def get_movie_info(movie_name):
    api_key = os.getenv('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}'
    response = requests.get(url)
    data = response.json()
    if data['results']:
        movie = data['results'][0]
        return {
            'title': movie['title'],
            'release_date': movie['release_date'],
            'overview': movie['overview'],
            'rating': movie['vote_average'],
            'poster_path': movie['poster_path']
        }
    else:
        return 'Movie not found'

def recommend_movies(preferences):
    api_key = os.getenv('TMDB_API_KEY')
    genre = preferences.get('genre')
    favorite_actor = preferences.get('favorite_actor')
    year_range = preferences.get('year_range')
    
    query = f'with_genres={genre}&primary_release_year={year_range}&with_cast={favorite_actor}'
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&{query}'
    response = requests.get(url)
    data = response.json()
    recommendations = []
    if data['results']:
        for movie in data['results']:
            recommendations.append(movie['title'])
    return recommendations