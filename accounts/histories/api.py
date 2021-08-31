from django.db.models import Q

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from .models import History

from .serializer import HistorySerializer, HistoryListSerializer


class HistoryViewSet(  # mixins.CreateModelMixin,
                    # mixins.UpdateModelMixin,
                    # mixins.ListModelMixin,
                    # mixins.RetrieveModelMixin,
                    # mixins.DestroyModelMixin,
                    GenericViewSet):
    model = History
    serializer_class = HistoryListSerializer

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