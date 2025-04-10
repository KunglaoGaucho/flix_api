from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh', TokenRefreshView.as_view(), name='refresh_token'),     # Fica dando refresh para gerar novos tokens
    path('authentication/token/verify', TokenVerifyView.as_view(), name='verify_token')                   # Verifica se o token é válido
]
