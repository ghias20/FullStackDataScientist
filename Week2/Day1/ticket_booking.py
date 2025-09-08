class Cinema:
    def __init__(self,movies):
        self.movies=movies
    
    def book(self,movie,seats):
        if movie not in self.movies:
            return f"{movie} is not available"
        if seats>self.movies[movie]:
            return f"Not enough seats for {movie}"
        self.movies[movie]-=seats
        return f"Booked {seats} tickets for {movie}"
    
    def cancel(self,movie,seats):
        if movie not in self.movies:
            return f"{movie} is not available"
        self.movies[movie]+=seats
        return f"Cancelled {seats} ticket for {movie}"
    
    def show_movies(self):
        print("Movies:",self.movies)

# Sample Input
cinema=Cinema({"Avatar":10,"Batman":5})
print(cinema.book("Avatar",2))
print(cinema.cancel("Avatar",1))
cinema.show_movies()
