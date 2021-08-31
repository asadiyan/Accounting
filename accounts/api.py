from django.db.models import Q

from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters

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
    def transfer(self, request):
        serializer = AccountTransactionSerializer(data=request.data)
        # we have a validation method inside our serializer we defined it by our need
        # we could have used a default one
        # but for our case we needed a custom one then we defined it in our serializer
        # when we call serializer.is_valid() it will check our validation method and will do our condition
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        source = data.get('transfer_source')
        destination = data.get('transfer_destination')
        transfer_amount = data.get('transfer_amount')

        source.amount = source.amount - transfer_amount
        destination.amount = destination.amount + transfer_amount
        source.save()
        destination.save()

        # with this action serializer.save() we create a object inside model of history
        # because AccountTransactionSerializer is our serializer and its model is history
        # so requirement fields for creating a history is:
        # created_time,transfer_amount,transfer_source,transfer_destination,account_amount
        # created_time is autofill and the other fields are inside request.data except account_amount
        # we pass it to our serializer.save()
        serializer.save(account_amount=source.amount)

        return Response('done')

    @action(detail=False, methods=['POST'])
    def withdraw(self, request):
        serializer = AccountWithdrawSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        source = data.get('transfer_source')
        transfer_amount = data.get('transfer_amount')

        source.amount = source.amount - transfer_amount
        source.save()
        serializer.save(account_amount=source.amount)
        return Response('done')

    @action(detail=False, methods=['POST'])
    def deposit(self, request):
        serializer = AccountDepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        destination = data.get('transfer_destination')

        transfer_amount = data.get('transfer_amount')
        destination.amount = destination.amount + transfer_amount
        destination.save()
        serializer.save(account_amount=destination.amount)
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
        filter_backend = [filters.OrderingFilter]
        ordering_fields = ['created_time']

        def get_queryset(request):
            params = request.query_params.get('type')
            if params == 'deposit':
                queryset = History.objects.filter(transfer_destination=pk)
            elif params == 'withdraw':
                queryset = History.objects.filter(transfer_source=pk)
            else:
                queryset = History.objects.filter(Q(transfer_source=pk) | Q(transfer_destination=pk)).order_by(
                    '-created_time')
            return queryset

        serializer = AccountHistoryListSerializer(get_queryset(request), many=True)
        return Response(serializer.data)
