from careers.models import Careers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    GenericAPIView
)
from rest_framework import status
from .serializers import (
    CreateCareersSerializer,
    PatchCareersSerializer,
    DeleteProductsSerializer,
    ListCareersSerializer
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
        id = kwargs.get('pk')        
        queryset = Careers.objects.filter(id=id).first()
        if queryset:
            get_serializer = self.get_serializer_class()
            serializer = get_serializer(queryset, request.data, partial=True)
            if serializer.is_valid():
                import ipdb
                ipdb.set_trace()
                serializer.save()
            return JsonResponse(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            queryset = Careers.objects.filter(id=id)
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PatchCareersSerializer
        return DeleteProductsSerializer
