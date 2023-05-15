from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Product
from .serializer import ProductSerializer


@api_view(['GET'])
def get_products(request: Request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

