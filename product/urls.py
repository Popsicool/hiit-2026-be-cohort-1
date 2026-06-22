from django.urls import path
from product.views import ProductViews, SingleProductView, BulkProductSerializer, SaleView

urlpatterns = [
    path("sell/", SaleView.as_view()),
    path("bulk-delete/", BulkProductSerializer.as_view()),
    path("<product_id>/", SingleProductView.as_view()),
    path("", ProductViews.as_view()),
]

#* https://localhost:8000/product/abc-xyz