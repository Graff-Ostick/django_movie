from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie

class MovieView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies_html/movie_list.html'

class MovieDetailView(DetailView):

    model = Movie
    slug_field = "url"
