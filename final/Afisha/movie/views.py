from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, RewievSerializer
from .models import Director, Movie, Review
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                tkn = Token.objects.get(user=user)
            except Token.DoesNotExist:
                tkn = Token.objects.create(user=user)
            return Response(data={'message': tkn.key}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Ошибка'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        email_ = request.data['email']
        try:
            User.objects.create_user(username=username, password=password, email=email_)
        except:
            return Response(data={'message': 'Ошибка'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'message': 'Успешно, необходима авторизация',
                              'link_for_signup': 'api/v1/login'},
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def directors(request):
    if request.method == 'GET':
        directors_data = DirectorSerializer(Director.objects.all(), many=True).data
        if request.user.is_authenticated:
            return Response(data=directors_data)
    elif request.method == 'POST':
        try:
            Director.objects.create(**request.data)
        except:
            return Response(data={'message': 'Произошла ошибка, повторите попытку'})
        return Response(data={'message': 'Сохранено'})


@api_view(['PUT', 'DELETE', 'GET'])
def directors_detail(request, id):
    try:
        obj = get_object_or_404(Director, id=id)
        serialized_obj = DirectorSerializer(obj).data
    except:
        return Response(data={'message': 'Произошла ошибка, попробуйте позже'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(data=serialized_obj)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(data={'message': 'Сохранено'})

    elif request.method == 'PUT':
        obj.name = request.data['name']
        obj.save()
        return Response(data={'message': 'Изменено'})


@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        data = MovieSerializer(Movie.objects.all(), many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        try:
            Movie.objects.create(**request.data)
        except:
            return Response(data={'message': 'Произошла ошибка, повторите попытку'})
        return Response(data={'message': 'Добавлено'})


@api_view(['PUT', 'DELETE', 'GET'])
def movies_detail(request, id):
    try:
        obj = get_object_or_404(Movie, id=id)
    except:
        return Response(data={'message': 'Ничего не найдено'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        return Response(data=MovieSerializer(obj).data)

    elif request.method == 'PUT':
        obj.title = request.data['title']
        obj.description = request.data['description']
        obj.duration = request.data['duration']
        obj.director = request.data['director']
        obj.save()
        return Response(data={'message': 'Изменено'})

    elif request.method == 'DELETE':
        obj.delete()
        return Response(data={'message': 'Удалено'})


@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        data = RewievSerializer(Review.objects.all(), many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        try:
            Movie.objects.create(**request.data)
        except:
            return Response(data={'message': 'Произошла ошибка., повторите попытку'})
        return Response(data={'message': 'Добавлено'})


@api_view(['GET', 'DELETE', 'PUT'])
def reviews_detail(request, id):
    try:
        obj = get_object_or_404(Review, id=id)
    except:
        return Response(data={'message': 'Ничего не найдено'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        return Response(data=RewievSerializer(obj).data)

    elif request.method == 'PUT':
        obj.text = request.data['text']
        obj.movie = request.data['movie']
        obj.stars = request.data['stars']
        obj.save()
        return Response(data={'message': 'Изменено'})

    elif request.method == 'DELETE':
        obj.delete()
        return Response(data={'message': 'Удалено'})
