from prompt import get_response
from tmdb_api import get_movie_info, recommend_movies

def gather_user_preferences(context):
    preferences = {
        'genre': None,
        'favorite_actor': None,
        'year_range': None
    }
    if not preferences['genre']:
        preferences['genre'] = input("What genres of movies do you like? ")
    if not preferences['favorite_actor']:
        preferences['favorite_actor'] = input("Who is your favorite actor? ")
    if not preferences['year_range']:
        preferences['year_range'] = input("Do you have a preferred year range for movies? ")

    return preferences

def handle_conversation():
    context = "" 
    preferences = {}
    print("Welcome to your personal movie assistant!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        if "recommend" in user_input.lower():
            if not preferences:
                preferences = gather_user_preferences(context)
            recommended_movies = recommend_movies(preferences)
            result = "Here are some movie recommendations for you: " + ", ".join(recommended_movies)
        else:
            result = get_response(context, user_input)
        
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nBot: {result}\n"