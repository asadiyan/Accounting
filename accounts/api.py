from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action

from .serializer import AccountSerializer, AccountGetInfoSerializer

from .models import Account


class AccountViewSets(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet
                      ):
    model = Account
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # @action(detail=False, methods=['POST'])
    # def account_registry(self):
    #     pass
    #
    # @action(detail=True, methods=['GET'])
    # def get_info(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = AccountGetInfoSerializer(instance)
    #     return Response(serializer.data)
    #
    # @action(detail=False, method=['POST'])
    # def deposit(self, request):
    #     instance = self.get_object()
