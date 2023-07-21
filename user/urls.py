from django.urls import path, include
from rest_framework import routers

from user.views import CustomUserViewSet, OrderViewSet, OrderItemsViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
