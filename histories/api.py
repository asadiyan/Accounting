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
