from django.urls import path
from .views import *

urlpatterns = [
    path('api/brands/', BrandListView.as_view()),
    path('api/brands/get/<slug:slug_brand>/', BrandDetailView.as_view()),
    path('api/brands/create/', BrandCreateView.as_view()),
    path('api/brands/update/<slug:slug_brand>/', BrandUpdateView.as_view()),
    path('api/brands/delete/<slug:slug_brand>/', BrandDeleteView.as_view()),

]