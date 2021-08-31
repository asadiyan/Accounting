from django.db.models import Q
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from .models import History

from .serializer import HistorySerializer, HistoryListSerializer


class HistoryViewSet(  # mixins.CreateModelMixin,
                    # mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    # mixins.RetrieveModelMixin,
                    # mixins.DestroyModelMixin,
                    GenericViewSet):

    model = History
    queryset = model.objects.all()
    serializer_class = HistoryListSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['__all__']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def history(self, request, pk):

        def get_queryset(request):
            transfer_type = request.query_params.get('type')
            if transfer_type == 'deposit':
                queryset = History.objects.filter(transfer_destination=pk)
            elif transfer_type == 'withdraw':
                queryset = History.objects.filter(transfer_source=pk)
            else:
                queryset = History.objects.filter(Q(transfer_source=pk) | Q(transfer_destination=pk)).order_by(
                    '-created_time')
            return queryset

        serializer = HistoryListSerializer(get_queryset(request), many=True)
        return Response(serializer.data)