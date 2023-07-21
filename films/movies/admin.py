from django.contrib import admin
from .models import Category, Movie, MovieShots, Actor, RatingStar, Rating, Reviews, Genre

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(RatingStar)
admin.site.register(Genre)

