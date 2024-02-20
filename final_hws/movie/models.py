from django.db import models


class Director(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.TimeField()
    director = models.CharField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.CharField(max_length=50)

    def __str__(self):
        return self.text