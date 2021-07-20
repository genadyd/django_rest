from pprint import pprint

from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Categories
from rest.serializers.categories_serializers import CategoriesSerializer


class CategoriesListView(APIView):

    def get(self, request):
        categories = []
        """
        categories = Categories.objects.queryset() ++++ Alternative
        """
        for p in Categories.objects.raw('SELECT id, name, description, slug, IFNULL(parent_id, 0) as parent_id '
                                        'FROM categories ORDER BY parent_id'):
            categories.append(p)
        ser_data = CategoriesSerializer(categories, many=True)
        return Response(ser_data.data)


class CategoryGetDetails(APIView):

    def get(self, request, ct_id):
        pprint(ct_id)
        # get one record (by id)
        category = Categories.objects.get(id=ct_id,)
        one_cat = CategoriesSerializer(category)
        return Response(one_cat.data)
