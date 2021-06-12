from movie_years.models import Movie, Guess

Movie.objects.all()

guess = Guess(movie=1, guess_year="1980")

guess.save()

print(guess.id)
