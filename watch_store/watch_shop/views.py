from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from requests import Response
from rest_framework import generics, permissions

from .models import Brand, SubBrand, Product
from .serializers import BrandListSerializer, BrandDetailSerializer, CRUDBrandSerializer


class BrandListView(generics.ListAPIView):
    """brand list"""

    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer


class BrandDetailView(generics.RetrieveAPIView):
    """brand detail"""

    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer
    lookup_field = 'slug_brand'


class BrandCreateView(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = CRUDBrandSerializer


class BrandUpdateView(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = CRUDBrandSerializer
    lookup_field = 'slug_brand'


class BrandDeleteView(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = CRUDBrandSerializer
    lookup_field = 'slug_brand'
