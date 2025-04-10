from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer


# View que é capaz de criar e listar itens do bd.
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()  # Queryset é para escolher o model e quais tabelas tem que buscar no BD.
    serializer_class = GenreSerializer  # Indica qual serializer a classe tem que usar.


# View que é capaz de atualizar e deletar itens do bd.
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
