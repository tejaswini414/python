choice_movie = {'Bahubali' : '10:00 AM',
                'Inception' : '1:00 PM',
                'Interstellar' : '4:00 PM',
                'The Dark Knight' : '7:00 PM',
                'Avatar' : '10:00 PM'}

print("avaliable movies and show times:")
movie = input("which movie would you like to know the timings?")

show_time = choice_movie.get(movie)
if(show_time == None):
    print("sorry", "we don't have that movie available")
else:
    print("show time for", movie, "is at", show_time)