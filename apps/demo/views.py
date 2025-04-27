# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response  import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.demo.models import CAR
from apps.demo.serializers import CARSERIALIZER


# Create your views here.


class CARFILTER(django_filters.FilterSet):
    make = django_filters.CharFilter(lookup_expr='icontains')  # Case insensitive search
    model = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.NumberFilter()
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  # price >= min
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  # price <= max

    class Meta:
        model = CAR
        fields = ['make', 'model', 'year', 'price_min', 'price_max']

@api_view(['GET','POST'])
def CARLISTAPI(request):
    if request.method == "POST":
        serializers = CARSERIALIZER(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data":serializers.data},status=status.HTTP_201_CREATED)
        else:
            return Response({"ERROR":serializers.errors,'Message':'oops something is wrong'},status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        InsertQuerySet = CAR.objects.all()
        serializers = CARSERIALIZER(InsertQuerySet,many=True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)


@api_view(['GET','PUT','DELETE','PATCH'])
def CARDETAILSAPI(request,id):
    try:
        InsertQuerySet = CAR.objects.get(id=id)
    except CAR.DoesNotExist:
        return Response({'Message':"data not found"},status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == "GET":
            serializers = CARSERIALIZER(InsertQuerySet)
            return Response({"data":serializers.data},status=status.HTTP_200_OK)
        
        if request.method == "PUT":
            serializers = CARSERIALIZER(InsertQuerySet,data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({"data":serializers.data},status=status.HTTP_200_OK)
            else:
                return Response({"ERROR":serializers.errors,'Message':'oops something is wrong'},status=status.HTTP_400_BAD_REQUEST)

        if request.method == "PATCH":
            serializers = CARSERIALIZER(InsertQuerySet,data = request.data,partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response({"data":serializers.data},status=status.HTTP_200_OK)
            else:
                return Response({"ERROR":serializers.errors,'Message':'oops something is wrong'},status=status.HTTP_400_BAD_REQUEST)       

        
        if request.method == "DELETE":
            InsertQuerySet.delete()
            return Response({'Message': "Stock deleted successfully" }, status=status.HTTP_204_NO_CONTENT)


