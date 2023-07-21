from django.urls import path, include
from rest_framework import routers

from books.views import BooksViewSet, AuthorViewSet, PublisherViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
