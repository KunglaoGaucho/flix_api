from django.db import models


# Tabela de gêneros.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    # Para aparecer o nome mais apresentável
    def __str__(self):
        return self.name
