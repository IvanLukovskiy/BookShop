from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from user.models import CustomUser, Order, OrderItems
from user.permissions import UserListPermission, UserObjectPermission, OrderPermission, OrderItemsPermission
from user.serializers import CustomUserSerializer, OrderSerializer, OrderItemsSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [UserListPermission | UserObjectPermission]

    @action(methods=['get'], detail=False, permission_classes=[AllowAny])
    def vendor_list(self, request):
        users = CustomUser.objects.all()
        required_list = []
        for user in users:
            if user.status == 'Ven':
                required_list.append(user)
        serializer = CustomUserSerializer(required_list, many=True)
        return Response({'Наши продавцы': serializer.data})

    @action(methods=['get'], detail=False, permission_classes=[IsAdminUser])
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
    permission_classes = [OrderPermission]


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer
    permission_classes = [OrderItemsPermission]
