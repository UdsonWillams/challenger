from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from careers.models import Careers

from .serializers import (
    CreateCareersSerializer,
    DeleteProductsSerializer,
    ListCareersSerializer,
    PatchCareersSerializer,
)


class ListCreateCareersView(ListCreateAPIView):
    """List and Create a Career"""

    def get_queryset(self):
        queryset = Careers.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateCareersSerializer
        return ListCareersSerializer


class PatchOrDeleteCareersView(GenericAPIView):
    """Patch or Delete a Career"""

    def patch(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        queryset = Careers.objects.filter(id=id).first()
        if queryset:
            get_serializer = self.get_serializer_class()
            serializer = get_serializer(queryset, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        if id:
            queryset = Careers.objects.filter(id=id)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PatchCareersSerializer
        return DeleteProductsSerializer
