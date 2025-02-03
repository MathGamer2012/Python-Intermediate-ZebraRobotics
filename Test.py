import urllib.request
import json
import fresh_tomatoes 


movies = []
class Movie:

    def __init__(self, title, poster, trailer):
        self.movie_title = title
        self.poster_image_url = poster 
        self.trailer_youtube_url = trailer

serverRequest = "https://api.themoviedb.org/3/trending/movie/day?api_key=ddc089a52e6eff0a16171cfd0c4178f4"

res = urllib.request.urlopen(serverRequest)
data = json.loads(res.read().decode("utf-8"))

for i in data["results"]:
    currentMovie = Movie(i["original_title"], "https://image.tmdb.org/t/p/w500"+i["poster_path"], fresh_tomatoes.getMovieTrailer(str(i["id"])))
    movies.append(currentMovie)

fresh_tomatoes.open_movies_page(movies)


    
 
