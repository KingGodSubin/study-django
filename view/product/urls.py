from django.urls import path

from product.views import ProductDetailView, ProductDetailAPI

appname = 'products'

urlpatterns = [
    path('detail/', ProductDetailView.as_view(), name='detail'),
    path('<int:product_id>/', ProductDetailAPI.as_view(), name='product-api'),
]