from django.contrib import admin
from django.urls import path

from products.views import ProducListAPI, ProductFormView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("api/", ProducListAPI.as_view(), name="list_product_api"),
    path("create/", ProductFormView.as_view(), name="create_product"),
]
