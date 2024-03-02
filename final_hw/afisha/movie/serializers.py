from rest_framework import serializers
from .models import Director, Movie
from rest_framework.exceptions import ValidationError


class DirectorValidationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, min_length=2)

    def validate(self, attrs):
        if not attrs['name']:
            raise ValidationError('Напишите правильное имя')


class MovieValidationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=500)
    duration = serializers.CharField(max_length=20)
    director = serializers.CharField(max_length=25)

    def validate(self, attrs):
        try:
            Director.objects.get(name=attrs['director'])
        except:
            raise ValidationError('Не найдено директора с таким именем')


class ReviewValidationSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    movie = serializers.CharField(max_length=25)
    stars =  serializers.CharField(max_length=10)

    def validate(self, attrs):
        try:
            Movie.objects.get(title=attrs['movie'])
        except:
            raise ValidationError('Такого фильма не существует')

        try:
            stars = int(attrs['stars'])
        except:
            raise ValidationError('Введите число')
        if stars < 1 or stars > 5:
            raise ValidationError('Оценка должна быть от 1 до 5')


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()