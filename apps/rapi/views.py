from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import viewsets
from apps.rapi.serializers import CARSERIALIZERS
from apps.rapi.models import CAR

class CARLISTAPI(viewsets.ModelViewSet):
    queryset = CAR.objects.all()
    serializer_class = CARSERIALIZERS

    # Add filters and ordering
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ['price', 'year', 'make']  # Example fields you can order by
    filterset_fields = ['make', 'model', 'year']  # Example fields you can filter by

