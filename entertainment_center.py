# import media for Movie class
import media

# import fresh_tomatoes to generate and open web page
import fresh_tomatoes

# Create Ratatouille object
ratatouille = media.Movie(
    "Ratatouille",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
)

# Create Avatar object
avatar = media.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
)

# Create Inside Out object
insideOut = media.Movie(
    "Inside Out",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=_MC3XuMvsDI"
)

# Create Up object
up = media.Movie(
    "Up",
    "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Up_%282009_film%29.jpg/220px-Up_%282009_film%29.jpg",
    "https://www.youtube.com/watch?v=pkqzFUhGPJg"
)

# Create Wall.E object
wallE = media.Movie(
    "Wall-E",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=alIq_wG9FNk"
)

# Create Toy Story object
toyStory = media.Movie(
    "Toy Story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

# Create list of Movie objects
movies = [ratatouille, avatar, insideOut, up, wallE, toyStory]

# Open Movies Webpage
fresh_tomatoes.open_movies_page(movies)
