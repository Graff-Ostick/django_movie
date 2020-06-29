from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .models import Movie, Category
from .forms import Reviews

class MovieView(ListView):

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies_app/movie_list.html'


class MovieDetailView(DetailView):

    model = Movie
    slug_field = "url"


class AddReview(View):
    """"review"""
    def post(self, request, pk):
        form = Reviews(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
