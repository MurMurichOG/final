from rest_framework import serializers
from . import models


class MovieSterializer(serializers.ModelSerializer):
    class Meta:
        movie = models.Movie
        fields = "__all__"

class DirectorSterializer(serializers.ModelSerializer):
    class Meta:
        director = models.Director
        fields = "__all__"


class ReviewSterializer(serializers.ModelSerializer):
    class Meta:
        review = models.Review
        fields = "__all__"