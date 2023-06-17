from django.shortcuts import render
from rest_framework import generics

from .models import Books
from .serializers import BooksSerializer


class BooksAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
