from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<slug:slug>/', views.MovieDetail.as_view(), name='movie_detail')
]