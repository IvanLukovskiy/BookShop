from django.urls import path, include
from rest_framework import routers

from user.views import CustomUserViewSet, OrderViewSet, OrderItemsViewSet

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitems', OrderItemsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
