from django.urls import path

from . import views


urlpatterns = [
    path("customers/", views.CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path("customers/<int:pk>/", views.CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
]
