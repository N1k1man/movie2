from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)#полож знач от нуля до 32767
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'



class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах')
    fees_in_world = models.PositiveIntegerField(default=0, help_text='указывать сумму в долларах')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug':self.url})
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStar(models.Model):
    #Звезда рейтинга
    value = models.SmallIntegerField(default=0) # от минус 32768 до 32767

    def __str__(self) -> str:
        return self.value
    
    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'

class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self) -> str:
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    #Отзывы

    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', verbose_name='родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.movie}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


