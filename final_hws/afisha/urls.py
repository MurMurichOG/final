from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.Director_view),
    path('api/v1/directors/<int:id>/', views.Director_view),
    path('api/v1/movies/', views.Movie_view),
    path('api/v1/movies/<int:id>/', views.Movie_view),
    path('api/v1/reviews/', views.Review_view),
    path('api/v1/reviews/<int:id>/', views.Review_view),
]
