from django.shortcuts import render
from . import sterializer, models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import Movie, Review, Director

@api_view(['GET'])
def Director_view(request):
    name = models.Director.objects.all()
    data = sterializer.DirectorSterializer(name).data
    return Response(data=data)


@api_view(['GET'])
def Movie_view(request):
    title = models.Movie.objects.all()
    description = models.Movie.objects.all()
    duration = models.Movie.objects()
    director = models.Movie.objects()
    data = sterializer.MovieSterializer(title, description, duration, director).data
    movies = Movie.objects.annotate(avg_rating=Avg('reviews__stars')).prefetch_related('reviews')
    directors = Director.objects.annotate(movies_count=Count('movies'))
    context = {
        'movies': movies,
        'avg_rating': Review.objects.aggregate(Avg('stars'))['stars__avg'],
        'directors': directors,
    }
    return render(request, context, data)


@api_view(['GET'])
def Review_view(request):
    text = models.Review.objects.all()
    movie = models.Movie.objects.all()
    data = sterializer.DirectorSterializer(text, movie).data
    return Response(data=data)
