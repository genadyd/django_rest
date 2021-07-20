from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Products
from rest.serializers.products_serializers import ProductsSerializer


class ProductsListView(APIView):

    def get(self, request):
        products = []
        """
            products = Products.objects.queryset() ++++ Alternative
            """
        for p in Products.objects.raw('SELECT id, name, slug, description, image, category_id '
                                      'FROM products ORDER BY id'):
            products.append(p)
        ser_data = ProductsSerializer(products, many=True)
        return Response(ser_data.data)


class ProductGetDetails(APIView):

    def get(self, request, prod_id):
        # get one record (by id)
        product = Products.objects.get(id=prod_id, )
        one_prod = ProductsSerializer(product)
        return Response(one_prod.data)
