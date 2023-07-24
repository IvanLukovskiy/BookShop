from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from books.models import Books, Author, Publisher
from books.serializers import BooksSerializer, AuthorSerializer, PublisherSerializer
from books.permissions import BooksPermission


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [BooksPermission]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser]
