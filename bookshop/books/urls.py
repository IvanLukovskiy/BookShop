from django.urls import path

from .views import *

urlpatterns = [
    path('list/', BooksAPIView.as_view()),
    path('<int:pk>/', BooksAPIUpdate.as_view()),
    path('delete/<int:pk>/', BooksAPIDestroy.as_view()),
]
