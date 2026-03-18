movies = [
    {"movieName": "A", "releaseDate": "2020-01-15"},
    {"movieName": "B", "releaseDate": "2019-06-10"},
]

movies.sort(key=lambda m: m["releaseDate"])

print(movies)