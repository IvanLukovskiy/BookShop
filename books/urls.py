from django.urls import path, include
from rest_framework import routers

from books.views import *

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'publisher', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
