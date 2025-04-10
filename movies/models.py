from django.db import models
from actors.models import Actors
from genres.models import Genre


# Tabela de filmes que herda itens de Actors e Genres
class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')  # Protegendo o gênero que estiver em uso de ser deletado
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actors, related_name='movie')  # Permite que eu ligue vários itens para esse campo
    resume = models.TextField(null=True, blank=True)  # Campo de texto livre

    def __str__(self):
        return self.title
