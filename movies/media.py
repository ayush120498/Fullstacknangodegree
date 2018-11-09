import webbrowser


class Movie():
    """ this class is for creating the variable of the movies.
    Atributes:
        title:Stores the movie title.
        storyline:Stores the storyline of the movie.
        poster_image_url:A string variable stores
                         poster url.
        trailer_youutube_url:A string variable stores
                            the url of trailer video.
     """

    def __init__(self, movie_title, movie_storyline, poster_img, trailer_utub):
        """Inits the class with incoming variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_utub

    def show_trailer(self):
        """Performs the opening of the trailer"""
        webbrowser.open(self.trailer_youtube_url)
