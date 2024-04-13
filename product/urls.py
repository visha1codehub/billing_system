from django.urls import path

from . import views

urlpatterns = [
    path('prodcuts/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('prodcuts/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]