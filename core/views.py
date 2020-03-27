from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
# Create your views here.




class MovieList(ListView):
	model = Movie



class MovieDetail(DetailView):
	"""docstring for MovieDetail"""
	model = Movie
	#print(object.title.url)
		
