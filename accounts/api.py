from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from .serializer import AccountSerializer, AccountCreateSerializer

from .models import Account


class AccountViewSets(mixins.CreateModelMixin,
                      # mixins.UpdateModelMixin,
                      # mixins.ListModelMixin,
                      # mixins.RetrieveModelMixin,
                      # mixins.DestroyModelMixin,
                      GenericViewSet
                      ):
    model = Account
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = AccountCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(customer=request.user) here we pass the instance it self for serializer
        serializer.save(customer_id=request.user.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
