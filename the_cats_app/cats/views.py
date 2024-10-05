from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


@api_view(["GET", "POST"])
def cat_list(request: HttpRequest) -> Response:
    if request.method == "POST":
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)


@api_view(["GET", "PATCH", "DELETE"])
def cat_detail(request: HttpRequest, pk: int) -> Response:
    cat = Cat.objects.get(pk=pk)
    if request.method == "PATCH":
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = CatSerializer(cat)
    return Response(serializer.data, status=status.HTTP_200_OK)
