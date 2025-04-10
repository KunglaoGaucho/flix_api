from rest_framework import serializers
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from movies.models import Movie


# Serializer para o método POST no app Movie
class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # Validador de data (validade_ é OBRIGATÓRIO antes)
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser abaixo de 1990.')
        return value

    # Validador de resumo (validade_ é OBRIGATÓRIO antes)
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo não deve ser maior que 200 caracteres.')
        return value


# Serializer personaliado para os demais métodos que usam o GET
class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)                    # Estou adicionando um campo além dos campos do model indicado

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    # Calculando a média de estrelas dos filmes
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']                 # Aggregate: Adiciona um campo extra à nossa query, além de pegar todos os outros campos. Avg: Calcula a média sozinho

        if rate:
            return round(rate, 1)

        return None
