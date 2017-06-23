
"""Movie related classes and functions"""


class Movie(object):
    """Class that returns simple Movie Instances"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


def movies(data):
    """Creates a lists of movies from certain data"""

    res = []
    for movie in data:
        res.append(Movie(movie[0], movie[1], movie[2]))

    return res
