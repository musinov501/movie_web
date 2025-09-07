from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Movie, Genre, Comment
from .forms import CommentForm, MovieForm

def home(request: HttpRequest):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres
    }

    return render(request, 'cinema/index.html', context)

def movie_by_category(request: HttpRequest, genre_id: int):
    movies = Movie.objects.filter(genre_id = genre_id)
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres
    }

    return render(request, 'cinema/index.html', context)


def show_in_detail(request: HttpRequest, pk: int):
    genres = Genre.objects.all()
    movie = Movie.objects.get(pk=pk)
    comments = Comment.objects.filter(movie = movie)



    context = {
        'movie': movie,
        'genres': genres,
        'comments': comments,
        'form': CommentForm()
    }

    return render(request, 'cinema/detail.html', context)

def save_comment(request: HttpRequest, movie_id):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text = request.POST.get("text"),
                movie_id = movie_id,
                user = request.user
            )

    return redirect("show_detail", pk = movie_id)

def save_movies(request: HttpRequest):
    if request.user.is_staff:
        if request.method == "POST":
            form = MovieForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                movies = form.save()
                return redirect('show_detail', pk = movies.pk )
        else:
            form = MovieForm()
        context = {
            'form': form
        }
        return render(request, 'cinema/add_movie.html', context)
    else:
        return redirect("home")

