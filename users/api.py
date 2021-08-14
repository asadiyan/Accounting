from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action

from .serializer import CustomerSerializer, CustomerLoginSerializer, CustomerGetInfoSerializer

from .models import Customer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # detail:True or False
    # depending on whether this endpoint is expected to deal with a single object or a group of objects.
    # Since we use single object of user info we have set detail=True.
    # our login method is a type of POST
    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if Customer.objects.filter(username=data.get("username"), password=data.get("password")).exists():
            print("ok")

        return Response(serializer.data)

    # get_info method is the same as retrieve
    @action(detail=True, methods=["GET"])
    def get_info(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CustomerGetInfoSerializer(instance)
        return Response(serializer.data)

