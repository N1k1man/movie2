from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


from .models import Movie


class MoviesView(View):
    #Список фильмов
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movies.html", {"movie_list":movies})
    

class MovieDetail(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})
    



# class MoviesView(ListView):
#     #Список фильмов
#     model = Movie
#     queryset = Movie.objects.filter(draft=False)
#     template_name = "movies/movies.html"
#     # шаблон называется подруому

# class MoviesView(DetailView):
#     #Список фильмов
#     model = Movie
#     slug_field = "url"# поле по какому искать запись
    # автоматически подставляет суффикс к шаблону
    # берет имя модели добавляет суффикс нижнее подч детейл