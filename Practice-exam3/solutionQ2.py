class Movie:
    def __init__(self, title, running_time=60, rating=0):
        self.title = title
        self.running_time = running_time
        self.rating = rating
        self.numbers = []
        if running_time < 60:
            raise AssertionError('Movie is too short')

    
    def put_rating(self, numbers):
        for number in numbers:
            if 0 <= number <= 5 and number % 0.5 == 0: # Only consider ratings in the interval [0.5], WTF DO THEY MEAN BY THAT??
                self.numbers.append(number)
        self.rating = sum(self.numbers) / len(self.numbers)
   

    def __str__(self):
        hours, minutes = divmod(self.running_time, 60) # there is probably a method we learned, but this is faster.
        rating_stars = '*' * int(self.rating) # string convertion rating to stars
        return f'Film: {self.title} ({hours}h{minutes}min; rating: {rating_stars})'


class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.movie = None

    def put_movie(self, Movie):
        if self.movie == None:
            self.movie = Movie

    
    def remove_movie(self): #Don't add the movie Parameter, it's about the movie INSIDE THE ROOM.
        if self.movie is not None:
            self.movie = None

    
    def same_movie_diff_rooms(self, other):
        if self.movie == other.movie:  #They didn't specify if it was about titles.
            #raise AssertionError(f'The same movie is being played in the room {self.room_number} as the movie being played in the room {other.room_number}')
            return f'The same movie is being played in the room {self.room_number} as the movie being played in the room {other.room_number}'
        else:
            #raise AssertionError(f'Room {self.room_number} has a different movie being played than the movie in room {other.room_number}')
            return f'Room {self.room_number} has a different movie being played than the movie in room {other.room_number}'
    
    def put_rating(self, numbers):
        if self.movie is not None:
            for number in numbers:
                if 0 <= number <= 5 and number % 0.5 == 0:
                    self.movie.numbers.append(number)
            self.movie.rating = sum(self.movie.numbers) / len(self.movie.numbers)
         
    
    def __str__(self):
        # self.running_time
        return f'Room: {self.room_number} \n{str(self.movie)}'



frozen = Movie('Frozen', 135)
shrek2ondvd = Movie('shrek2ondvd', 140)
room12 = Room(12)
room14 = Room(14)
room15 = Room(15)
room12.put_movie(frozen)
room14.put_movie(frozen)
room15.put_movie(shrek2ondvd)
room14.put_rating([1,2,3,4,10,5,1,2,3,4,5,20])
room15.put_rating([5,5,5,5,5])
print(room12.same_movie_diff_rooms(room14))
print(room12.same_movie_diff_rooms(room15))
print(room14)
print(room15)