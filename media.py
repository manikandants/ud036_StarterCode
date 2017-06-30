class Movie():

    """Movie has the following properties
    title: Name of the movie
    poster_image_url: Link to poster image
    trailer_youtube_url: Link to trailer in youtube"""

    # Constructor method for Movie class

    def __init__(self, title, poster_image_url, trailer_youtube_url):

        # Assign title
        self.title = title

        # Assign poster image link
        self.poster_image_url = poster_image_url

        # Assign youtube trailer link
        self.trailer_youtube_url = trailer_youtube_url
