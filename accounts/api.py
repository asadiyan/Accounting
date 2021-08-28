from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action, authentication_classes
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import TokenAuthentication

from .serializer import AccountSerializer, AccountCreateSerializer, AccountTransactionSerializer, \
    AccountWithdrawSerializer, AccountDepositSerializer, AccountListSerializer, AccountHistoryListSerializer

from .models import Account
from histories.models import History

from .services import check_amount, do_transfer, check_account

from .exceptions import AccountBalanceIsNotEnoughException, AccountDoesNotExist, OperationImpossibleException


class AccountViewSets(mixins.CreateModelMixin,
                      # mixins.UpdateModelMixin,
                      # mixins.ListModelMixin,
                      # mixins.RetrieveModelMixin,
                      # mixins.DestroyModelMixin,
                      GenericViewSet):
    model = Account
    queryset = Account.objects.all()

    serializer_class = AccountCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = AccountCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(customer=request.user) here we pass the instance it self(object) for serializer
        serializer.save(customer_id=request.user.id)  # here we pass just id tp serializer
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['POST'])
    @authentication_classes([TokenAuthentication])
    def transfer(self, request):
        serializer = AccountTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        source = data.get('transfer_source')
        destination = data.get('transfer_destination')
        transfer_amount = data.get('transfer_amount')

        source.amount = source.amount - transfer_amount
        destination.amount = destination.amount + transfer_amount
        source.save()
        destination.save()
        History.objects.create(transfer_amount=transfer_amount, transfer_source=source,
                               transfer_destination=destination, account_amount=source.amount)
        return Response('done')

        # if transfer_source.bank_id != transfer_destination.bank_id:
        #     if transfer_source.amount > transfer_amount:
        #         transfer_source.amount = transfer_source.amount - transfer_amount
        #         transfer_destination.amount = transfer_destination.amount + transfer_amount
        #         transfer_destination.save()
        #         transfer_source.save()
        #         History.objects.create(transfer_amount=transfer_amount, transfer_source=transfer_source,
        #                                transfer_destination=transfer_destination, account_amount=transfer_source.amount)
        #         return Response('done')
        #     else:
        #         raise AccountBalanceIsNotEnoughException
        # else:
        #     raise OperationImpossibleException

    @action(detail=False, methods=['POST'])
    def withdraw(self, request):
        serializer = AccountWithdrawSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        source = data.get('transfer_source')

        transfer_source = get_object_or_404(Account.objects, pk=source.id)
        transfer_amount = data.get('transfer_amount')

        if transfer_source.amount > transfer_amount:
            transfer_source.amount = transfer_source.amount - transfer_amount
            transfer_source.save()
            History.objects.create(transfer_amount=transfer_amount, transfer_source=transfer_source,
                                   transfer_destination=None, account_amount=transfer_source.amount)
            return Response('done')
        else:
            raise AccountBalanceIsNotEnoughException

    @action(detail=False, methods=['POST'])
    def deposit(self, request):
        serializer = AccountDepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        source = data.get('transfer_source')

        transfer_source = get_object_or_404(Account.objects, pk=source.id)
        transfer_amount = data.get('transfer_amount')
        transfer_source.amount = transfer_source.amount + transfer_amount
        transfer_source.save()
        History.objects.create(transfer_amount=transfer_amount, transfer_source=transfer_source,
                               transfer_destination=None, account_amount=transfer_source.amount)
        return Response('done')

    @action(detail=False, methods=['GET'])
    def my_accounts(self, request):
        model = Account
        queryset = model.objects.filter(customer=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AccountListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AccountListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def history(self, request, pk):
        queryset = History.objects.filter(Q(transfer_source=pk) | Q(transfer_destination=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AccountHistoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AccountHistoryListSerializer(queryset, many=True)
        return Response(serializer.data)
