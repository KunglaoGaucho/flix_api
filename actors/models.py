from django.db import models


# Pré definição de um campo
NATIONALITY_CHOICES = (                                                                                         # Faz uma pré-definição do que o usuário deve colocar no campo
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)


# Tabela de atores do bd
class Actors(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)                                                          # Null e Blanck = True permite que o campo seja em branco
    nationality = models.CharField(max_length=80, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name
