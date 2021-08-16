from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action, authentication_classes
from rest_framework.authentication import TokenAuthentication

from .serializer import CustomerSerializer, CustomerLoginSerializer, CustomerGetInfoSerializer

from .models import Customer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet,
                      APIView):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # detail:True or False
    # depending on whether this endpoint is expected to deal with a single object or a group of objects.
    # Since we use single object of user info we have set detail=True.
    # our login method is a type of POST
    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        serializer = CustomerLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            # customer = Customer.objects.get(username=data.get("username"), password=data.get("password"))
            customer = Customer.objects.filter(username=data.get("username"), password=data.get("password")).first()
            token, _ = Token.objects.get_or_create(user=customer)
            return Response(token.key)
        except Customer.DoesNotExist:
            raise ()
        except Customer.MultipleObjectsReturned:
            raise Http404()

    # get_info method is the same as retrieve
    @action(detail=False, methods=['GET'])
    @authentication_classes([TokenAuthentication])
    def get_info(self, request, *args, **kwargs):
        instance = request.user
        serializer = CustomerGetInfoSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    @authentication_classes([TokenAuthentication])
    def test(self, request, *args, **kwargs):
        user = request.user
        content = {'message': 'hello this is Demo!', 'username': user.username}
        return Response(content)
