from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import UserSerializer, FilmMiniSerializer
from .models import Film
from .serializers import FilmSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by()
    serializer_class = FilmSerializer

    def get_queryset(self):
        filmy = Film.objects.all().filter(po_premierze=True)
        return filmy

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = FilmMiniSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = FilmSerializer(instance)
        return Response(serializer.data)