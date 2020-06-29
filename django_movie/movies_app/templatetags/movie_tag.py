from django import template

from movies_app.models import Category, Movie

register = template.Library()

@register.simple_tag()
def get_category():
    """вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('movies_app/tags/last_movie.html')
def get_last_movies(count=5):
    """вывод всех категорий"""
    movies = Movie.objects.order_by("id")[:count]
    return {"last_movies" : movies}
