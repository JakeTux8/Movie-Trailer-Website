import webbrowser #module needed to open url links in browser

class Movie():

    """"This class allows the creation of movie objects that include movie title, synopsis, poster, and trailer"""
    
    #Movie class constructor.  Four arguments besides self are needed to initialize: movie title, movie synopsis, poster image url, and youtube url.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Function to show movie trailer
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)  #opens youtube url in system's default browser
