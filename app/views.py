from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app.models import ToDo
from app.serializers import ToDoModelSerializer


class ToDOView(ModelViewSet):
    queryset = ToDo.objects.all().order_by('id')
    serializer_class = ToDoModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


