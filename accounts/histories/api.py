from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.filters import OrderingFilter
from .models import History



from .serializer import HistorySerializer, HistoryListSerializer


class HistoryViewSet(  # mixins.CreateModelMixin,
                    # mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    # mixins.RetrieveModelMixin,
                    # mixins.DestroyModelMixin,
                    GenericViewSet):

    model = History
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-created_time']

    def get_queryset(self):
        transfer_type = self.request.query_params.get('type')
        pk = self.request.query_params.get('account_id')

        if transfer_type == 'deposit':
            queryset = History.objects.filter(transfer_destination=pk)
        elif transfer_type == 'withdraw':
            queryset = History.objects.filter(transfer_source=pk)
        else:
            queryset = History.objects.filter(Q(transfer_source=pk) | Q(transfer_destination=pk))
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = HistoryListSerializer(queryset, many=True)
        return Response(serializer.data)

