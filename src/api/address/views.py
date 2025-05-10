from rest_framework import viewsets
from address.models import Address
from .serializers import AddressSerializer
from ..permissions import AddressPermission

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AddressPermission]