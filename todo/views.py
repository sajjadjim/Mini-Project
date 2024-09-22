from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer