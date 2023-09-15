from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Review
from .forms import Movieform

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    context ={
        'movies' : movies
    }
    return render(request,'movie/index.html',context)

def details(request,pk):
    movie=Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form=Movieform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movi_name = movie
            review.save()
    form = Movieform()
    reviews = Review.objects.filter(movi_name=movie)
    context={
        'movie' : movie,
        'form' : form,
        'reviews' : reviews
    }
    return render(request,'movie/details.html',context)
