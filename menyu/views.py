from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView

from menyu.filters import ProductFilter
from menyu.models import Menyu
from menyu.serializer import MenyuListSeralizer


# Create your views here.


class MenyuListCreateView(ListCreateAPIView):
    queryset = Menyu.objects.all()
    serializer_class = MenyuListSeralizer
    filter_backends = DjangoFilterBackend,
    # filterset_fields = 'category',
    filterset_class = ProductFilter


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSeralizer(products, many=True).data
        data = {
            'products': f'All products: {len(products)}',
            'status': status.HTTP_200_OK,
            'data': serializer

        }
        return Response(data)

class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product.objects.all(), id=pk)
        serializer = ProductDetailSeralizer(product).data
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer

        }
        return Response(data)

class ProductPostAPIView(APIView):
    def post(self, request):
        serializer = ProductPostSerializer(data=request.data)
        product = get_object_or_404(Product.objects.all(), id=request.data['id'])
        data = {'status': status.HTTP_200_OK, 'data': serializer}
        return Response(data)

class ProductUpdateAPIView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product.objects.all(), id=pk)
        serializer = ProductPostSerializer(data=request.data)
        data = {'status': status.HTTP_200_OK, 'data': serializer}
        return Response(data)

class ProductDeleteAPIView(APIView):
    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), id=pk)
        data = {'status': status.HTTP_200_OK, 'data': product}
        return Response(data)

