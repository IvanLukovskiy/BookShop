from django.urls import path, include
from rest_framework import routers

from books.views import *

routerbook = routers.DefaultRouter()
routerbook.register(r'books', BooksViewSet)

routerauthor = routers.DefaultRouter()
routerauthor.register(r'author', AuthorViewSet)

routerpublisher = routers.DefaultRouter()
routerpublisher.register(r'publisher', PublisherViewSet)

urlpatterns = [
    path('', include(routerbook.urls)),
    path('', include(routerauthor.urls)),
    path('', include(routerpublisher.urls)),
]
