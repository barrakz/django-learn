from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View

from viewer.forms import MovieForm
from viewer.models import Movie, Genre
from django.views.generic import TemplateView, ListView, FormView
from django.forms import (
    CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea
)


# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all()}
#     )

# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all()}
#         )

# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all()}


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')
