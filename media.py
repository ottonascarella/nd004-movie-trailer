
class Movie():
    """Class that returns simple Movie Instances"""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

# This is a data object
# that will be used to generate the instances
data = [
    [
        "Cinema Paradiso",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BM2FhYjEyYmYtMDI1Yy00YTdlLWI2NWQtYmEzNzAxOGY1NjY2XkEyXkFqcGdeQXVyNTA3NTIyNDg@._V1_.jpg",
        "https://www.youtube.com/watch?v=C2-GX0Tltgw"
    ],
    [
        "Matrix",
        "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
        "https://www.youtube.com/watch?v=m8e-FF8MsqU"
    ],
    [
        "Soul Kitchen",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BZDg3MGIyYWEtOGRkYS00NWY5LWI3MDctMDY1NWJjZDlkOGE1XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,707,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=Ua86x-J4ubA"
    ],
    [
        "Central do Brasil",
        "https://upload.wikimedia.org/wikipedia/en/1/12/Central-do-brasil-poster04.jpg",
        "https://www.youtube.com/watch?v=pF8QAf7a2Js"
    ],
    [
        "Contact",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BYWNkYmFiZjUtYmI3Ni00NzIwLTkxZjktN2ZkMjdhMzlkMDc3XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_SX672_AL_.jpg",
        "https://www.youtube.com/watch?v=d9C2cF3KvP8"
    ],
    [
        "99 Francs",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxMTc3MDIzNl5BMl5BanBnXkFtZTcwODkyMjA0Mg@@._V1_.jpg",
        "https://www.youtube.com/watch?v=sF4EL5G7qhQ"
    ]
];

# create a separated list for movie instances to avoid mutation
movies = [];

for movie in data:
    movies.append( Movie(movie[0], movie[1], movie[2]) )
