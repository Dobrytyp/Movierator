from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer
from .models import Film
from .serializers import FilmSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by()
    serializer_class = FilmSerializer

