from rest_framework.viewsets import mixins, GenericViewSet

from .serializer import BankSerializer

from .models import Bank


class BankViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):

    model = Bank
    queryset = model.objects.all()
    serializer_class = BankSerializer
