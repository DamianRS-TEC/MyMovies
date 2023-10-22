from django.shortcuts import render
from mymovies.models import Movie, Genre, Job, Person, MovieCredit, MovieReview

# Create your views here.


def home(request):
    movies = Movie.objects.all()
    genre = Genre.objects.all()
    job = Job.objects.all()
    person = Person.objects.all()
    movcred = MovieCredit.objects.all()

    mov = {
        "movies": movies,
        "genre": genre,
        "job": job,
        "person": person,
        "movcred": movcred,
    }
    return render(request, 'Index.html', mov)

def tail(request):
    return render(request, 'tail.html')
