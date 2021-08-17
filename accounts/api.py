from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action

from .serializer import AccountSerializer, AccountCreateSerializer, AccountTransactionSerializer

from .models import Account

from .services import check_amount

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

    @action(detail=False, methods=['POST'])
    def transfer(self, request):
        serializer = AccountTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        amount = serializer.validated_data.get('transfer_amount')
        source = serializer.validated_data.get('transfer_source')
        destination = serializer.validated_data.get('transfer_destination')
        if check_amount(data):
            return Response("done")




