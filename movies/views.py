from django.db.models import Avg, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, views, response, status
from app.permissions import GlobalDefaultPermission
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from reviews.models import Review


# View que cria e lista itens.
class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


# View que detalha, atualiza e deleta itens.
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


# View que trará alguns dados da nossa base de dados e mostrar ao usuário
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))    # Values pega só uma coluna de todas que eu to pegando no queryset, e a coluna em questão é o name, e agrupando com o Count.
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']        # Estou fazendo uma média da quantidade de estrelas dos filmes

        return response.Response(data={
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,            # Caso haja reviews na base de dados, vai acontecer o códgio, senão vai ser 0 o valor, evitando um erro de Null
        },
            status=status.HTTP_200_OK)
