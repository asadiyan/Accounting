from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from .models import History

from .serializer import HistorySerializer


class HistoryViewSet(  # mixins.CreateModelMixin,
                    # mixins.UpdateModelMixin,
                    # mixins.ListModelMixin,
                    # mixins.RetrieveModelMixin,
                    # mixins.DestroyModelMixin,
                    GenericViewSet):
    model = History
    queryset = model.objects.all()
    serializer_class = HistorySerializer

    # @action(detail=False, methods=['GET'])
    # def get_history(self, request, *args, **kwargs):
    #     model = History
    #     queryset = model.objects.filter(transfer_source_id=request.user.id)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = HistorySerializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = HistorySerializer(queryset, many=True)
    #     return Response(serializer.data)
