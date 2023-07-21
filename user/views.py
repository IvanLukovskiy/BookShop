from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import CustomUser, Order, OrderItems
from user.permissions import IsAdminOrReadOnly
from user.serializers import CustomUserSerializer, OrderSerializer, OrderItemsSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated])
    def vendor_list(self, request):
        users = CustomUser.objects.all()
        required_list = []
        for user in users:
            if user.status == 'Ven':
                required_list.append(user)
        serializer = CustomUserSerializer(required_list, many=True)
        return Response({'Список продавцов': serializer.data})

    @action(methods=['get'], detail=False, permission_classes=[IsAdminOrReadOnly])
    def customer_list(self, request):
        users = CustomUser.objects.all()
        required_list = []
        for user in users:
            if user.status == 'Cus':
                required_list.append(user)
        serializer = CustomUserSerializer(required_list, many=True)
        return Response({'Список наших покупателей': serializer.data})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
