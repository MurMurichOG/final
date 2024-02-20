from django.shortcuts import render
from . import sterializer, models
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    return Response(data=data)


@api_view(['GET'])
def Review_view(request):
    text = models.Review.objects.all()
    movie = models.Movie.objects.all()
    data = sterializer.DirectorSterializer(text, movie).data
    return Response(data=data)
