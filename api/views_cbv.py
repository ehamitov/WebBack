from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from api.serializers import CategoryModelSerializer, CategoryWithProductModelSerializer, ProductModelSerializer, \
    ProductSerializer, Product2ModelSerializer
from api.models import Category, Product
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = Product2ModelSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #permission_classes = (IsAuthenticated,)


class ProductDetailAPIView(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist as e:
            return Response({'Error': str(e)})

    def get(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductModelSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_id):
        product = self.get_object(product_id)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})

    def delete(self, request, product_id):
        product = self.get_object(product_id)
        product.delete()
        return Response({'deleted': True})

    #permission_classes = (IsAuthenticated,IsAdminUser,)


class ThreeCheapProductAPIView(APIView):
    def get(self, request):
        top_three = Product.objects.order_by('price')[:3]
        serializer = ProductModelSerializer(top_three, many=True)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated,)
