from django.db import models
# run commands from django_root
# run `python3 manage.py makemigrations movie_years` to create SQL statements needed to update database
# then run `python3 manage.py migrate` to actually update db with SQL scripts

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField('release date')

    def __str__(self):
        return self.title+"-"+str(self.release_date)


class Guess(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    guess_year = models.IntegerField(default=None, null=True)
    guess_month = models.IntegerField(default=None, null=True)
    guess_day = models.IntegerField(default=None, null=True)
    isGuessCorrect = models.BooleanField(null=True)

    def isGuessYearCorrect(self):
        correct_date = self.movie.release_date
        if(correct_date.year == self.guess_year):
            return True
        return False


    def __str__(self):
        return str(self.movie)+"-"+str(self.guess_year)+"-"+str(self.isGuessCorrect)



